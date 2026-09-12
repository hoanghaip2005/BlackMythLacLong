import math
import os
from pathlib import Path

import bpy
from mathutils import Vector


ROOT = Path(__file__).resolve().parent.parent
OUT_DIR = ROOT / "assets" / "characters" / "long_nhan"
OUT_DIR.mkdir(parents=True, exist_ok=True)


def clear_scene():
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete(use_global=False)
    for datablocks in (bpy.data.meshes, bpy.data.curves, bpy.data.materials, bpy.data.cameras, bpy.data.lights):
        for block in list(datablocks):
            if block.users == 0:
                datablocks.remove(block)


def make_collection(name):
    collection = bpy.data.collections.new(name)
    bpy.context.scene.collection.children.link(collection)
    return collection


def move_to_collection(obj, collection):
    for current in list(obj.users_collection):
        current.objects.unlink(obj)
    collection.objects.link(obj)


def material(name, color, metallic=0.0, roughness=0.5, emission=None):
    mat = bpy.data.materials.new(name)
    mat.diffuse_color = (*color, 1.0)
    mat.use_nodes = True
    bsdf = mat.node_tree.nodes.get("Principled BSDF")
    bsdf.inputs["Base Color"].default_value = (*color, 1.0)
    bsdf.inputs["Metallic"].default_value = metallic
    bsdf.inputs["Roughness"].default_value = roughness
    if emission:
        emission_color = bsdf.inputs.get("Emission Color")
        emission_strength = bsdf.inputs.get("Emission Strength")
        if emission_color:
            if emission_strength:
                emission_color.default_value = (*emission[0], 1.0)
                emission_strength.default_value = emission[1]
            else:
                emission_color.default_value = tuple(channel * emission[1] for channel in emission[0]) + (1.0,)
    return mat


def assign(obj, mat):
    obj.data.materials.append(mat)
    return obj


def bevel(obj, width=0.08, segments=2):
    modifier = obj.modifiers.new("soft_handmade_edges", "BEVEL")
    modifier.width = width
    modifier.segments = segments
    modifier.limit_method = "ANGLE"
    return obj


def cube(name, location, scale, mat, collection, rotation=(0.0, 0.0, 0.0), bevel_width=0.08):
    bpy.ops.mesh.primitive_cube_add(size=1.0, location=location, rotation=rotation)
    obj = bpy.context.object
    obj.name = name
    obj.scale = scale
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    assign(obj, mat)
    bevel(obj, bevel_width)
    move_to_collection(obj, collection)
    return obj


def sphere(name, location, scale, mat, collection, segments=20, rings=12):
    bpy.ops.mesh.primitive_uv_sphere_add(segments=segments, ring_count=rings, location=location)
    obj = bpy.context.object
    obj.name = name
    obj.scale = scale
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    assign(obj, mat)
    move_to_collection(obj, collection)
    return obj


def ico(name, location, scale, mat, collection, subdivisions=1):
    bpy.ops.mesh.primitive_ico_sphere_add(subdivisions=subdivisions, radius=1.0, location=location)
    obj = bpy.context.object
    obj.name = name
    obj.scale = scale
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    assign(obj, mat)
    move_to_collection(obj, collection)
    return obj


def cylinder(name, location, radius, depth, mat, collection, vertices=12, rotation=(0.0, 0.0, 0.0)):
    bpy.ops.mesh.primitive_cylinder_add(vertices=vertices, radius=radius, depth=depth, location=location, rotation=rotation)
    obj = bpy.context.object
    obj.name = name
    assign(obj, mat)
    bevel(obj, min(radius * 0.28, 0.08), 2)
    move_to_collection(obj, collection)
    return obj


def cylinder_between(name, start, end, radius, mat, collection, vertices=12):
    start = Vector(start)
    end = Vector(end)
    direction = end - start
    obj = cylinder(name, (start + end) / 2.0, radius, direction.length, mat, collection, vertices)
    obj.rotation_mode = "QUATERNION"
    obj.rotation_quaternion = direction.to_track_quat("Z", "Y")
    return obj


def torus(name, location, major_radius, minor_radius, mat, collection, scale=(1.0, 1.0, 1.0)):
    bpy.ops.mesh.primitive_torus_add(
        major_radius=major_radius,
        minor_radius=minor_radius,
        major_segments=32,
        minor_segments=8,
        location=location,
    )
    obj = bpy.context.object
    obj.name = name
    obj.scale = scale
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    assign(obj, mat)
    move_to_collection(obj, collection)
    return obj


def axe_head(name, location, mat, collection):
    # A broad stone blade with an asymmetrical, hand-forged silhouette.
    outline = [(-0.65, -0.45), (-0.35, 0.35), (0.05, 0.62), (0.62, 0.48), (0.48, -0.30), (0.12, -0.58)]
    thickness = 0.20
    vertices = []
    for y in (-thickness, thickness):
        vertices.extend([(x, y, z) for x, z in outline])
    faces = []
    faces.append(tuple(range(6)))
    faces.append(tuple(range(6, 12)))
    for index in range(6):
        next_index = (index + 1) % 6
        faces.append((index, next_index, next_index + 6, index + 6))
    mesh = bpy.data.meshes.new(name + "_mesh")
    mesh.from_pydata(vertices, [], faces)
    mesh.update()
    obj = bpy.data.objects.new(name, mesh)
    collection.objects.link(obj)
    obj.location = location
    assign(obj, mat)
    bevel(obj, 0.07, 2)
    return obj


def sun_disk(name, location, mat, collection, radius=0.24):
    cylinder(name, location, radius, 0.10, mat, collection, vertices=16, rotation=(math.pi / 2.0, 0.0, 0.0))
    for angle in range(0, 360, 45):
        radians = math.radians(angle)
        start = Vector(location) + Vector((math.cos(radians) * radius * 0.75, -0.08, math.sin(radians) * radius * 0.75))
        end = Vector(location) + Vector((math.cos(radians) * radius * 1.45, -0.08, math.sin(radians) * radius * 1.45))
        cylinder_between(name + "_ray_" + str(angle), start, end, 0.025, mat, collection, 6)


def look_at(obj, target):
    direction = Vector(target) - obj.location
    obj.rotation_euler = direction.to_track_quat("-Z", "Y").to_euler()


def build_character():
    clear_scene()
    body = make_collection("LONG_NHAN_BODY")
    costume = make_collection("LONG_NHAN_VIET_COSTUME")
    weapon = make_collection("LONG_NHAN_WEAPON")
    stage = make_collection("PRESENTATION_STAGE")

    skin = material("skin_warm_bronze", (0.38, 0.16, 0.09), roughness=0.72)
    skin_light = material("skin_highlight", (0.64, 0.30, 0.16), roughness=0.66)
    hair = material("hair_ink_black", (0.018, 0.012, 0.010), roughness=0.36)
    indigo = material("indigo_dye", (0.025, 0.09, 0.15), roughness=0.72)
    teal = material("river_teal", (0.03, 0.24, 0.25), roughness=0.62)
    cloth_red = material("earth_red_sash", (0.42, 0.08, 0.045), roughness=0.66)
    woven_brown = material("woven_brown", (0.22, 0.095, 0.035), roughness=0.86)
    bronze = material("dong_son_bronze", (0.34, 0.16, 0.045), metallic=0.72, roughness=0.30)
    jade = material("river_jade", (0.02, 0.30, 0.22), metallic=0.18, roughness=0.28)
    stone = material("thach_son_stone", (0.12, 0.16, 0.18), metallic=0.08, roughness=0.54)
    stone_edge = material("axe_edge_ember", (0.34, 0.045, 0.018), metallic=0.24, roughness=0.30, emission=((0.70, 0.06, 0.01), 2.2))
    eye = material("dragon_amber_eye", (0.72, 0.30, 0.025), metallic=0.05, roughness=0.22, emission=((1.0, 0.18, 0.01), 4.0))
    eye_dark = material("pupil", (0.005, 0.002, 0.001), roughness=0.22)
    stage_mat = material("wet_black_stone", (0.012, 0.025, 0.032), metallic=0.25, roughness=0.34)
    water_mat = material("deep_water", (0.005, 0.055, 0.075), metallic=0.12, roughness=0.18, emission=((0.0, 0.12, 0.18), 0.35))

    root = bpy.data.objects.new("Long_Nhan_Root", None)
    body.objects.link(root)

    # Legs and boots: grounded, athletic silhouette.
    cube("leg_left", (-0.52, -0.18, 1.78), (0.42, 0.48, 1.20), indigo, body, rotation=(0.0, -0.06, -0.05), bevel_width=0.14)
    cube("leg_right", (0.52, 0.12, 1.78), (0.42, 0.48, 1.20), indigo, body, rotation=(0.0, 0.06, 0.04), bevel_width=0.14)
    cube("boot_left", (-0.58, -0.45, 0.48), (0.50, 0.72, 0.42), woven_brown, costume, rotation=(0.0, -0.08, -0.04), bevel_width=0.12)
    cube("boot_right", (0.58, -0.18, 0.48), (0.50, 0.72, 0.42), woven_brown, costume, rotation=(0.0, 0.10, 0.04), bevel_width=0.12)
    cube("boot_left_wrap", (-0.58, -0.45, 0.82), (0.53, 0.56, 0.12), cloth_red, costume, rotation=(0.0, -0.08, -0.04), bevel_width=0.05)
    cube("boot_right_wrap", (0.58, -0.18, 0.82), (0.53, 0.56, 0.12), cloth_red, costume, rotation=(0.0, 0.10, 0.04), bevel_width=0.05)

    # Layered tunic: an ao tu than inspired split silhouette, kept simple and combat-ready.
    cube("torso_underlayer", (0.0, 0.02, 4.55), (1.14, 0.66, 1.45), teal, body, bevel_width=0.20)
    cube("front_wrap_panel", (0.0, -0.69, 4.05), (0.88, 0.10, 1.45), indigo, costume, rotation=(0.0, 0.0, -0.035), bevel_width=0.09)
    cube("coat_left_panel", (-0.77, -0.05, 3.55), (0.56, 0.17, 1.25), indigo, costume, rotation=(0.0, 0.06, -0.10), bevel_width=0.10)
    cube("coat_right_panel", (0.77, -0.05, 3.55), (0.56, 0.17, 1.25), indigo, costume, rotation=(0.0, -0.06, 0.10), bevel_width=0.10)
    cube("sash", (0.0, -0.02, 4.06), (1.20, 0.78, 0.18), cloth_red, costume, bevel_width=0.06)
    cube("sash_tail_left", (-0.46, -0.76, 3.55), (0.22, 0.08, 0.72), cloth_red, costume, rotation=(0.0, 0.0, -0.17), bevel_width=0.04)
    cube("sash_tail_right", (0.10, -0.78, 3.42), (0.22, 0.08, 0.82), cloth_red, costume, rotation=(0.0, 0.0, 0.13), bevel_width=0.04)

    # Dong Son-inspired sun disk: a circular radial symbol, not a Chinese cloud/dragon motif.
    sun_disk("dong_son_sun_disk", (0.0, -0.83, 4.82), bronze, costume, radius=0.25)
    torus("sash_buckle", (0.0, -0.83, 4.08), 0.19, 0.045, bronze, costume, scale=(1.0, 0.72, 1.0))
    sphere("buckle_core", (0.0, -0.88, 4.08), (0.09, 0.04, 0.09), jade, costume, 12, 8)

    # Shoulders and arms.
    sphere("shoulder_left", (-1.16, 0.0, 5.40), (0.48, 0.50, 0.46), teal, costume)
    sphere("shoulder_right", (1.16, 0.0, 5.40), (0.48, 0.50, 0.46), teal, costume)
    cylinder_between("upper_arm_left", (-1.18, 0.0, 5.25), (-1.70, -0.30, 4.38), 0.32, indigo, body, 10)
    cylinder_between("upper_arm_right", (1.18, 0.0, 5.25), (1.52, -0.42, 4.25), 0.32, indigo, body, 10)
    cylinder_between("forearm_left", (-1.70, -0.30, 4.38), (-1.92, -0.52, 3.82), 0.22, skin_light, body, 10)
    cylinder_between("forearm_right", (1.52, -0.42, 4.25), (1.44, -0.70, 3.72), 0.22, skin_light, body, 10)
    cylinder_between("bracer_left", (-1.78, -0.42, 4.12), (-1.91, -0.52, 3.84), 0.28, bronze, costume, 10)
    cylinder_between("bracer_right", (1.48, -0.58, 4.00), (1.44, -0.70, 3.74), 0.28, bronze, costume, 10)
    sphere("hand_left", (-1.94, -0.54, 3.70), (0.25, 0.22, 0.26), skin, body)
    sphere("hand_right", (1.43, -0.73, 3.58), (0.25, 0.22, 0.26), skin, body)

    # Neck and head.
    cylinder("neck", (0.0, 0.0, 6.12), 0.35, 0.52, skin, body, 12)
    sphere("head", (0.0, -0.03, 7.06), (0.72, 0.64, 0.84), skin, body, 24, 16)
    sphere("hair_cap", (0.0, 0.02, 7.65), (0.75, 0.67, 0.46), hair, costume, 20, 12)
    sphere("topknot", (0.0, 0.05, 8.10), (0.32, 0.30, 0.42), hair, costume, 16, 10)
    cylinder("topknot_wrap", (0.0, -0.02, 7.88), 0.22, 0.12, cloth_red, costume, 12)
    torus("woven_headband", (0.0, -0.02, 7.54), 0.65, 0.075, cloth_red, costume, scale=(1.0, 0.86, 0.72))

    # Face: restrained, readable at medium distance.
    sphere("eye_left", (-0.28, -0.65, 7.22), (0.12, 0.055, 0.09), eye, body, 16, 8)
    sphere("eye_right", (0.28, -0.65, 7.22), (0.12, 0.055, 0.09), eye, body, 16, 8)
    sphere("pupil_left", (-0.28, -0.702, 7.22), (0.045, 0.022, 0.055), eye_dark, body, 12, 8)
    sphere("pupil_right", (0.28, -0.702, 7.22), (0.045, 0.022, 0.055), eye_dark, body, 12, 8)
    cube("brow_left", (-0.28, -0.66, 7.42), (0.17, 0.04, 0.035), hair, body, rotation=(0.0, 0.0, -0.12), bevel_width=0.025)
    cube("brow_right", (0.28, -0.66, 7.42), (0.17, 0.04, 0.035), hair, body, rotation=(0.0, 0.0, 0.12), bevel_width=0.025)
    ico("nose", (0.0, -0.72, 7.02), (0.12, 0.16, 0.20), skin_light, body, 1)
    cube("mouth_shadow", (0.0, -0.68, 6.84), (0.16, 0.025, 0.025), hair, body, bevel_width=0.015)
    cube("cheek_scar", (0.43, -0.67, 7.00), (0.20, 0.025, 0.025), cloth_red, body, rotation=(0.0, 0.0, -0.38), bevel_width=0.015)

    # Small jade plates echo river scales without Chinese dragon/cloud ornament.
    for index, x in enumerate((-0.72, -0.48, 0.48, 0.72)):
        sphere("river_scale_" + str(index), (x, -0.72, 5.20 + abs(x) * 0.18), (0.10, 0.035, 0.13), jade, costume, 12, 8)

    # Rìu Thần Thạch Sơn is anchored to the right hand for a readable hero pose.
    cylinder_between("axe_haft", (1.43, -0.73, 3.58), (1.88, 0.10, 7.22), 0.105, woven_brown, weapon, 10)
    axe_head("axe_head", (1.90, 0.10, 7.32), stone, weapon)
    cube("axe_edge_mark_1", (1.60, 0.10, 7.40), (0.05, 0.025, 0.36), stone_edge, weapon, rotation=(0.0, 0.0, -0.48), bevel_width=0.02)
    cube("axe_edge_mark_2", (1.77, 0.10, 7.18), (0.04, 0.025, 0.22), stone_edge, weapon, rotation=(0.0, 0.0, 0.36), bevel_width=0.02)
    sun_disk("axe_sun_mark", (1.58, 0.08, 7.36), bronze, weapon, radius=0.10)

    # Presentation stage.
    cylinder("wet_stone_plinth", (0.0, 0.0, -0.24), 2.8, 0.40, stage_mat, stage, 64)
    torus("water_ring", (0.0, 0.0, -0.02), 2.55, 0.035, water_mat, stage, scale=(1.0, 0.78, 1.0))
    for x, y, z, scale in [(-2.6, 0.8, 0.18, 0.75), (2.4, 0.5, 0.22, 0.62), (-2.0, -1.2, 0.18, 0.50)]:
        ico("coral_fragment", (x, y, z), (scale * 0.35, scale * 0.25, scale), jade, stage, 1)

    # Lighting and camera.
    scene = bpy.context.scene
    scene.render.engine = "BLENDER_EEVEE_NEXT"
    scene.render.resolution_x = 760
    scene.render.resolution_y = 1024
    scene.render.resolution_percentage = 100
    scene.render.image_settings.file_format = "PNG"
    scene.render.filepath = str(OUT_DIR / "long_nhan_preview.png")
    scene.world.color = (0.004, 0.008, 0.012)
    try:
        scene.view_settings.look = "AgX - Medium High Contrast"
    except Exception:
        pass

    def area_light(name, location, energy, color, size):
        data = bpy.data.lights.new(name, "AREA")
        data.energy = energy
        data.color = color
        data.shape = "DISK"
        data.size = size
        obj = bpy.data.objects.new(name, data)
        stage.objects.link(obj)
        obj.location = location
        look_at(obj, (0.0, 0.0, 4.0))
        return obj

    area_light("key_cool", (4.5, -7.5, 9.5), 1050, (0.36, 0.62, 1.0), 4.0)
    area_light("fill_warm", (-5.0, -4.0, 5.8), 780, (1.0, 0.34, 0.12), 3.5)
    area_light("rim_teal", (2.5, 3.5, 8.5), 1250, (0.02, 0.56, 0.50), 3.0)

    camera_data = bpy.data.cameras.new("Long_Nhan_Camera")
    camera = bpy.data.objects.new("Long_Nhan_Camera", camera_data)
    stage.objects.link(camera)
    camera.location = (10.6, -17.5, 8.4)
    camera_data.lens = 58
    camera_data.sensor_width = 36
    look_at(camera, (0.18, 0.0, 4.25))
    scene.camera = camera

    # Organize viewport and save a ready-to-review file.
    for obj in bpy.context.scene.objects:
        obj.select_set(False)
    bpy.context.view_layer.objects.active = root
    root.select_set(True)
    root["design_note"] = "Vietnam-inspired hero: ao tu than split panels, Dong Son sun disk, woven sash, river jade accents. No Chinese cloud or imperial motifs."
    root["asset_status"] = "concept_blockout"
    root["character_id"] = "PLAYER-LONG-NHAN"
    scene["project"] = "Huyet Mach Lac Long"
    scene["asset_scope"] = "Main character visual blockout"
    scene["documentation_status"] = "Documentation intentionally deferred by user"
    bpy.ops.wm.save_as_mainfile(filepath=str(OUT_DIR / "long_nhan_concept.blend"))
    bpy.ops.render.render(write_still=True)


if __name__ == "__main__":
    build_character()
