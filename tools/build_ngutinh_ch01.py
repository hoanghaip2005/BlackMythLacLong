"""Chapter 01 boss: Ngu Tinh.

Built from the project's MPFB material and lighting pipeline, then extended
with a custom fish-monster assembly: tapered body, anatomical fins, jaw,
teeth, barbels, Dong Son jade shard, and a rebuilt fire tail.
"""

import math
import sys
from pathlib import Path

import bpy
from mathutils import Vector

TOOLS = Path(__file__).resolve().parent
ROOT = TOOLS.parent
OUT_DIR = ROOT / "assets" / "bosses" / "chapter_01_ngutinh"
OUT_DIR.mkdir(parents=True, exist_ok=True)
sys.path.insert(0, str(TOOLS))
import build_long_nhan as blockout
import build_long_nhan_v3 as hero


def mesh_object(name, vertices, faces, material, collection, smooth=True):
    mesh = bpy.data.meshes.new(name + "_mesh")
    mesh.from_pydata(vertices, [], faces)
    mesh.update()
    obj = bpy.data.objects.new(name, mesh)
    collection.objects.link(obj)
    blockout.assign(obj, material)
    if smooth:
        for polygon in mesh.polygons:
            polygon.use_smooth = True
    return obj


def fish_material(name, dark, light):
    mat, tree, bsdf = hero._principled(name)
    nodes, links = tree.nodes, tree.links
    coord = nodes.new("ShaderNodeTexCoord")
    noise = nodes.new("ShaderNodeTexNoise")
    noise.inputs["Scale"].default_value = 8.0
    noise.inputs["Detail"].default_value = 7.0
    noise.inputs["Roughness"].default_value = 0.70
    ramp = nodes.new("ShaderNodeValToRGB")
    ramp.color_ramp.elements[0].position = 0.24
    ramp.color_ramp.elements[0].color = (*dark, 1.0)
    ramp.color_ramp.elements[1].position = 0.76
    ramp.color_ramp.elements[1].color = (*light, 1.0)
    scale_noise = nodes.new("ShaderNodeTexNoise")
    scale_noise.inputs["Scale"].default_value = 34.0
    scale_noise.inputs["Detail"].default_value = 3.0
    bump = nodes.new("ShaderNodeBump")
    bump.inputs["Strength"].default_value = 0.34
    bump.inputs["Distance"].default_value = 0.035
    links.new(coord.outputs["Object"], noise.inputs["Vector"])
    links.new(coord.outputs["Object"], scale_noise.inputs["Vector"])
    links.new(noise.outputs["Fac"], ramp.inputs["Fac"])
    links.new(ramp.outputs["Color"], bsdf.inputs["Base Color"])
    links.new(scale_noise.outputs["Fac"], bump.inputs["Height"])
    links.new(bump.outputs["Normal"], bsdf.inputs["Normal"])
    bsdf.inputs["Roughness"].default_value = 0.42
    bsdf.inputs["Metallic"].default_value = 0.05
    return mat


def emissive_material(name, color, strength):
    mat, tree, bsdf = hero._principled(name)
    bsdf.inputs["Base Color"].default_value = (*color, 1.0)
    bsdf.inputs["Roughness"].default_value = 0.22
    if "Emission Color" in bsdf.inputs:
        bsdf.inputs["Emission Color"].default_value = (*color, 1.0)
        if "Emission Strength" in bsdf.inputs:
            bsdf.inputs["Emission Strength"].default_value = strength
        else:
            bsdf.inputs["Emission Color"].default_value = tuple(channel * strength for channel in color) + (1.0,)
    return mat


def make_materials():
    mats = hero.make_materials()
    mats["fish"] = fish_material("ngu_tinh_deep_teal_skin", (0.004, 0.028, 0.040), (0.025, 0.20, 0.22))
    mats["belly"] = fish_material("ngu_tinh_ash_belly", (0.10, 0.075, 0.055), (0.38, 0.27, 0.15))
    mats["scale"] = hero.bronze_material("ngu_tinh_oxidized_bronze_scale")
    mats["mouth"] = blockout.material("ngu_tinh_mouth", (0.045, 0.003, 0.002), roughness=0.32, emission=((0.12, 0.006, 0.002), 0.35))
    mats["eye"] = emissive_material("ngu_tinh_amber_eye", (1.0, 0.12, 0.006), 8.0)
    mats["gill"] = blockout.material("ngu_tinh_gill_red", (0.30, 0.015, 0.006), roughness=0.48, emission=((0.32, 0.012, 0.003), 1.8))
    mats["bone"] = hero.stone_material("ngu_tinh_teeth_bone", (0.16, 0.11, 0.065), (0.62, 0.45, 0.22))
    mats["water"] = blockout.material("ngu_tinh_deep_water", (0.001, 0.018, 0.028), metallic=0.20, roughness=0.10, emission=((0.0, 0.10, 0.16), 0.45))
    mats["tail_fire"] = blockout.material("ngu_tinh_rebuilt_fire_tail", (0.16, 0.006, 0.001), roughness=0.30, emission=((0.75, 0.012, 0.001), 1.6))
    return mats


def loft_body(name, centers, radii, material, collection, segments=40):
    vertices = []
    frames = []
    for index, center in enumerate(centers):
        if index == 0:
            tangent = centers[1] - centers[0]
        elif index == len(centers) - 1:
            tangent = centers[-1] - centers[-2]
        else:
            tangent = centers[index + 1] - centers[index - 1]
        tangent.normalize()
        reference = Vector((0.0, 0.0, 1.0))
        if abs(tangent.dot(reference)) > 0.92:
            reference = Vector((1.0, 0.0, 0.0))
        axis_x = tangent.cross(reference).normalized()
        axis_z = axis_x.cross(tangent).normalized()
        frames.append((axis_x, axis_z))
        rx, rz = radii[index]
        for step in range(segments):
            angle = math.tau * step / segments
            vertices.append(tuple(center + axis_x * (math.cos(angle) * rx) + axis_z * (math.sin(angle) * rz)))
    faces = []
    for row in range(len(centers) - 1):
        for step in range(segments):
            nxt = (step + 1) % segments
            a = row * segments + step
            faces.append((a, row * segments + nxt, (row + 1) * segments + nxt, (row + 1) * segments + step))
    faces.append(tuple(reversed(range(segments))))
    base = (len(centers) - 1) * segments
    faces.append(tuple(base + step for step in range(segments)))
    return mesh_object(name, vertices, faces, material, collection)


def prism_from_2d(name, points, depth, material, collection, axis="x"):
    vertices = []
    for layer in (-depth / 2.0, depth / 2.0):
        for first, second in points:
            if axis == "x":
                vertices.append((layer, first, second))
            else:
                vertices.append((first, second, layer))
    count = len(points)
    faces = [tuple(range(count)), tuple(reversed(range(count, count * 2)))]
    for index in range(count):
        nxt = (index + 1) % count
        faces.append((index, nxt, nxt + count, index + count))
    return mesh_object(name, vertices, faces, material, collection, smooth=False)


def cone(name, location, radius, depth, material, collection, direction=(0.0, 0.0, 1.0), vertices=16):
    bpy.ops.mesh.primitive_cone_add(vertices=vertices, radius1=radius, radius2=0.0, depth=depth, location=location)
    obj = bpy.context.object
    obj.name = name
    obj.rotation_mode = "QUATERNION"
    obj.rotation_quaternion = Vector(direction).to_track_quat("Z", "Y")
    blockout.assign(obj, material)
    blockout.bevel(obj, min(radius * 0.22, 0.08), 2)
    blockout.move_to_collection(obj, collection)
    return obj


def create_scales(collection, mats):
    # Small overlapping plates create a fish surface without Chinese dragon motifs.
    locations = []
    for y, width, height in [(-0.65, 1.72, 3.75), (0.15, 1.88, 3.78), (0.95, 1.56, 3.80), (1.75, 1.18, 3.80)]:
        for index in range(7):
            x = -width + (2.0 * width * index / 6.0)
            z = height + 0.24 * math.sin(index * 1.7 + y)
            surface_y = y - math.sqrt(max(0.0, 1.0 - (x / max(width, 0.01)) ** 2)) * 0.34
            plate = blockout.sphere(
                "scale_plate_%02d" % len(locations),
                (x, surface_y - 0.18, z),
                (0.16, 0.055, 0.20),
                mats["scale"],
                collection,
                16,
                10,
            )
            plate.rotation_euler.y = math.radians(18 * math.sin(index + y))
            locations.append(plate)


def create_boss(collection, mats):
    body_centers = [
        Vector((0.0, -1.40, 3.55)),
        Vector((0.0, -0.70, 3.55)),
        Vector((0.0, 0.15, 3.55)),
        Vector((0.0, 1.10, 3.56)),
        Vector((0.0, 1.95, 3.60)),
        Vector((0.0, 2.65, 3.68)),
    ]
    body_radii = [(1.35, 1.28), (1.78, 1.55), (1.90, 1.70), (1.58, 1.42), (1.05, 0.98), (0.52, 0.48)]
    body = loft_body("ngu_tinh_main_body", body_centers, body_radii, mats["fish"], collection)
    tail_stalk_centers = [Vector((0.0, 2.15, 3.62)), Vector((0.0, 3.15, 3.72)), Vector((0.0, 4.05, 3.88))]
    tail_stalk_radii = [(0.68, 0.62), (0.40, 0.38), (0.16, 0.15)]
    loft_body("ngu_tinh_fire_tail_stalk", tail_stalk_centers, tail_stalk_radii, mats["fish"], collection, 32)

    belly_centers = [Vector((0.0, y, z - 0.44)) for y, z in [(-1.20, 3.38), (-0.40, 3.20), (0.45, 3.12), (1.25, 3.18), (1.95, 3.36)]]
    belly_radii = [(1.10, 0.42), (1.38, 0.52), (1.42, 0.56), (1.16, 0.46), (0.75, 0.30)]
    loft_body("ngu_tinh_ash_belly", belly_centers, belly_radii, mats["belly"], collection, 32)

    # Open maw facing the player.
    mouth = blockout.torus("ngu_tinh_open_maw", (0.0, -2.30, 3.48), 1.02, 0.17, mats["mouth"], collection, scale=(1.0, 1.0, 1.05))
    mouth.rotation_euler.x = math.pi / 2.0
    mouth_inner = blockout.sphere("ngu_tinh_mouth_depth", (0.0, -2.28, 3.48), (0.88, 0.10, 0.88), mats["mouth"], collection, 32, 20)
    upper_jaw = blockout.sphere("ngu_tinh_upper_jaw", (0.0, -2.02, 4.06), (1.20, 0.82, 0.36), mats["fish"], collection, 28, 16)
    lower_jaw = blockout.sphere("ngu_tinh_lower_jaw", (0.0, -2.04, 2.91), (1.18, 0.85, 0.32), mats["belly"], collection, 28, 16)

    # Amber eyes and short sockets, placed asymmetrically for the three-quarter camera.
    for side in (-1.0, 1.0):
        socket = blockout.sphere("ngu_tinh_eye_socket_%s" % ("l" if side < 0 else "r"), (side * 0.94, -2.04, 4.32), (0.30, 0.22, 0.30), mats["scale"], collection, 20, 12)
        eye = blockout.sphere("ngu_tinh_amber_eye_%s" % ("l" if side < 0 else "r"), (side * 0.98, -2.22, 4.34), (0.17, 0.10, 0.17), mats["eye"], collection, 20, 12)
        pupil = blockout.sphere("ngu_tinh_eye_slit_%s" % ("l" if side < 0 else "r"), (side * 0.98, -2.30, 4.34), (0.035, 0.025, 0.12), mats["mouth"], collection, 12, 8)

    # A Long Ngoc shard is embedded in the brow; this is the Chapter 01 phase anchor.
    shard = blockout.ico("manh_long_ngoc_ngu_tinh", (0.0, -2.23, 4.90), (0.24, 0.11, 0.34), mats["jade"], collection, 2)
    shard.rotation_euler = (math.radians(-15), 0.0, 0.0)

    # Teeth point down from the upper jaw and up from the lower jaw.
    for row, z, direction in (("upper", 4.02, (0.0, -0.20, -1.0)), ("lower", 2.98, (0.0, -0.18, 1.0))):
        for index in range(9):
            x = -0.86 + index * 0.215
            cone("ngu_tinh_%s_tooth_%02d" % (row, index), (x, -2.43, z), 0.09, 0.45, mats["bone"], collection, direction)

    # Dorsal fin and rebuilt tail fin: angular, biological, not ornamental cloud/dragon forms.
    dorsal = prism_from_2d(
        "ngu_tinh_dorsal_fin",
        [(0.20, 4.70), (0.76, 5.28), (1.38, 6.65), (1.92, 5.20), (2.55, 4.40)],
        0.16,
        mats["fish"],
        collection,
        axis="x",
    )
    dorsal.location.x = 0.0
    tail_fin = prism_from_2d(
        "ngu_tinh_fire_tail_fin",
        [(2.20, 3.65), (3.45, 5.05), (4.60, 6.00), (4.25, 3.70), (5.10, 2.06), (3.60, 2.55), (2.20, 3.10)],
        0.24,
        mats["tail_fire"],
        collection,
        axis="x",
    )
    # Prism points are (y,z) with local x thickness; place it on the tail axis.
    tail_fin.location.x = 0.0
    tail_fin.location.y = 0.0

    # Side fins fan forward and outward from the gills.
    for side in (-1.0, 1.0):
        fin = prism_from_2d(
            "ngu_tinh_pectoral_fin_%s" % ("l" if side < 0 else "r"),
            [(side * 1.10, -1.05), (side * 2.55, -0.65), (side * 3.65, -1.50), (side * 2.10, -1.95), (side * 1.12, -1.55)],
            0.12,
            mats["fish"],
            collection,
            axis="z",
        )
        fin.location.z = 3.55
        fin.rotation_euler.y = math.radians(-9.0 * side)

    # Gills, barbels, and a few hard dorsal spines provide the monster read.
    for side in (-1.0, 1.0):
        for index in range(3):
            y = -1.82 + index * 0.24
            gill = curve_tube(
                "ngu_tinh_gill_%s_%d" % ("l" if side < 0 else "r", index),
                [(side * 1.18, y, 4.02 - index * 0.13), (side * 1.38, y - 0.16, 3.72 - index * 0.13)],
                0.07,
                mats["gill"],
                collection,
            )
            gill.rotation_euler.y = math.radians(7.0 * side)
        for index in range(4):
            cone(
                "ngu_tinh_dorsal_spine_%d_%s" % (index, "l" if side < 0 else "r"),
                (side * (1.12 + index * 0.20), 0.05 + index * 0.34, 5.16),
                0.10,
                0.66 - index * 0.07,
                mats["scale"],
                collection,
                (0.12 * side, 0.04, 1.0),
            )

    for index, (start, end) in enumerate([
        ((-0.55, -2.65, 3.00), (-0.92, -3.20, 2.72)),
        ((0.55, -2.65, 3.00), (0.92, -3.20, 2.72)),
        ((-0.62, -2.56, 3.72), (-1.15, -3.10, 3.98)),
        ((0.62, -2.56, 3.72), (1.15, -3.10, 3.98)),
    ]):
        curve_tube("ngu_tinh_barbel_%d" % index, [start, end], 0.055, mats["gill"], collection)

    create_scales(collection, mats)
    return body


def curve_tube(name, points, radius, material, collection):
    curve_data = bpy.data.curves.new(name + "_curve", "CURVE")
    curve_data.dimensions = "3D"
    curve_data.resolution_u = 3
    curve_data.bevel_depth = radius
    curve_data.bevel_resolution = 3
    spline = curve_data.splines.new("BEZIER")
    spline.bezier_points.add(len(points) - 1)
    for bezier, point in zip(spline.bezier_points, points):
        bezier.co = point
        bezier.handle_left_type = "AUTO"
        bezier.handle_right_type = "AUTO"
    obj = bpy.data.objects.new(name, curve_data)
    collection.objects.link(obj)
    blockout.assign(obj, material)
    return obj


def create_rig(collection):
    armature_data = bpy.data.armatures.new("Ngu_Tinh_Combat_Rig_Data")
    rig = bpy.data.objects.new("Ngu_Tinh_Combat_Rig", armature_data)
    collection.objects.link(rig)
    bpy.context.view_layer.objects.active = rig
    rig.select_set(True)
    bpy.ops.object.mode_set(mode="EDIT")
    bones = [("root", (0.0, 0.0, 3.5), (0.0, 1.0, 3.5), None),
             ("spine_01", (0.0, 0.0, 3.5), (0.0, 1.2, 3.6), "root"),
             ("tail_01", (0.0, 1.2, 3.6), (0.0, 2.3, 3.7), "spine_01"),
             ("tail_02", (0.0, 2.3, 3.7), (0.0, 3.5, 3.9), "tail_01"),
             ("tail_03", (0.0, 3.5, 3.9), (0.0, 4.8, 4.2), "tail_02")]
    for name, head, tail, parent_name in bones:
        bone = armature_data.edit_bones.new(name)
        bone.head = head
        bone.tail = tail
        if parent_name:
            bone.parent = armature_data.edit_bones[parent_name]
    bpy.ops.object.mode_set(mode="OBJECT")
    rig.display_type = "WIRE"
    rig.show_in_front = True
    rig.hide_render = True
    return rig


def create_stage(collection, mats):
    blockout.cylinder("ngu_tinh_abyssal_altar", (0.0, 0.65, -0.42), 5.0, 0.62, mats["stage"], collection, 96)
    blockout.cylinder("ngu_tinh_water_surface", (0.0, 0.65, -0.08), 4.88, 0.04, mats["water"], collection, 96)
    for index, (x, y, z, scale) in enumerate([
        (-4.0, 1.5, 0.55, 1.15), (4.0, 2.0, 0.42, 0.92), (-3.7, -2.0, 0.30, 0.72),
        (3.45, -2.25, 0.28, 0.60), (0.0, 4.1, 0.45, 0.85),
    ]):
        rock = blockout.ico("ngu_tinh_basalt_%d" % index, (x, y, z), (scale * 0.65, scale * 0.46, scale), mats["stone"], collection, 2)
        rock.rotation_euler = (0.16 * index, -0.11 * index, 0.39 * index)

    # Broken altar ribs behind the boss, hinting at the drowned temple from CH-01.
    for index, x in enumerate((-3.4, 3.4)):
        rib = blockout.cube("drowned_temple_rib_%d" % index, (x, 2.9, 2.3), (0.18, 0.32, 2.2), mats["stone"], collection, rotation=(0.0, 0.20 * (-1 if index else 1), 0.08), bevel_width=0.10)
        rib.rotation_euler.z = 0.18 * (-1 if index else 1)


def create_lights(collection):
    def area(name, location, energy, color, size, target):
        data = bpy.data.lights.new(name, "AREA")
        data.energy = energy
        data.color = color
        data.shape = "DISK"
        data.size = size
        obj = bpy.data.objects.new(name, data)
        collection.objects.link(obj)
        obj.location = location
        blockout.look_at(obj, target)

    area("boss_key_underwater", (-6.5, -8.0, 8.5), 2300, (0.18, 0.52, 0.68), 6.0, (0.0, 0.0, 3.5))
    area("boss_fire_rim", (5.5, -2.0, 7.5), 2700, (1.0, 0.12, 0.025), 3.0, (0.0, 1.3, 3.7))
    area("boss_top_teal", (0.0, 5.5, 10.0), 3100, (0.02, 0.68, 0.70), 3.5, (0.0, 1.0, 4.0))
    area("boss_eye_fill", (0.0, -9.0, 4.0), 520, (1.0, 0.34, 0.10), 2.0, (0.0, -2.3, 3.7))


def setup_render(stage):
    scene = bpy.context.scene
    scene.render.engine = "BLENDER_EEVEE_NEXT"
    scene.render.resolution_x = 1200
    scene.render.resolution_y = 900
    scene.render.resolution_percentage = 100
    scene.render.image_settings.file_format = "PNG"
    scene.render.image_settings.color_mode = "RGBA"
    scene.render.filepath = str(OUT_DIR / "ngu_tinh_ch01_preview.png")
    scene.world.use_nodes = True
    background = scene.world.node_tree.nodes.get("Background")
    background.inputs["Color"].default_value = (0.001, 0.006, 0.011, 1.0)
    background.inputs["Strength"].default_value = 0.22
    camera_data = bpy.data.cameras.new("Ngu_Tinh_Hero_Camera")
    camera = bpy.data.objects.new("Ngu_Tinh_Hero_Camera", camera_data)
    stage.objects.link(camera)
    camera.location = (12.5, -15.5, 6.8)
    camera_data.lens = 56
    camera_data.sensor_width = 36
    blockout.look_at(camera, (0.0, 0.55, 3.65))
    scene.camera = camera
    hero.setup_compositor()


def build():
    blockout.clear_scene()
    boss_collection = blockout.make_collection("BOSS_NGU_TINH_CH01")
    rig_collection = blockout.make_collection("BOSS_NGU_TINH_RIG")
    stage_collection = blockout.make_collection("CH01_DROWNED_TEMPLE_STAGE")
    mats = make_materials()
    create_boss(boss_collection, mats)
    rig = create_rig(rig_collection)
    create_stage(stage_collection, mats)
    create_lights(stage_collection)
    setup_render(stage_collection)
    boss = bpy.data.objects.get("ngu_tinh_main_body")
    boss["boss_id"] = "CH01-NGU-TINH"
    boss["encounter"] = "Tram Thuy Ngu Tinh"
    boss["asset_status"] = "custom_assembled_boss_concept"
    boss["source_pipeline"] = "MPFB/MakeHuman material library plus custom biological assembly"
    boss["design_note"] = "Abyssal fish monster, rebuilt fire tail, Dong Son radial jade shard. No Chinese cloud or imperial motifs."
    boss["rig_source"] = rig.name
    bpy.context.scene["project"] = "Huyet Mach Lac Long"
    bpy.context.scene["chapter"] = "01 - Tram Thuy Ngu Tinh"
    bpy.context.scene["asset_scope"] = "Boss visual target, phase 1"
    bpy.context.scene["source_assets"] = "MPFB/MakeHuman System Assets CC0 material pipeline"
    rig_collection.hide_render = True
    bpy.ops.wm.save_as_mainfile(filepath=str(OUT_DIR / "ngu_tinh_ch01.blend"))
    bpy.ops.render.render(write_still=True)
    print("NGU_TINH_BUILD", boss.name, "RIG", rig.name, "OBJECTS", len(bpy.context.scene.objects))


if __name__ == "__main__":
    build()
