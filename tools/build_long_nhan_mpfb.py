import math
import sys
from pathlib import Path

import bpy
from mathutils import Matrix, Vector


TOOLS = Path(__file__).resolve().parent
ROOT = TOOLS.parent
OUT_DIR = ROOT / "assets" / "characters" / "long_nhan"
OUT_DIR.mkdir(parents=True, exist_ok=True)
sys.path.insert(0, str(TOOLS))
import build_long_nhan as blockout


def textured_material(name, dark, light, roughness, metallic=0.0, scale=7.0, bump=0.12):
    mat = bpy.data.materials.new(name)
    mat.use_nodes = True
    nodes = mat.node_tree.nodes
    links = mat.node_tree.links
    nodes.clear()

    output = nodes.new("ShaderNodeOutputMaterial")
    bsdf = nodes.new("ShaderNodeBsdfPrincipled")
    noise = nodes.new("ShaderNodeTexNoise")
    ramp = nodes.new("ShaderNodeValToRGB")
    bump_node = nodes.new("ShaderNodeBump")

    noise.inputs["Scale"].default_value = scale
    noise.inputs["Detail"].default_value = 4.0
    noise.inputs["Roughness"].default_value = 0.72
    ramp.color_ramp.elements[0].position = 0.24
    ramp.color_ramp.elements[0].color = (*dark, 1.0)
    ramp.color_ramp.elements[1].position = 0.78
    ramp.color_ramp.elements[1].color = (*light, 1.0)
    bsdf.inputs["Metallic"].default_value = metallic
    bsdf.inputs["Roughness"].default_value = roughness
    bump_node.inputs["Strength"].default_value = bump
    bump_node.inputs["Distance"].default_value = 0.07

    links.new(noise.outputs["Fac"], ramp.inputs["Fac"])
    links.new(ramp.outputs["Color"], bsdf.inputs["Base Color"])
    links.new(noise.outputs["Fac"], bump_node.inputs["Height"])
    links.new(bump_node.outputs["Normal"], bsdf.inputs["Normal"])
    links.new(bsdf.outputs["BSDF"], output.inputs["Surface"])
    return mat


def cloth_material(name, dark, light):
    mat = textured_material(name, dark, light, 0.76, scale=34.0, bump=0.17)
    nodes = mat.node_tree.nodes
    links = mat.node_tree.links
    bsdf = next(node for node in nodes if node.bl_idname == "ShaderNodeBsdfPrincipled")
    source = next(node for node in nodes if node.bl_idname == "ShaderNodeValToRGB")
    wave = nodes.new("ShaderNodeTexWave")
    mix = nodes.new("ShaderNodeMixRGB")
    wave.wave_type = "BANDS"
    wave.bands_direction = "X"
    wave.inputs["Scale"].default_value = 125.0
    wave.inputs["Distortion"].default_value = 3.0
    wave.inputs["Detail"].default_value = 2.0
    mix.blend_type = "MULTIPLY"
    mix.inputs[0].default_value = 0.18
    for link in list(bsdf.inputs["Base Color"].links):
        links.remove(link)
    links.new(source.outputs["Color"], mix.inputs[1])
    links.new(wave.outputs["Color"], mix.inputs[2])
    links.new(mix.outputs["Color"], bsdf.inputs["Base Color"])
    return mat


def make_materials():
    materials = {
        "indigo": cloth_material("viet_indigo_handwoven", (0.006, 0.025, 0.055), (0.025, 0.16, 0.24)),
        "teal": cloth_material("river_teal_handwoven", (0.005, 0.075, 0.075), (0.025, 0.29, 0.25)),
        "red": cloth_material("lac_red_handwoven", (0.12, 0.012, 0.006), (0.55, 0.075, 0.025)),
        "brown": textured_material("woven_brown_leather", (0.035, 0.012, 0.004), (0.24, 0.075, 0.018), 0.82, scale=19.0, bump=0.26),
        "bronze": textured_material("dong_son_bronze_patina", (0.045, 0.10, 0.075), (0.48, 0.19, 0.035), 0.31, metallic=0.78, scale=8.0, bump=0.22),
        "jade": textured_material("river_jade", (0.004, 0.055, 0.038), (0.015, 0.42, 0.25), 0.24, metallic=0.12, scale=5.0, bump=0.07),
        "stone": textured_material("thach_son_volcanic_stone", (0.012, 0.018, 0.023), (0.18, 0.23, 0.25), 0.55, metallic=0.08, scale=5.5, bump=0.38),
        "stage": textured_material("wet_black_stone", (0.003, 0.008, 0.012), (0.04, 0.075, 0.08), 0.30, metallic=0.22, scale=4.0, bump=0.22),
    }
    materials["edge"] = blockout.material(
        "axe_edge_ember",
        (0.24, 0.018, 0.004),
        metallic=0.32,
        roughness=0.24,
        emission=((0.95, 0.055, 0.004), 3.5),
    )
    materials["water"] = blockout.material(
        "deep_water",
        (0.002, 0.025, 0.035),
        metallic=0.24,
        roughness=0.10,
        emission=((0.0, 0.10, 0.12), 0.25),
    )
    return materials


def create_mpfb_human(body_collection):
    from bl_ext.user_default.mpfb.services import AssetService, HumanService, TargetService

    macro = TargetService.get_default_macro_info_dict()
    macro["race"]["asian"] = 1.0
    macro["race"]["african"] = 0.0
    macro["race"]["caucasian"] = 0.0
    macro["gender"] = 0.94
    macro["age"] = 0.37
    macro["muscle"] = 0.76
    macro["weight"] = 0.44
    macro["proportions"] = 0.58
    macro["height"] = 0.62

    human = HumanService.create_human(
        mask_helpers=True,
        detailed_helpers=True,
        extra_vertex_groups=True,
        feet_on_ground=True,
        scale=0.5,
        macro_detail_dict=macro,
    )
    human.name = "Long_Nhan_MPFB_Basemesh"
    blockout.move_to_collection(human, body_collection)

    skin = next((p for p in AssetService.list_mhmat_assets("skins") if p.name == "young_asian_male.mhmat"), None)
    if skin:
        HumanService.set_character_skin(str(skin), human, skin_type="GAMEENGINE", material_instances=True)
        warm_skin_materials(human)

    bpy.ops.object.select_all(action="DESELECT")
    human.select_set(True)
    bpy.context.view_layer.objects.active = human
    rig = HumanService.add_builtin_rig(human, "game_engine", import_weights=True)
    if rig:
        rig.name = "Long_Nhan_GameEngine_Rig"
        rig.show_in_front = True

    hair_path = next((p for p in AssetService.list_mhclo_assets("hair") if p.name == "ponytail01.mhclo"), None)
    hair = None
    if hair_path:
        hair = HumanService.add_mhclo_asset(
            str(hair_path),
            human,
            asset_type="Hair",
            subdiv_levels=1,
            material_type="MAKESKIN",
            set_up_rigging=True,
            interpolate_weights=True,
            import_subrig=True,
            import_weights=True,
        )
    return human, rig, hair


def warm_skin_materials(human):
    for slot in human.material_slots:
        mat = slot.material
        if not mat or not mat.use_nodes:
            continue
        nodes = mat.node_tree.nodes
        links = mat.node_tree.links
        bsdf = next((node for node in nodes if node.bl_idname == "ShaderNodeBsdfPrincipled"), None)
        image = next((node for node in nodes if node.bl_idname == "ShaderNodeTexImage" and node.image), None)
        if not bsdf or not image:
            continue
        for link in list(bsdf.inputs["Base Color"].links):
            links.remove(link)
        tint = nodes.new("ShaderNodeMixRGB")
        tint.name = "Long_Nhan_Warm_Skin_Tint"
        tint.blend_type = "MULTIPLY"
        tint.inputs[0].default_value = 0.80
        tint.inputs[1].default_value = (0.57, 0.30, 0.16, 1.0)
        links.new(image.outputs["Color"], tint.inputs[2])
        links.new(tint.outputs[0], bsdf.inputs["Base Color"])
        bsdf.inputs["Roughness"].default_value = 0.48


def extract_body_shell(human, rig, name, predicate, material, collection, offset=0.035, thickness=0.026):
    body_group = human.vertex_groups.get("body")
    if body_group is None:
        raise RuntimeError("MPFB body vertex group is missing")
    body_ids = {
        vertex.index
        for vertex in human.data.vertices
        if any(group.group == body_group.index and group.weight > 0.5 for group in vertex.groups)
    }

    selected_faces = []
    used_ids = set()
    for polygon in human.data.polygons:
        center = sum((human.data.vertices[index].co for index in polygon.vertices), Vector()) / len(polygon.vertices)
        if all(index in body_ids for index in polygon.vertices) and predicate(center):
            selected_faces.append(tuple(polygon.vertices))
            used_ids.update(polygon.vertices)

    ordered_ids = sorted(used_ids)
    remap = {old: new for new, old in enumerate(ordered_ids)}
    vertices = [
        human.data.vertices[index].co + human.data.vertices[index].normal * offset
        for index in ordered_ids
    ]
    faces = [tuple(remap[index] for index in face) for face in selected_faces]
    mesh = bpy.data.meshes.new(name + "_mesh")
    mesh.from_pydata(vertices, [], faces)
    mesh.update()
    obj = bpy.data.objects.new(name, mesh)
    collection.objects.link(obj)
    blockout.assign(obj, material)

    for source_group in human.vertex_groups:
        obj.vertex_groups.new(name=source_group.name)
    for old_index, new_index in remap.items():
        for assignment in human.data.vertices[old_index].groups:
            obj.vertex_groups[assignment.group].add([new_index], assignment.weight, "REPLACE")

    solidify = obj.modifiers.new("tailored_cloth_thickness", "SOLIDIFY")
    solidify.thickness = thickness
    solidify.offset = 0.35
    solidify.use_rim = True
    armature = obj.modifiers.new("GameEngine_Rig_Deform", "ARMATURE")
    armature.object = rig
    for polygon in mesh.polygons:
        polygon.use_smooth = True
    return obj


def add_rig_weight(obj, rig, group_name):
    group = obj.vertex_groups.new(name=group_name)
    group.add(list(range(len(obj.data.vertices))), 1.0, "REPLACE")
    modifier = obj.modifiers.new("GameEngine_Rig_Deform", "ARMATURE")
    modifier.object = rig
    return obj


def ellipse_band(name, z, radius_x, radius_y, height, material, collection, rig, segments=48):
    vertices = []
    for z_offset in (-height / 2.0, height / 2.0):
        for index in range(segments):
            angle = 2.0 * math.pi * index / segments
            vertices.append((math.cos(angle) * radius_x, math.sin(angle) * radius_y, z + z_offset))
    faces = []
    for index in range(segments):
        next_index = (index + 1) % segments
        faces.append((index, next_index, next_index + segments, index + segments))
    mesh = bpy.data.meshes.new(name + "_mesh")
    mesh.from_pydata(vertices, [], faces)
    mesh.update()
    obj = bpy.data.objects.new(name, mesh)
    collection.objects.link(obj)
    blockout.assign(obj, material)
    solidify = obj.modifiers.new("woven_band_depth", "SOLIDIFY")
    solidify.thickness = 0.055
    solidify.offset = 0.0
    blockout.bevel(obj, 0.025, 3)
    add_rig_weight(obj, rig, "pelvis")
    return obj


def curved_panel(name, side, material, collection, rig, long_panel=True):
    columns = 7
    rows = 9
    top_outer = side * 1.02
    top_inner = side * 0.08
    bottom_outer = side * (1.42 if long_panel else 1.22)
    bottom_inner = side * 0.10
    length = 2.52 if long_panel else 2.05
    vertices = []
    for row in range(rows):
        v = row / (rows - 1)
        for column in range(columns):
            u = column / (columns - 1)
            top_x = top_outer * (1.0 - u) + top_inner * u
            bottom_x = bottom_outer * (1.0 - u) + bottom_inner * u
            x = top_x * (1.0 - v) + bottom_x * v
            y = -0.62 + 0.11 * v - 0.045 * math.sin(math.pi * u)
            z = 4.18 - length * v - 0.10 * v * (1.0 - u)
            vertices.append((x, y, z))
    faces = []
    for row in range(rows - 1):
        for column in range(columns - 1):
            a = row * columns + column
            faces.append((a, a + 1, a + columns + 1, a + columns))
    mesh = bpy.data.meshes.new(name + "_mesh")
    mesh.from_pydata(vertices, [], faces)
    mesh.update()
    obj = bpy.data.objects.new(name, mesh)
    collection.objects.link(obj)
    blockout.assign(obj, material)
    solidify = obj.modifiers.new("cloth_edge", "SOLIDIFY")
    solidify.thickness = 0.035
    solidify.offset = 0.0
    bevel = obj.modifiers.new("soft_fold_edges", "BEVEL")
    bevel.width = 0.018
    bevel.segments = 2
    add_rig_weight(obj, rig, "pelvis")
    return obj


def bib_panel(material, collection, rig):
    # Smooth V-neck bib hides the raw topology boundary and establishes a clear giao linh wrap.
    columns = 7
    rows = 3
    vertices = []
    for row in range(rows):
        v = row / (rows - 1)
        width = 0.82 + v * 0.12
        z_base = 5.62 - v * 0.98
        for column in range(columns):
            u = column / (columns - 1)
            x = -width + 2.0 * width * u
            if row == 0:
                z = z_base + 0.30 * abs(2.0 * u - 1.0)
            else:
                z = z_base
            y = -0.73 - 0.025 * math.sin(math.pi * u)
            vertices.append((x, y, z))
    faces = []
    for row in range(rows - 1):
        for column in range(columns - 1):
            a = row * columns + column
            faces.append((a, a + 1, a + columns + 1, a + columns))
    mesh = bpy.data.meshes.new("giao_linh_bib_mesh")
    mesh.from_pydata(vertices, [], faces)
    mesh.update()
    obj = bpy.data.objects.new("ao_giao_linh_v_neck_bib", mesh)
    collection.objects.link(obj)
    blockout.assign(obj, material)
    solidify = obj.modifiers.new("bib_cloth_depth", "SOLIDIFY")
    solidify.thickness = 0.045
    solidify.offset = 0.0
    bevel = obj.modifiers.new("bib_soft_edge", "BEVEL")
    bevel.width = 0.022
    bevel.segments = 2
    add_rig_weight(obj, rig, "spine_03")
    return obj


def hero_chest_overlay(material, collection):
    # A clean front wrap is kept in the hero pose so the silhouette reads before animation polish.
    columns = 8
    rows = 5
    vertices = []
    for row in range(rows):
        v = row / (rows - 1)
        width = 0.86 + 0.10 * v
        z = 5.88 - 1.20 * v
        for column in range(columns):
            u = column / (columns - 1)
            x = -width + 2.0 * width * u
            y = -0.91 - 0.025 * math.sin(math.pi * u) + 0.03 * v
            vertices.append((x, y, z - 0.08 * v * (1.0 - u)))
    faces = []
    for row in range(rows - 1):
        for column in range(columns - 1):
            a = row * columns + column
            faces.append((a, a + 1, a + columns + 1, a + columns))
    mesh = bpy.data.meshes.new("hero_chest_wrap_mesh")
    mesh.from_pydata(vertices, [], faces)
    mesh.update()
    obj = bpy.data.objects.new("ao_giao_linh_hero_chest_wrap", mesh)
    collection.objects.link(obj)
    blockout.assign(obj, material)
    solidify = obj.modifiers.new("wrap_thickness", "SOLIDIFY")
    solidify.thickness = 0.045
    solidify.offset = 0.0
    bevel = obj.modifiers.new("wrap_soft_edges", "BEVEL")
    bevel.width = 0.025
    bevel.segments = 3
    for polygon in mesh.polygons:
        polygon.use_smooth = True
    return obj


def curve_tube(name, points, radius, material, collection):
    curve_data = bpy.data.curves.new(name + "_curve", "CURVE")
    curve_data.dimensions = "3D"
    curve_data.resolution_u = 2
    curve_data.bevel_depth = radius
    curve_data.bevel_resolution = 3
    spline = curve_data.splines.new("BEZIER")
    spline.bezier_points.add(len(points) - 1)
    for bezier_point, point in zip(spline.bezier_points, points):
        bezier_point.co = point
        bezier_point.handle_left_type = "AUTO"
        bezier_point.handle_right_type = "AUTO"
    obj = bpy.data.objects.new(name, curve_data)
    collection.objects.link(obj)
    blockout.assign(obj, material)
    return obj


def parent_to_bone(obj, rig, bone_name):
    world = obj.matrix_world.copy()
    obj.parent = rig
    obj.parent_type = "BONE"
    obj.parent_bone = bone_name
    obj.matrix_world = world


def star_prism(name, location, outer_radius, inner_radius, depth, material, collection, points=12):
    vertices = []
    count = points * 2
    for y in (-depth / 2.0, depth / 2.0):
        for index in range(count):
            angle = math.pi / 2.0 + math.pi * index / points
            radius = outer_radius if index % 2 == 0 else inner_radius
            vertices.append((location[0] + math.cos(angle) * radius, location[1] + y, location[2] + math.sin(angle) * radius))
    faces = [tuple(range(count)), tuple(range(count, count * 2))]
    for index in range(count):
        next_index = (index + 1) % count
        faces.append((index, next_index, next_index + count, index + count))
    mesh = bpy.data.meshes.new(name + "_mesh")
    mesh.from_pydata(vertices, [], faces)
    mesh.update()
    obj = bpy.data.objects.new(name, mesh)
    collection.objects.link(obj)
    blockout.assign(obj, material)
    blockout.bevel(obj, 0.012, 2)
    return obj


def create_costume(human, rig, collection, materials):
    extract_body_shell(
        human,
        rig,
        "ao_giao_linh_inner",
        lambda co: 4.08 < co.z < 6.02 and abs(co.x) < 1.34,
        materials["teal"],
        collection,
        offset=0.045,
        thickness=0.035,
    )
    extract_body_shell(
        human,
        rig,
        "ao_giao_linh_front_yoke",
        lambda co: 5.18 < co.z < 6.45 and abs(co.x) < 1.28 and co.y < -0.18,
        materials["indigo"],
        collection,
        offset=0.070,
        thickness=0.035,
    )
    extract_body_shell(
        human,
        rig,
        "combat_trousers",
        lambda co: 0.62 < co.z < 4.20 and abs(co.x) < 1.34,
        materials["indigo"],
        collection,
        offset=0.035,
        thickness=0.028,
    )
    extract_body_shell(
        human,
        rig,
        "short_sleeves",
        lambda co: 4.88 < co.z < 6.20 and 0.90 < abs(co.x) < 1.82,
        materials["indigo"],
        collection,
        offset=0.055,
        thickness=0.032,
    )
    extract_body_shell(
        human,
        rig,
        "woven_field_boots",
        lambda co: 0.015 < co.z < 1.22 and 0.42 < abs(co.x) < 1.48,
        materials["brown"],
        collection,
        offset=0.055,
        thickness=0.040,
    )

    ellipse_band("lac_red_war_sash", 4.18, 1.02, 0.60, 0.30, materials["red"], collection, rig)
    curved_panel("ao_tu_than_front_left", -1.0, materials["indigo"], collection, rig, long_panel=True)
    curved_panel("ao_tu_than_front_right", 1.0, materials["indigo"], collection, rig, long_panel=False)

    # Compact forearm guards follow the actual lower-arm bones; no disconnected armor shell.
    for side, bone_name, start, end in (
        ("l", "lowerarm_l", (1.72, -0.28, 5.10), (2.00, -0.68, 4.82)),
        ("r", "lowerarm_r", (-1.72, -0.28, 5.10), (-2.00, -0.68, 4.82)),
    ):
        guard = blockout.cylinder_between(
            "bronze_forearm_guard_" + side,
            start,
            end,
            0.155,
            materials["bronze"],
            collection,
            18,
        )
        parent_to_bone(guard, rig, bone_name)

    left_trim = curve_tube(
        "bronze_geometric_lapel_left",
        [(-0.82, -0.70, 5.82), (-0.42, -0.76, 5.20), (-0.04, -0.75, 4.55)],
        0.045,
        materials["bronze"],
        collection,
    )
    right_trim = curve_tube(
        "lac_red_lapel_right",
        [(0.70, -0.70, 5.78), (0.36, -0.77, 5.18), (-0.04, -0.78, 4.55)],
        0.050,
        materials["red"],
        collection,
    )
    parent_to_bone(left_trim, rig, "spine_03")
    parent_to_bone(right_trim, rig, "spine_03")

    medallion = star_prism(
        "dong_son_twelve_ray_medallion",
        (0.0, -0.80, 4.58),
        0.24,
        0.12,
        0.065,
        materials["bronze"],
        collection,
        points=12,
    )
    parent_to_bone(medallion, rig, "spine_02")

    buckle = blockout.torus(
        "river_jade_sash_buckle",
        (0.0, -0.67, 4.17),
        0.19,
        0.045,
        materials["bronze"],
        collection,
        scale=(1.0, 0.72, 1.0),
    )
    buckle_core = blockout.sphere(
        "river_jade_buckle_core",
        (0.0, -0.72, 4.17),
        (0.085, 0.04, 0.085),
        materials["jade"],
        collection,
        20,
        12,
    )
    parent_to_bone(buckle, rig, "pelvis")
    parent_to_bone(buckle_core, rig, "pelvis")

    headband = blockout.cube(
        "lac_woven_forehead_band",
        (0.0, -0.60, 7.64),
        (0.58, 0.055, 0.065),
        materials["red"],
        collection,
        bevel_width=0.035,
    )
    parent_to_bone(headband, rig, "head")
    headband_knot = blockout.sphere(
        "lac_headband_knot",
        (0.56, -0.56, 7.64),
        (0.10, 0.07, 0.10),
        materials["bronze"],
        collection,
        16,
        10,
    )
    parent_to_bone(headband_knot, rig, "head")

    for index, x in enumerate((-0.55, -0.30, 0.30, 0.55)):
        scale = blockout.sphere(
            "river_jade_scale_" + str(index),
            (x, -0.74, 5.42 - abs(x) * 0.18),
            (0.085, 0.028, 0.12),
            materials["jade"],
            collection,
            20,
            12,
        )
        parent_to_bone(scale, rig, "spine_03")

    sash_tail = curve_tube(
        "lac_sash_trailing_cord",
        [(-0.72, -0.25, 4.12), (-1.05, 0.18, 3.45), (-1.34, 0.25, 2.70), (-1.22, -0.12, 2.10)],
        0.075,
        materials["red"],
        collection,
    )
    parent_to_bone(sash_tail, rig, "pelvis")


def create_static_boot_toes(collection, materials):
    # The IK pose moves foot bones aggressively; keep hero footwear clean and readable.
    for side, x, y in (("l", 1.18, -0.10), ("r", -1.15, 0.42)):
        toe = blockout.cube(
            "woven_boot_toe_" + side,
            (x, y, 0.25),
            (0.48, 0.62, 0.25),
            materials["brown"],
            collection,
            rotation=(0.0, 0.0, 0.02 if side == "l" else -0.02),
            bevel_width=0.16,
        )


def create_hero_lapels(collection, materials):
    # Crossed fabric bands make the giao linh construction legible in the hero pose.
    curve_tube(
        "hero_red_cross_lapel",
        [(-0.82, -1.03, 5.90), (-0.40, -1.06, 5.56), (0.16, -1.07, 5.14), (0.74, -1.04, 4.72)],
        0.052,
        materials["red"],
        collection,
    )
    curve_tube(
        "hero_bronze_cross_lapel",
        [(0.78, -1.05, 5.88), (0.38, -1.08, 5.55), (-0.18, -1.09, 5.13), (-0.70, -1.06, 4.72)],
        0.037,
        materials["bronze"],
        collection,
    )


def create_ik_target(collection, name, location, display_type="SPHERE"):
    target = bpy.data.objects.new(name, None)
    collection.objects.link(target)
    target.location = location
    target.empty_display_type = display_type
    target.empty_display_size = 0.16
    target.hide_render = True
    return target


def pose_character(rig, controls):
    rig.data.pose_position = "POSE"
    pelvis = rig.pose.bones.get("pelvis")
    if pelvis:
        pelvis.rotation_mode = "XYZ"
        pelvis.location.z = -0.13
        pelvis.rotation_euler = (math.radians(2), math.radians(-5), math.radians(7))

    for name, rotation in {
        "spine_01": (2, -2, -4),
        "spine_02": (3, 3, -5),
        "spine_03": (-2, 5, -5),
        "neck_01": (1, -2, 4),
        "head": (-2, 1, 3),
    }.items():
        bone = rig.pose.bones.get(name)
        if bone:
            bone.rotation_mode = "XYZ"
            bone.rotation_euler = tuple(math.radians(value) for value in rotation)

    targets = {
        "lowerarm_l": ((0.53, -1.02, 5.30), (1.72, 0.28, 5.20)),
        "lowerarm_r": ((0.05, -1.04, 4.57), (-1.72, 0.20, 4.85)),
        "calf_l": ((1.02, -0.35, 0.27), (0.92, -1.95, 2.05)),
        "calf_r": ((-0.98, 0.24, 0.29), (-0.82, -1.82, 2.00)),
    }
    for bone_name, (target_location, pole_location) in targets.items():
        bone = rig.pose.bones.get(bone_name)
        if not bone:
            continue
        target = create_ik_target(controls, bone_name + "_IK", target_location)
        pole = create_ik_target(controls, bone_name + "_POLE", pole_location, "CUBE")
        constraint = bone.constraints.new("IK")
        constraint.name = "Long_Nhan_Combat_Pose"
        constraint.target = target
        constraint.pole_target = pole
        constraint.chain_count = 2
        constraint.use_tail = True
        if "calf" in bone_name:
            constraint.pole_angle = math.radians(90)

    for side in ("l", "r"):
        hand = rig.pose.bones.get("hand_" + side)
        if hand:
            hand.rotation_mode = "XYZ"
            hand.rotation_euler = (math.radians(12), math.radians(-8 if side == "l" else 8), math.radians(8))
        for finger in ("index", "middle", "ring", "pinky"):
            for joint in ("01", "02", "03"):
                bone = rig.pose.bones.get(f"{finger}_{joint}_{side}")
                if bone:
                    bone.rotation_mode = "XYZ"
                    bone.rotation_euler.x = math.radians(42 if joint == "01" else 55)
        for joint in ("01", "02", "03"):
            thumb = rig.pose.bones.get(f"thumb_{joint}_{side}")
            if thumb:
                thumb.rotation_mode = "XYZ"
                thumb.rotation_euler.x = math.radians(24)

    bpy.context.view_layer.update()


def create_weapon(rig, collection, materials):
    bottom = Vector((-0.62, -1.02, 3.62))
    top = Vector((2.02, -0.74, 7.62))
    direction = top - bottom
    length = direction.length

    root = bpy.data.objects.new("Riu_Than_Thach_Son_ROOT", None)
    collection.objects.link(root)
    root.location = bottom
    root.rotation_mode = "QUATERNION"
    root.rotation_quaternion = direction.to_track_quat("Z", "Y")

    parts = []
    parts.append(blockout.cylinder_between("riu_haft", (0.0, 0.0, 0.0), (0.0, 0.0, length - 0.18), 0.085, materials["brown"], collection, 18))
    socket = blockout.cylinder("bronze_axe_socket", (0.0, 0.0, length - 0.55), 0.16, 0.42, materials["bronze"], collection, 20)
    parts.append(socket)
    head = blockout.axe_head("thach_son_axe_head", (0.0, 0.0, length), materials["stone"], collection)
    head.scale = (1.38, 1.0, 1.16)
    parts.append(head)
    parts.append(blockout.cube("ember_edge_upper", (-0.67, -0.225, length + 0.28), (0.06, 0.028, 0.33), materials["edge"], collection, rotation=(0.0, 0.0, -0.36), bevel_width=0.025))
    parts.append(blockout.cube("ember_edge_lower", (-0.70, -0.225, length - 0.25), (0.055, 0.028, 0.26), materials["edge"], collection, rotation=(0.0, 0.0, 0.30), bevel_width=0.025))
    mark = star_prism("axe_dong_son_mark", (0.04, -0.235, length + 0.06), 0.15, 0.075, 0.025, materials["bronze"], collection, points=10)
    parts.append(mark)
    pommel = blockout.sphere("river_jade_pommel", (0.0, 0.0, 0.02), (0.15, 0.15, 0.19), materials["jade"], collection, 24, 14)
    parts.append(pommel)

    for part in parts:
        local_matrix = part.matrix_world.copy()
        part.parent = root
        part.matrix_parent_inverse = Matrix.Identity(4)
        part.matrix_basis = local_matrix

    world = root.matrix_world.copy()
    root.parent = rig
    root.parent_type = "BONE"
    root.parent_bone = "hand_l"
    root.matrix_world = world
    return root


def create_stage(stage, materials):
    blockout.cylinder("wet_stone_plinth", (0.0, 0.0, -0.27), 3.05, 0.45, materials["stage"], stage, 96)
    blockout.cylinder("shallow_black_water", (0.0, 0.0, -0.025), 2.88, 0.025, materials["water"], stage, 96)
    blockout.torus("water_ripple_outer", (0.0, 0.0, -0.005), 2.72, 0.025, materials["jade"], stage, scale=(1.0, 0.82, 1.0))
    blockout.torus("water_ripple_inner", (0.45, -0.20, 0.005), 1.75, 0.012, materials["water"], stage, scale=(1.0, 0.68, 1.0))
    for index, (x, y, z, scale) in enumerate([
        (-2.45, 0.62, 0.24, 0.75),
        (2.52, 0.72, 0.18, 0.58),
        (-2.15, -1.15, 0.17, 0.48),
        (2.18, -1.02, 0.13, 0.36),
    ]):
        rock = blockout.ico("basalt_fragment_" + str(index), (x, y, z), (scale * 0.42, scale * 0.30, scale), materials["stone"], stage, 2)
        rock.rotation_euler = (0.18 * index, -0.12 * index, 0.42 * index)


def setup_presentation(stage):
    scene = bpy.context.scene
    scene.render.engine = "BLENDER_EEVEE_NEXT"
    scene.render.resolution_x = 900
    scene.render.resolution_y = 1200
    scene.render.resolution_percentage = 100
    scene.render.image_settings.file_format = "PNG"
    scene.render.image_settings.color_mode = "RGBA"
    scene.render.filepath = str(OUT_DIR / "long_nhan_mpfb_v2_preview.png")
    scene.render.film_transparent = False
    scene.render.image_settings.color_depth = "8"
    scene.world.use_nodes = True
    background = scene.world.node_tree.nodes.get("Background")
    background.inputs["Color"].default_value = (0.0015, 0.004, 0.006, 1.0)
    background.inputs["Strength"].default_value = 0.16
    try:
        scene.view_settings.look = "AgX - Medium High Contrast"
    except Exception:
        pass

    def area_light(name, location, energy, color, size, target=(0.0, 0.0, 4.1)):
        data = bpy.data.lights.new(name, "AREA")
        data.energy = energy
        data.color = color
        data.shape = "DISK"
        data.size = size
        obj = bpy.data.objects.new(name, data)
        stage.objects.link(obj)
        obj.location = location
        blockout.look_at(obj, target)
        return obj

    area_light("key_cool", (4.8, -7.8, 10.2), 1450, (0.38, 0.68, 1.0), 4.0)
    area_light("fill_fire", (-5.5, -4.8, 5.6), 1120, (1.0, 0.20, 0.045), 3.2)
    area_light("rim_river", (2.2, 4.2, 9.0), 1780, (0.01, 0.65, 0.55), 3.0)
    area_light("face_softbox", (-0.8, -5.5, 8.6), 540, (1.0, 0.63, 0.40), 2.2, (0.0, -0.1, 7.0))
    area_light("ground_glow", (0.0, 0.0, 0.6), 410, (0.0, 0.42, 0.38), 3.0, (0.0, 0.0, 3.2))

    camera_data = bpy.data.cameras.new("Long_Nhan_Hero_Camera")
    camera = bpy.data.objects.new("Long_Nhan_Hero_Camera", camera_data)
    stage.objects.link(camera)
    camera.location = (8.8, -20.8, 7.2)
    camera_data.lens = 68
    camera_data.sensor_width = 36
    blockout.look_at(camera, (0.10, -0.05, 4.15))
    scene.camera = camera

    scene.use_nodes = True
    nodes = scene.node_tree.nodes
    links = scene.node_tree.links
    nodes.clear()
    render_layers = nodes.new("CompositorNodeRLayers")
    glare = nodes.new("CompositorNodeGlare")
    glare.glare_type = "FOG_GLOW"
    glare.quality = "HIGH"
    glare.threshold = 1.15
    glare.size = 6
    glare.mix = -0.88
    composite = nodes.new("CompositorNodeComposite")
    links.new(render_layers.outputs["Image"], glare.inputs["Image"])
    links.new(glare.outputs["Image"], composite.inputs["Image"])


def build():
    blockout.clear_scene()
    body = blockout.make_collection("LONG_NHAN_MPFB_BODY")
    costume = blockout.make_collection("LONG_NHAN_VIET_COSTUME")
    weapon = blockout.make_collection("RIU_THAN_THACH_SON")
    controls = blockout.make_collection("LONG_NHAN_RIG_CONTROLS")
    stage = blockout.make_collection("PRESENTATION_STAGE")

    human, rig, hair = create_mpfb_human(body)
    materials = make_materials()
    create_costume(human, rig, costume, materials)
    pose_character(rig, controls)
    create_static_boot_toes(costume, materials)
    create_weapon(rig, weapon, materials)
    create_stage(stage, materials)
    setup_presentation(stage)

    human["character_id"] = "PLAYER-LONG-NHAN"
    human["asset_status"] = "library_backed_v2_combat_character"
    human["design_note"] = "Vietnam-inspired ao giao linh and ao tu than silhouette, Dong Son radial geometry, woven Lac sash, river jade. No Chinese cloud, imperial, or hanfu motifs."
    human["library"] = "MPFB 2.0.17 / MakeHuman System Assets CC0"
    human["skin_source"] = "young_asian_male.mhmat"
    human["hair_source"] = hair.name if hair else "not_loaded"
    human["rig_source"] = rig.name if rig else "not_loaded"
    bpy.context.scene["project"] = "Huyet Mach Lac Long"
    bpy.context.scene["asset_scope"] = "Main character MPFB v2 combat concept"
    bpy.context.scene["library_status"] = "MPFB installed; MakeHuman System Assets CC0 loaded"
    bpy.context.scene["cultural_direction"] = "Vietnam-inspired; Chinese motifs excluded"

    controls.hide_render = True
    bpy.ops.wm.save_as_mainfile(filepath=str(OUT_DIR / "long_nhan_mpfb_v2.blend"))
    bpy.ops.render.render(write_still=True)
    print(
        "MPFB_V2_BUILD",
        human.name,
        "VERTS",
        len(human.data.vertices),
        "RIG",
        bool(rig),
        "HAIR",
        bool(hair),
        "OBJECTS",
        len(bpy.context.scene.objects),
    )


if __name__ == "__main__":
    build()
