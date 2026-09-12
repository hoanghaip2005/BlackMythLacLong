"""Long Nhan - main character build v3.

Rebuild of the MPFB concept. The v2 pass failed on four counts and each is
fixed here deliberately:

1. Anatomy. v2 set ``gender`` but left ``cupsize`` at its 0.5 default, so the
   base mesh kept a female chest under a male skin. Every macro slider is now
   set explicitly.

2. Garments. v2 carved clothing out of the body mesh with world-space Z slabs.
   That is what produced the bare shoulders, the stair-stepped hems and the
   floating flat panels. Here nothing is carved. Every garment is lofted: a
   polyline is run down the limb or the spine, rays are cast outward onto the
   body to measure the real cross-section at each ring, and a clean quad tube
   is built at that radius plus a tailoring clearance. The result follows the
   anatomy, has continuous hems and can be flared per-piece.

3. Pose and weapon. v2 placed the axe in world space and hoped the IK hands
   would meet it. Here the body is posed first and the axe is then fitted to
   the measured palm matrix, so the grip is correct by construction.

4. Light. v2 lit almost entirely with teal and cyan rims and the skin died.
   Here a warm key carries the read and the cool light is demoted to rim.

Run:
    blender -b -P tools/build_long_nhan_v3.py
"""

import math
import sys
from pathlib import Path

import bpy
from mathutils import Matrix, Vector
from mathutils.bvhtree import BVHTree

TOOLS = Path(__file__).resolve().parent
ROOT = TOOLS.parent
OUT_DIR = ROOT / "assets" / "characters" / "long_nhan"
OUT_DIR.mkdir(parents=True, exist_ok=True)
sys.path.insert(0, str(TOOLS))
import build_long_nhan as blockout


# ---------------------------------------------------------------------------
# materials
# ---------------------------------------------------------------------------


def _principled(name):
    mat = bpy.data.materials.new(name)
    mat.use_nodes = True
    tree = mat.node_tree
    tree.nodes.clear()
    out = tree.nodes.new("ShaderNodeOutputMaterial")
    bsdf = tree.nodes.new("ShaderNodeBsdfPrincipled")
    tree.links.new(bsdf.outputs["BSDF"], out.inputs["Surface"])
    return mat, tree, bsdf


def fabric_material(name, dark, light, weave=300.0, roughness=0.84, variation=0.30):
    """Hand-woven cloth: a fine warp/weft weave plus slight dye unevenness.

    Kept low-contrast on purpose. v2 used a big blotchy noise that read as
    watercolour rather than as woven hemp or indigo.
    """
    mat, tree, bsdf = _principled(name)
    nodes, links = tree.nodes, tree.links

    coord = nodes.new("ShaderNodeTexCoord")
    warp = nodes.new("ShaderNodeTexWave")
    warp.wave_type = "BANDS"
    warp.bands_direction = "X"
    warp.inputs["Scale"].default_value = weave
    warp.inputs["Distortion"].default_value = 2.0
    warp.inputs["Detail"].default_value = 1.0
    weft = nodes.new("ShaderNodeTexWave")
    weft.wave_type = "BANDS"
    weft.bands_direction = "Z"
    weft.inputs["Scale"].default_value = weave
    weft.inputs["Distortion"].default_value = 2.0
    weft.inputs["Detail"].default_value = 1.0
    thread = nodes.new("ShaderNodeMixRGB")
    thread.blend_type = "MULTIPLY"
    thread.inputs[0].default_value = 0.75

    dye = nodes.new("ShaderNodeTexNoise")
    dye.inputs["Scale"].default_value = 26.0
    dye.inputs["Detail"].default_value = 4.0
    dye.inputs["Roughness"].default_value = 0.55
    blend = nodes.new("ShaderNodeMixRGB")
    blend.inputs[0].default_value = variation
    ramp = nodes.new("ShaderNodeValToRGB")
    ramp.color_ramp.elements[0].position = 0.30
    ramp.color_ramp.elements[0].color = (*dark, 1.0)
    ramp.color_ramp.elements[1].position = 0.72
    ramp.color_ramp.elements[1].color = (*light, 1.0)

    bump = nodes.new("ShaderNodeBump")
    bump.inputs["Strength"].default_value = 0.28
    bump.inputs["Distance"].default_value = 0.012

    links.new(coord.outputs["Object"], warp.inputs["Vector"])
    links.new(coord.outputs["Object"], weft.inputs["Vector"])
    links.new(coord.outputs["Object"], dye.inputs["Vector"])
    links.new(warp.outputs["Color"], thread.inputs[1])
    links.new(weft.outputs["Color"], thread.inputs[2])
    links.new(thread.outputs["Color"], blend.inputs[1])
    links.new(dye.outputs["Fac"], blend.inputs[2])
    links.new(blend.outputs["Color"], ramp.inputs["Fac"])
    links.new(ramp.outputs["Color"], bsdf.inputs["Base Color"])
    links.new(thread.outputs["Color"], bump.inputs["Height"])
    links.new(bump.outputs["Normal"], bsdf.inputs["Normal"])

    bsdf.inputs["Roughness"].default_value = roughness
    if "Sheen Weight" in bsdf.inputs:
        bsdf.inputs["Sheen Weight"].default_value = 0.30
        bsdf.inputs["Sheen Roughness"].default_value = 0.50
    return mat


def leather_material(name, dark, light, roughness=0.58):
    mat, tree, bsdf = _principled(name)
    nodes, links = tree.nodes, tree.links
    coord = nodes.new("ShaderNodeTexCoord")
    grain = nodes.new("ShaderNodeTexVoronoi")
    grain.feature = "DISTANCE_TO_EDGE"
    grain.inputs["Scale"].default_value = 140.0
    wear = nodes.new("ShaderNodeTexNoise")
    wear.inputs["Scale"].default_value = 14.0
    wear.inputs["Detail"].default_value = 6.0
    ramp = nodes.new("ShaderNodeValToRGB")
    ramp.color_ramp.elements[0].position = 0.36
    ramp.color_ramp.elements[0].color = (*dark, 1.0)
    ramp.color_ramp.elements[1].position = 0.68
    ramp.color_ramp.elements[1].color = (*light, 1.0)
    bump = nodes.new("ShaderNodeBump")
    bump.inputs["Strength"].default_value = 0.40
    bump.inputs["Distance"].default_value = 0.010
    rough = nodes.new("ShaderNodeMapRange")
    rough.inputs["To Min"].default_value = max(0.0, roughness - 0.16)
    rough.inputs["To Max"].default_value = min(1.0, roughness + 0.16)

    links.new(coord.outputs["Object"], grain.inputs["Vector"])
    links.new(coord.outputs["Object"], wear.inputs["Vector"])
    links.new(wear.outputs["Fac"], ramp.inputs["Fac"])
    links.new(ramp.outputs["Color"], bsdf.inputs["Base Color"])
    links.new(grain.outputs["Distance"], bump.inputs["Height"])
    links.new(bump.outputs["Normal"], bsdf.inputs["Normal"])
    links.new(wear.outputs["Fac"], rough.inputs["Value"])
    links.new(rough.outputs["Result"], bsdf.inputs["Roughness"])
    return mat


def bronze_material(name):
    """Dong Son bronze. Mostly warm metal, patina only in the deep recesses.

    v2 ran the patina at 50 percent and the armour read as mould.
    """
    mat, tree, bsdf = _principled(name)
    nodes, links = tree.nodes, tree.links
    coord = nodes.new("ShaderNodeTexCoord")
    noise = nodes.new("ShaderNodeTexNoise")
    noise.inputs["Scale"].default_value = 22.0
    noise.inputs["Detail"].default_value = 7.0
    ramp = nodes.new("ShaderNodeValToRGB")
    ramp.color_ramp.elements[0].position = 0.24
    ramp.color_ramp.elements[0].color = (0.055, 0.105, 0.080, 1.0)
    ramp.color_ramp.elements[1].position = 0.46
    ramp.color_ramp.elements[1].color = (0.62, 0.38, 0.135, 1.0)
    metallic = nodes.new("ShaderNodeMapRange")
    metallic.inputs["From Min"].default_value = 0.24
    metallic.inputs["From Max"].default_value = 0.46
    metallic.inputs["To Min"].default_value = 0.35
    metallic.inputs["To Max"].default_value = 1.0
    rough = nodes.new("ShaderNodeMapRange")
    rough.inputs["From Min"].default_value = 0.24
    rough.inputs["From Max"].default_value = 0.46
    rough.inputs["To Min"].default_value = 0.68
    rough.inputs["To Max"].default_value = 0.24
    bump = nodes.new("ShaderNodeBump")
    bump.inputs["Strength"].default_value = 0.16
    bump.inputs["Distance"].default_value = 0.010

    links.new(coord.outputs["Object"], noise.inputs["Vector"])
    links.new(noise.outputs["Fac"], ramp.inputs["Fac"])
    links.new(noise.outputs["Fac"], metallic.inputs["Value"])
    links.new(noise.outputs["Fac"], rough.inputs["Value"])
    links.new(noise.outputs["Fac"], bump.inputs["Height"])
    links.new(ramp.outputs["Color"], bsdf.inputs["Base Color"])
    links.new(metallic.outputs["Result"], bsdf.inputs["Metallic"])
    links.new(rough.outputs["Result"], bsdf.inputs["Roughness"])
    links.new(bump.outputs["Normal"], bsdf.inputs["Normal"])
    return mat


def jade_material(name):
    mat, tree, bsdf = _principled(name)
    nodes, links = tree.nodes, tree.links
    coord = nodes.new("ShaderNodeTexCoord")
    vein = nodes.new("ShaderNodeTexNoise")
    vein.inputs["Scale"].default_value = 9.0
    vein.inputs["Detail"].default_value = 8.0
    vein.inputs["Roughness"].default_value = 0.72
    ramp = nodes.new("ShaderNodeValToRGB")
    ramp.color_ramp.elements[0].position = 0.34
    ramp.color_ramp.elements[0].color = (0.006, 0.090, 0.066, 1.0)
    ramp.color_ramp.elements[1].position = 0.68
    ramp.color_ramp.elements[1].color = (0.075, 0.44, 0.30, 1.0)
    links.new(coord.outputs["Object"], vein.inputs["Vector"])
    links.new(vein.outputs["Fac"], ramp.inputs["Fac"])
    links.new(ramp.outputs["Color"], bsdf.inputs["Base Color"])
    bsdf.inputs["Roughness"].default_value = 0.14
    bsdf.inputs["IOR"].default_value = 1.62
    if "Subsurface Weight" in bsdf.inputs:
        bsdf.inputs["Subsurface Weight"].default_value = 0.45
        bsdf.inputs["Subsurface Radius"].default_value = (0.10, 0.35, 0.25)
    if "Emission Color" in bsdf.inputs:
        bsdf.inputs["Emission Color"].default_value = (0.02, 0.38, 0.26, 1.0)
        bsdf.inputs["Emission Strength"].default_value = 0.55
    return mat


def stone_material(name, dark=(0.010, 0.011, 0.014), light=(0.068, 0.072, 0.082)):
    mat, tree, bsdf = _principled(name)
    nodes, links = tree.nodes, tree.links
    coord = nodes.new("ShaderNodeTexCoord")
    rock = nodes.new("ShaderNodeTexVoronoi")
    rock.feature = "F1"
    rock.inputs["Scale"].default_value = 9.0
    grit = nodes.new("ShaderNodeTexNoise")
    grit.inputs["Scale"].default_value = 34.0
    grit.inputs["Detail"].default_value = 8.0
    mix = nodes.new("ShaderNodeMixRGB")
    mix.blend_type = "OVERLAY"
    mix.inputs[0].default_value = 0.40
    ramp = nodes.new("ShaderNodeValToRGB")
    ramp.color_ramp.elements[0].position = 0.20
    ramp.color_ramp.elements[0].color = (*dark, 1.0)
    ramp.color_ramp.elements[1].position = 0.80
    ramp.color_ramp.elements[1].color = (*light, 1.0)
    bump = nodes.new("ShaderNodeBump")
    bump.inputs["Strength"].default_value = 0.55
    bump.inputs["Distance"].default_value = 0.03
    links.new(coord.outputs["Object"], rock.inputs["Vector"])
    links.new(coord.outputs["Object"], grit.inputs["Vector"])
    links.new(rock.outputs["Distance"], mix.inputs[1])
    links.new(grit.outputs["Fac"], mix.inputs[2])
    links.new(mix.outputs["Color"], ramp.inputs["Fac"])
    links.new(ramp.outputs["Color"], bsdf.inputs["Base Color"])
    links.new(mix.outputs["Color"], bump.inputs["Height"])
    links.new(bump.outputs["Normal"], bsdf.inputs["Normal"])
    bsdf.inputs["Roughness"].default_value = 0.80
    return mat


def hair_material(name):
    mat, tree, bsdf = _principled(name)
    bsdf.inputs["Base Color"].default_value = (0.021, 0.016, 0.014, 1.0)
    bsdf.inputs["Roughness"].default_value = 0.58
    if "Specular IOR Level" in bsdf.inputs:
        bsdf.inputs["Specular IOR Level"].default_value = 0.32
    if "Anisotropic" in bsdf.inputs:
        bsdf.inputs["Anisotropic"].default_value = 0.25
    return mat


def make_materials():
    mats = {
        "indigo": fabric_material("cham_indigo", (0.008, 0.013, 0.030), (0.030, 0.052, 0.105)),
        "indigo_dark": fabric_material("cham_indigo_dam", (0.004, 0.006, 0.015), (0.016, 0.026, 0.055)),
        "hemp": fabric_material("vai_gai_moc", (0.085, 0.070, 0.050), (0.285, 0.240, 0.180), weave=340.0),
        "red": fabric_material("do_lac", (0.130, 0.018, 0.010), (0.52, 0.085, 0.034), weave=240.0),
        "teal": fabric_material("xanh_song", (0.006, 0.042, 0.046), (0.040, 0.175, 0.165)),
        "leather": leather_material("da_trau", (0.030, 0.017, 0.009), (0.165, 0.090, 0.042)),
        "dark_leather": leather_material("da_hun_khoi", (0.016, 0.010, 0.007), (0.072, 0.044, 0.026), roughness=0.68),
        "bronze": bronze_material("dong_dong_son"),
        "jade": jade_material("long_ngoc"),
        "stone": stone_material("da_thach_son"),
        "hair": hair_material("toc_den"),
    }
    mats["stage"] = stone_material("da_uot_be", (0.003, 0.0035, 0.005), (0.013, 0.015, 0.018))
    mats["ember"] = blockout.material(
        "than_khi_riu",
        (0.32, 0.050, 0.012),
        metallic=0.20,
        roughness=0.32,
        emission=((1.0, 0.18, 0.02), 6.0),
    )
    return mats


# ---------------------------------------------------------------------------
# base mesh
# ---------------------------------------------------------------------------


def create_human(body_collection):
    from bl_ext.user_default.mpfb.services import AssetService, HumanService, TargetService

    macro = TargetService.get_default_macro_info_dict()
    macro["race"] = {"asian": 1.0, "caucasian": 0.0, "african": 0.0}
    # Every slider is set. Leaving cupsize at its 0.5 default is exactly what
    # gave the v2 build a female chest under a male skin.
    macro["gender"] = 1.0
    macro["cupsize"] = 0.0
    macro["firmness"] = 0.5
    macro["age"] = 0.55
    macro["muscle"] = 0.88
    macro["weight"] = 0.46
    macro["proportions"] = 0.62
    macro["height"] = 0.74

    human = HumanService.create_human(
        mask_helpers=True,
        detailed_helpers=True,
        extra_vertex_groups=True,
        feet_on_ground=True,
        scale=0.5,
        macro_detail_dict=macro,
    )
    human.name = "Long_Nhan_Body"
    blockout.move_to_collection(human, body_collection)

    skin = next((p for p in AssetService.list_mhmat_assets("skins") if p.name == "young_asian_male.mhmat"), None)
    if skin:
        HumanService.set_character_skin(str(skin), human, skin_type="GAMEENGINE", material_instances=True)
        grade_skin(human)

    apply_detail_targets(human)

    bpy.ops.object.select_all(action="DESELECT")
    human.select_set(True)
    bpy.context.view_layer.objects.active = human
    rig = HumanService.add_builtin_rig(human, "game_engine", import_weights=True)
    rig.name = "Long_Nhan_Rig"
    rig.show_in_front = True

    attachments = {}
    for label, category, filename, asset_type in (
        # A tied-up bun reads as a Dong Son warrior's bui toc far better than
        # the system ponytail, which barely covered the scalp.
        ("hair", "hair", "sonntag78_junglebook_hair.mhclo", "Hair"),
        ("trousers", "clothes", "toigo_harem_pants.mhclo", "Clothes"),
        ("boots", "clothes", "culturalibre_male_boots.mhclo", "Clothes"),
        ("eyes", "eyes", "low-poly.mhclo", "Eyes"),
        ("eyebrows", "eyebrows", "eyebrow010.mhclo", "Eyebrows"),
        ("eyelashes", "eyelashes", "eyelashes01.mhclo", "Eyelashes"),
        ("teeth", "teeth", "teeth_base.mhclo", "Teeth"),
    ):
        path = next((p for p in AssetService.list_mhclo_assets(category) if p.name == filename), None)
        if not path:
            continue
        obj = HumanService.add_mhclo_asset(
            str(path),
            human,
            asset_type=asset_type,
            subdiv_levels=1,
            material_type="MAKESKIN",
            set_up_rigging=True,
            interpolate_weights=True,
            import_weights=True,
        )
        if obj:
            attachments[label] = obj
            blockout.move_to_collection(obj, body_collection)

    HumanService.refit(human)
    print("LIBRARY loaded:", ", ".join(sorted(attachments)))
    return human, rig, attachments


# Heavy brow, wide cheekbones, square jaw, thick neck, V-torso, worked arms
# and legs. Values are deliberately moderate: pushed hard these targets read as
# caricature rather than as a man who swings an axe for a living.
DETAIL_TARGETS = {
    "head/head-square": 0.42,
    "head/head-scale-depth-incr": 0.16,
    "head/head-scale-vert-decr": 0.06,
    "forehead/forehead-nubian-decr": 0.45,
    "forehead/forehead-trans-backward": 0.22,
    "forehead/forehead-temple-incr": 0.30,
    "eyebrows/eyebrows-trans-down": 0.52,
    "eyebrows/eyebrows-angle-down": 0.30,
    "eyes/l-eye-eyefold-down": 0.38,
    "eyes/r-eye-eyefold-down": 0.38,
    "eyes/l-eye-height1-decr": 0.24,
    "eyes/r-eye-height1-decr": 0.24,
    "cheek/l-cheek-bones-incr": 0.68,
    "cheek/r-cheek-bones-incr": 0.68,
    "cheek/l-cheek-inner-decr": 0.48,
    "cheek/r-cheek-inner-decr": 0.48,
    "chin/chin-bones-incr": 0.72,
    "chin/chin-width-incr": 0.44,
    "chin/chin-prominent-incr": 0.34,
    "chin/chin-height-incr": 0.20,
    "nose/nose-scale-horiz-incr": 0.28,
    "nose/nose-hump-incr": 0.22,
    "nose/nose-width2-incr": 0.20,
    "mouth/mouth-scale-horiz-incr": 0.26,
    "mouth/mouth-upperlip-volume-decr": 0.34,
    "mouth/mouth-lowerlip-volume-decr": 0.28,
    "mouth/mouth-angles-down": 0.18,
    "neck/measure-neck-circ-incr": 0.55,
    "torso/measure-shoulder-dist-incr": 0.58,
    "torso/torso-vshape-incr": 0.60,
    "torso/measure-waist-circ-decr": 0.42,
    "torso/torso-muscle-dorsi-incr": 0.42,
    "torso/torso-muscle-pectoral-incr": 0.34,
    "stomach/stomach-tone-incr": 0.50,
    "arms/l-upperarm-muscle-incr": 0.50,
    "arms/r-upperarm-muscle-incr": 0.50,
    "arms/l-upperarm-shoulder-muscle-incr": 0.48,
    "arms/r-upperarm-shoulder-muscle-incr": 0.48,
    "arms/l-lowerarm-muscle-incr": 0.42,
    "arms/r-lowerarm-muscle-incr": 0.42,
    "hands/l-hand-scale-incr": 0.20,
    "hands/r-hand-scale-incr": 0.20,
    "legs/l-upperleg-muscle-incr": 0.36,
    "legs/r-upperleg-muscle-incr": 0.36,
    "legs/l-lowerleg-muscle-incr": 0.40,
    "legs/r-lowerleg-muscle-incr": 0.40,
}


def apply_detail_targets(human):
    from bl_ext.user_default.mpfb.services import TargetService

    applied = 0
    for name, weight in DETAIL_TARGETS.items():
        path = TargetService.target_full_path(name.rsplit("/", 1)[-1])
        if not path:
            print("TARGET missing:", name)
            continue
        try:
            TargetService.load_target(human, path, weight=weight, name=name.rsplit("/", 1)[-1])
            applied += 1
        except Exception as error:  # a missing target must not abort the build
            print("TARGET failed:", name, error)
    print("TARGETS applied %d/%d" % (applied, len(DETAIL_TARGETS)))
    return applied


def grade_skin(human):
    """Warm and darken the MakeHuman diffuse, add subsurface.

    The stock GAMEENGINE skin is a light-skinned scan and renders as chalk
    under a strong key, which is how the v3 first pass came out white.
    """
    for slot in human.material_slots:
        mat = slot.material
        if not mat or not mat.use_nodes:
            continue
        nodes, links = mat.node_tree.nodes, mat.node_tree.links
        bsdf = next((n for n in nodes if n.bl_idname == "ShaderNodeBsdfPrincipled"), None)
        image = next((n for n in nodes if n.bl_idname == "ShaderNodeTexImage" and n.image), None)
        if not bsdf or not image:
            continue
        for link in list(bsdf.inputs["Base Color"].links):
            links.remove(link)
        tint = nodes.new("ShaderNodeMixRGB")
        tint.blend_type = "MULTIPLY"
        tint.inputs[0].default_value = 1.0
        tint.inputs[1].default_value = (0.62, 0.395, 0.255, 1.0)
        links.new(image.outputs["Color"], tint.inputs[2])
        links.new(tint.outputs[0], bsdf.inputs["Base Color"])
        bsdf.inputs["Roughness"].default_value = 0.56
        if "Specular IOR Level" in bsdf.inputs:
            bsdf.inputs["Specular IOR Level"].default_value = 0.32
        if "Subsurface Weight" in bsdf.inputs:
            bsdf.inputs["Subsurface Weight"].default_value = 0.12
            bsdf.inputs["Subsurface Radius"].default_value = (0.36, 0.14, 0.09)
            if "Subsurface Scale" in bsdf.inputs:
                bsdf.inputs["Subsurface Scale"].default_value = 0.10


# ---------------------------------------------------------------------------
# anatomy read from the MakeHuman joint cubes
# ---------------------------------------------------------------------------


def shaped_coords(human):
    """Vertex positions with all MPFB shape keys resolved.

    ``mesh.vertices[i].co`` is the unshaped base mesh: every macro slider and
    every detail target is a shape key on top of it.
    """
    mesh = human.data
    count = len(mesh.vertices)
    flat = [0.0] * (count * 3)
    keys = mesh.shape_keys
    if not keys:
        mesh.vertices.foreach_get("co", flat)
    else:
        blocks = keys.key_blocks
        blocks[0].data.foreach_get("co", flat)
        scratch = [0.0] * (count * 3)
        reference = [0.0] * (count * 3)
        for block in blocks[1:]:
            value = block.value
            if abs(value) < 1e-6:
                continue
            block.data.foreach_get("co", scratch)
            (block.relative_key or blocks[0]).data.foreach_get("co", reference)
            for index in range(count * 3):
                flat[index] += (scratch[index] - reference[index]) * value
    return [Vector(flat[i * 3:i * 3 + 3]) for i in range(count)]


def joint_positions(human, coords):
    buckets = {}
    for vertex in human.data.vertices:
        for assignment in vertex.groups:
            buckets.setdefault(assignment.group, []).append(coords[vertex.index])
    result = {}
    for group in human.vertex_groups:
        if not group.name.startswith("joint-"):
            continue
        points = buckets.get(group.index)
        if points:
            result[group.name[6:]] = sum(points, Vector()) / len(points)
    return result


def toe_tip(joints, side):
    tips = [v for k, v in joints.items() if k.startswith(f"{side}-toe-") and k.endswith("-3")]
    if tips:
        return sum(tips, Vector()) / len(tips)
    ankle = joints[f"{side}-ankle"]
    ball = joints[f"{side}-foot-1"]
    return ball + (ball - ankle) * 0.8


# ---------------------------------------------------------------------------
# garment lofting
#
# Nothing is carved out of the body. Every piece is a clean quad tube: a
# polyline is run down the limb or the spine, rays measure the real body
# cross-section at each ring, the profile is smoothed, and the surface is
# rebuilt at that radius plus a tailoring gap.
# ---------------------------------------------------------------------------


def point_to_polyline(point, polyline):
    best = None
    for start, end in zip(polyline, polyline[1:]):
        span = end - start
        length_sq = span.length_squared
        t = 0.0 if length_sq == 0.0 else max(0.0, min(1.0, (point - start).dot(span) / length_sq))
        distance = (point - (start + span * t)).length
        if best is None or distance < best:
            best = distance
    return best


def build_ray_targets(human, coords, joints):
    """Two BVH trees: the whole body, and the body without the arms.

    Torso garments measure against the second one. In the A-pose a chest-height
    ray reaches the upper arm first, so measuring the trunk against the full
    body reports the arm's position and inflates every torso piece.
    """
    body_group = human.vertex_groups.get("body")
    body_ids = {
        vertex.index
        for vertex in human.data.vertices
        if any(g.group == body_group.index and g.weight > 0.5 for g in vertex.groups)
    }

    spine = [joints["pelvis"] + Vector((0.0, 0.0, -1.4)), joints["neck"], joints["head"]]
    arms = []
    for side in ("l", "r"):
        shoulder = joints[side + "-shoulder"]
        elbow = joints[side + "-elbow"]
        hand = joints[side + "-hand"]
        arms.append([shoulder, elbow, hand, hand + (hand - elbow).normalized() * 1.3])

    trunk_ids = set()
    for index in body_ids:
        point = coords[index]
        to_arm = min(point_to_polyline(point, arm) for arm in arms)
        if to_arm > point_to_polyline(point, spine) * 0.95:
            trunk_ids.add(index)

    def tree(allowed):
        verts, faces, remap = [], [], {}
        for polygon in human.data.polygons:
            if not all(i in allowed for i in polygon.vertices):
                continue
            face = []
            for i in polygon.vertices:
                if i not in remap:
                    remap[i] = len(verts)
                    verts.append(coords[i])
                face.append(remap[i])
            faces.append(tuple(face))
        return BVHTree.FromPolygons(verts, faces)

    return tree(body_ids), tree(trunk_ids)


def frame_for(points, index):
    count = len(points)
    if index == 0:
        tangent = points[1] - points[0]
    elif index == count - 1:
        tangent = points[-1] - points[-2]
    else:
        tangent = points[index + 1] - points[index - 1]
    tangent.normalize()
    reference = Vector((0.0, 0.0, 1.0))
    if abs(tangent.dot(reference)) > 0.9:
        reference = Vector((0.0, 1.0, 0.0))
    u = tangent.cross(reference).normalized()
    v = tangent.cross(u).normalized()
    return u, v


def ray_radius(bvh, center, direction, reach):
    """Distance from ``center`` out to the body surface, or None if missed."""
    location, _, _, _ = bvh.ray_cast(center + direction * reach, -direction, reach * 2.0)
    if location is None:
        return None
    radius = (location - center).dot(direction)
    return radius if radius > 0.02 else None


def fill_gaps(row, default):
    """Replace missed rays by interpolating around the ring."""
    count = len(row)
    if all(value is None for value in row):
        return [default] * count
    filled = list(row)
    for index in range(count):
        if filled[index] is not None:
            continue
        back = forward = None
        for step in range(1, count):
            if back is None and row[(index - step) % count] is not None:
                back = row[(index - step) % count]
            if forward is None and row[(index + step) % count] is not None:
                forward = row[(index + step) % count]
            if back is not None and forward is not None:
                break
        filled[index] = (back + forward) / 2.0
    return filled


def smooth_profile(profile, ring_passes=3, axis_passes=1):
    """1-2-1 smoothing around each ring and along the axis.

    Raw ray measurements are noisy wherever a ray grazes an ear, a finger or
    the opposite limb. Left unsmoothed, that noise is exactly the jagged hem
    the earlier passes produced.
    """
    rows = [list(row) for row in profile]
    segments = len(rows[0])
    for _ in range(ring_passes):
        for row in rows:
            source = list(row)
            for index in range(segments):
                row[index] = (
                    source[(index - 1) % segments] + 2.0 * source[index] + source[(index + 1) % segments]
                ) / 4.0
    for _ in range(axis_passes):
        source = [list(row) for row in rows]
        for index in range(1, len(rows) - 1):
            for column in range(segments):
                rows[index][column] = (
                    source[index - 1][column] + 2.0 * source[index][column] + source[index + 1][column]
                ) / 4.0
    return rows


def measure_rings(bvh, points, segments=32, gap=lambda t, a: 0.08, cap=None, floor=None,
                  reach=3.2, ring_passes=3, axis_passes=1):
    directions, profile = [], []
    for index, point in enumerate(points):
        t = index / (len(points) - 1) if len(points) > 1 else 0.0
        u, v = frame_for(points, index)
        row_directions, row = [], []
        for step in range(segments):
            angle = 2.0 * math.pi * step / segments
            direction = (u * math.cos(angle) + v * math.sin(angle)).normalized()
            radius = ray_radius(bvh, point, direction, reach)
            if radius is not None:
                if cap is not None:
                    radius = min(radius, cap(t, angle))
                if floor is not None:
                    radius = max(radius, floor(t, angle))
            row_directions.append(direction)
            row.append(radius)
        directions.append(row_directions)
        profile.append(fill_gaps(row, 0.35))
    measured = [list(row) for row in profile]
    profile = smooth_profile(profile, ring_passes=ring_passes, axis_passes=axis_passes)
    for row, raw in zip(profile, measured):
        for index, value in enumerate(raw):
            if value > row[index]:
                row[index] = value

    rings = []
    for index, point in enumerate(points):
        t = index / (len(points) - 1) if len(points) > 1 else 0.0
        ring = []
        for step in range(segments):
            angle = 2.0 * math.pi * step / segments
            ring.append(point + directions[index][step] * (profile[index][step] + gap(t, angle)))
        rings.append(ring)
    return rings


def loft(name, rings, mat, collection, close_start=False, close_end=False):
    verts = []
    for ring in rings:
        verts.extend(tuple(point) for point in ring)
    segments = len(rings[0])
    faces = []
    for row in range(len(rings) - 1):
        base = row * segments
        for column in range(segments):
            nxt = (column + 1) % segments
            faces.append((base + column, base + nxt, base + segments + nxt, base + segments + column))
    if close_start:
        faces.append(tuple(reversed(range(segments))))
    if close_end:
        base = (len(rings) - 1) * segments
        faces.append(tuple(base + i for i in range(segments)))
    mesh = bpy.data.meshes.new(name + "_mesh")
    mesh.from_pydata(verts, [], faces)
    mesh.update()
    obj = bpy.data.objects.new(name, mesh)
    collection.objects.link(obj)
    blockout.assign(obj, mat)
    for polygon in mesh.polygons:
        polygon.use_smooth = True
    return obj


def diagonal_panel(name, rings, start_column, end_column, width, mat, collection):
    """A ribbon that slides around the rings as it descends.

    This is what makes a cross-collar: the band starts at a shoulder and walks
    around to the centre front by the waist.
    """
    segments = len(rings[0])
    verts = []
    rows = len(rings)
    for row, ring in enumerate(rings):
        t = row / (rows - 1)
        centre = start_column + (end_column - start_column) * t
        for step in range(width):
            column = centre + step - (width - 1) / 2.0
            low = int(math.floor(column)) % segments
            high = (low + 1) % segments
            blend = column - math.floor(column)
            verts.append(tuple(ring[low].lerp(ring[high], blend)))
    faces = []
    for row in range(rows - 1):
        base = row * width
        for column in range(width - 1):
            faces.append((base + column, base + column + 1, base + width + column + 1, base + width + column))
    mesh = bpy.data.meshes.new(name + "_mesh")
    mesh.from_pydata(verts, [], faces)
    mesh.update()
    obj = bpy.data.objects.new(name, mesh)
    collection.objects.link(obj)
    blockout.assign(obj, mat)
    for polygon in mesh.polygons:
        polygon.use_smooth = True
    return obj


def panel(name, rings, first, last, mat, collection):
    """A ribbon cut from a set of rings, keeping only columns first..last."""
    segments = len(rings[0])
    columns = [i % segments for i in range(first, last + 1)]
    verts = []
    for ring in rings:
        verts.extend(tuple(ring[c]) for c in columns)
    width = len(columns)
    faces = []
    for row in range(len(rings) - 1):
        base = row * width
        for column in range(width - 1):
            faces.append((base + column, base + column + 1, base + width + column + 1, base + width + column))
    mesh = bpy.data.meshes.new(name + "_mesh")
    mesh.from_pydata(verts, [], faces)
    mesh.update()
    obj = bpy.data.objects.new(name, mesh)
    collection.objects.link(obj)
    blockout.assign(obj, mat)
    for polygon in mesh.polygons:
        polygon.use_smooth = True
    return obj


def body_skinning(human, coords):
    """KD-tree of the shaped body plus its weights, for garment skinning."""
    from mathutils.kdtree import KDTree

    tree = KDTree(len(human.data.vertices))
    for vertex in human.data.vertices:
        tree.insert(coords[vertex.index], vertex.index)
    tree.balance()
    weights = [
        [(assignment.group, assignment.weight) for assignment in vertex.groups]
        for vertex in human.data.vertices
    ]
    return tree, weights


def finish(obj, human, rig, skin, thickness=0.035, subdivide=1, pelvis_below=None):
    """Thickness, hem and rig deformation.

    Weights are copied from the nearest body vertex through a KD-tree rather
    than through a Data Transfer modifier: it is deterministic and it cannot
    silently no-op, which is what left the previous pass's garments behind the
    pose.
    """
    tree, weights = skin
    for group in human.vertex_groups:
        obj.vertex_groups.new(name=group.name)
    groups = obj.vertex_groups
    pelvis_group = groups.get("pelvis")
    for vertex in obj.data.vertices:
        if pelvis_below is not None and vertex.co.z < pelvis_below and pelvis_group:
            # Hem cloth hangs from the hips. Letting it inherit thigh weights
            # is what split and tore the skirt around the legs.
            pelvis_group.add([vertex.index], 1.0, "REPLACE")
            continue
        _, index, _ = tree.find(vertex.co)
        for group_index, weight in weights[index]:
            if weight > 0.0005:
                groups[group_index].add([vertex.index], weight, "REPLACE")

    if subdivide:
        smooth = obj.modifiers.new("cloth_smooth", "SUBSURF")
        smooth.levels = subdivide
        smooth.render_levels = subdivide
    solidify = obj.modifiers.new("cloth_thickness", "SOLIDIFY")
    solidify.thickness = thickness
    solidify.offset = 1.0
    solidify.use_rim = True
    bevel = obj.modifiers.new("hem", "BEVEL")
    bevel.width = min(thickness * 0.4, 0.018)
    bevel.segments = 2
    bevel.limit_method = "ANGLE"
    armature = obj.modifiers.new("rig_deform", "ARMATURE")
    armature.object = rig
    return obj


def spline(a, b, count):
    return [a.lerp(b, i / (count - 1)) for i in range(count)]


def chain(sections):
    out = []
    for index, (a, b, count) in enumerate(sections):
        part = spline(a, b, count)
        out.extend(part if index == 0 else part[1:])
    return out


# ---------------------------------------------------------------------------
# costume
#
# Deliberately short. The previous pass layered an over-robe, four hanging
# panels, pauldrons and shin wraps on top of one another and they fought. A
# small set of well-fitted pieces reads better than a large set that
# self-intersects.
# ---------------------------------------------------------------------------


def create_costume(human, rig, joints, bvh, trunk, skin, collection, mats, skip=()):
    pelvis = joints["pelvis"]
    neck = joints["neck"]
    shoulder_z = joints["l-shoulder"].z
    pieces = {}

    # --- ao giao linh, the tunic -------------------------------------------
    hem_z = pelvis.z - 1.62
    top_z = shoulder_z + 0.12
    torso_axis = [
        Vector((0.0, pelvis.y * 0.5, hem_z + (top_z - hem_z) * i / 21.0))
        for i in range(22)
    ]
    # The A-pose arm sits at chest height, so an unconstrained ray at that
    # height hits the arm and balloons the tunic. Measure the chest once and
    # hold the profile to it above the armpit.
    chest_probe = Vector((0.0, pelvis.y * 0.5, pelvis.z + (neck.z - pelvis.z) * 0.55))
    chest_half = max(
        ray_radius(trunk, chest_probe, Vector((1.0, 0.0, 0.0)), 3.2) or 0.95,
        ray_radius(trunk, chest_probe, Vector((-1.0, 0.0, 0.0)), 3.2) or 0.95,
    )
    armpit_t = (pelvis.z + (neck.z - pelvis.z) * 0.60 - hem_z) / (top_z - hem_z)

    def torso_cap(t, angle):
        if t < armpit_t:
            return 9.0
        rise = (t - armpit_t) / max(1e-5, 1.0 - armpit_t)
        return chest_half * (1.0 + 0.09 * rise) - 0.14 * rise * abs(math.cos(angle))

    torso_rings = measure_rings(
        trunk, torso_axis, 36,
        gap=lambda t, a: 0.090 + 0.28 * max(0.0, 0.22 - t),
        cap=torso_cap, ring_passes=6, axis_passes=3,
    )
    pieces["tunic"] = finish(
        loft("ao_giao_linh", torso_rings, mats["indigo"], collection), human, rig, skin, 0.040,
        pelvis_below=pelvis.z - 0.30,
    )

    # --- shoulder yoke ------------------------------------------------------
    # A vertical tube stops at the shoulder line and leaves a boat neck, which
    # is why the previous pass read as off-the-shoulder. The yoke is lofted
    # along the clavicle axis instead, so it wraps over both shoulders and
    # meets the sleeves.
    left_shoulder = joints["l-shoulder"]
    right_shoulder = joints["r-shoulder"]
    yoke_axis = chain([(
        right_shoulder + (right_shoulder - left_shoulder).normalized() * 0.34,
        left_shoulder + (left_shoulder - right_shoulder).normalized() * 0.34,
        11,
    )])
    yoke_rings = measure_rings(
        bvh, yoke_axis, 28,
        gap=lambda t, a: 0.092 + 0.030 * math.sin(math.pi * t),
        cap=lambda t, a: 0.60,
        reach=1.5, ring_passes=4,
    )
    pieces["yoke"] = finish(
        loft("vai_ao_giao_linh", yoke_rings, mats["indigo"], collection), human, rig, skin, 0.040
    )

    # Standing collar. Without it the yoke and the tunic meet in a wide boat
    # neck and the collarbones show through.
    collar_axis = [Vector((0.0, neck.y, neck.z - 0.22 + 0.14 * i)) for i in range(4)]
    collar_rings = measure_rings(
        collar_axis and trunk, collar_axis, 26,
        gap=lambda t, a: 0.075 + 0.030 * (1.0 - t),
        reach=1.4, ring_passes=4,
    )
    pieces["collar"] = finish(
        loft("co_ao_dung", collar_rings, mats["indigo_dark"], collection),
        human, rig, skin, 0.030, subdivide=1,
    )

    # --- sash and belt ------------------------------------------------------
    waist_z = pelvis.z + 0.20
    sash_axis = [Vector((0.0, pelvis.y * 0.5, waist_z + offset)) for offset in (-0.26, -0.06, 0.14, 0.34)]
    sash_rings = measure_rings(
        trunk, sash_axis, 36,
        gap=lambda t, a: 0.205 + 0.055 * math.sin(math.pi * t),
        ring_passes=5,
    )
    print("FIT chest_half=%.2f tunic=%.2f..%.2f sash=%.2f" % (
        chest_half,
        min(max((p - a).length for p in ring) for ring, a in zip(torso_rings, torso_axis)),
        max(max((p - a).length for p in ring) for ring, a in zip(torso_rings, torso_axis)),
        max(max((p - a).length for p in ring) for ring, a in zip(sash_rings, sash_axis)),
    ))
    pieces["sash"] = finish(
        loft("that_lung_do", sash_rings, mats["red"], collection), human, rig, skin, 0.028,
        subdivide=0, pelvis_below=99.0,
    )

    belt_axis = [Vector((0.0, pelvis.y * 0.5, waist_z - 0.42 + offset)) for offset in (0.0, 0.12, 0.24)]
    belt_rings = measure_rings(trunk, belt_axis, 36, gap=lambda t, a: 0.255, ring_passes=5)
    pieces["belt"] = finish(
        loft("dai_da", belt_rings, mats["dark_leather"], collection), human, rig, skin, 0.032,
        subdivide=0, pelvis_below=99.0,
    )

    # --- sleeves and bracers ------------------------------------------------
    for side in ("l", "r"):
        shoulder = joints[side + "-shoulder"]
        elbow = joints[side + "-elbow"]
        hand = joints[side + "-hand"]
        # Start just outboard of the joint. Starting inboard of it put the
        # first rings inside the ribcage and sheared the sleeve on skinning.
        axis = chain([
            (shoulder.lerp(elbow, -0.16), elbow, 8),
            (elbow, elbow.lerp(hand, 0.40), 4),
        ])
        rings = measure_rings(
            bvh, axis, 24,
            gap=lambda t, a: 0.108 + 0.070 * t,
            cap=lambda t, a: 0.44 + 0.52 * t,
            reach=1.4, ring_passes=4,
        )
        pieces["sleeve_" + side] = finish(
            loft("tay_ao_" + side, rings, mats["indigo"], collection), human, rig, skin, 0.036
        )

        bracer_axis = chain([(elbow.lerp(hand, 0.34), elbow.lerp(hand, 0.88), 5)])
        bracer_rings = measure_rings(bvh, bracer_axis, 20, gap=lambda t, a: 0.070, reach=1.2)
        pieces["bracer_" + side] = finish(
            loft("bao_tay_dong_" + side, bracer_rings, mats["bronze"], collection),
            human, rig, skin, 0.045, subdivide=0,
        )

    # --- trousers and boots --------------------------------------------------
    crotch_z = pelvis.z - 1.00
    seat_axis = [
        Vector((0.0, pelvis.y * 0.5, pelvis.z + 0.10 - 0.27 * i)) for i in range(4)
    ]
    seat_rings = measure_rings(trunk, seat_axis, 30, gap=lambda t, a: 0.085, reach=2.0, ring_passes=5)
    pieces["seat"] = finish(
        loft("cap_quan", seat_rings, mats["indigo_dark"], collection), human, rig, skin, 0.034
    )

    for side in ("l", "r"):
        sign = 1.0 if side == "l" else -1.0
        knee = joints[side + "-knee"]
        ankle = joints[side + "-ankle"]
        hip = Vector((sign * 0.47, pelvis.y, crotch_z))
        axis = chain([(hip, knee, 6), (knee, ankle.lerp(knee, 0.24), 6)])
        if "trousers" not in skip:
            rings = measure_rings(
                bvh, axis, 26,
                gap=lambda t, a: 0.085 + 0.070 * t,
                reach=1.5, ring_passes=5,
            )
            pieces["trousers_" + side] = finish(
                loft("quan_chien_" + side, rings, mats["indigo_dark"], collection),
                human, rig, skin, 0.034,
            )

        ball = joints[side + "-foot-1"]
        tip = toe_tip(joints, side)
        boot_axis = chain([
            (ankle + Vector((0.0, 0.0, 0.70)), ankle, 4),
            (ankle, ball, 3),
            (ball, tip + (tip - ball).normalized() * 0.20, 3),
        ])
        if "boots" not in skip:
            boot_rings = measure_rings(bvh, boot_axis, 20, gap=lambda t, a: 0.075 + 0.035 * t, reach=1.2)
            for ring in boot_rings:
                for point in ring:
                    point.z = max(point.z, 0.020)
            pieces["boot_" + side] = finish(
                loft("giay_da_" + side, boot_rings, mats["leather"], collection, close_end=True),
                human, rig, skin, 0.045, subdivide=0,
            )

    return pieces


def parent_to_bone(obj, rig, bone_name):
    """Parent to a bone, keeping the object exactly where it is.

    Two traps here, both of which have bitten this build. matrix_world is only
    recomputed when the depsgraph is evaluated, so it must be refreshed before
    being read. And Blender measures a bone parent from the bone's TAIL, so the
    offset is solved explicitly rather than by assigning matrix_world back and
    hoping the setter resolves against an up-to-date parent.
    """
    bpy.context.view_layer.update()
    world = obj.matrix_world.copy()
    bone = rig.pose.bones[bone_name]
    parent_world = rig.matrix_world @ bone.matrix @ Matrix.Translation((0.0, bone.length, 0.0))
    obj.parent = rig
    obj.parent_type = "BONE"
    obj.parent_bone = bone_name
    obj.matrix_parent_inverse = Matrix.Identity(4)
    obj.matrix_basis = parent_world.inverted() @ world
    bpy.context.view_layer.update()
    return obj


def axe_blade(name, location, mat, collection, thickness=0.155):
    """An asymmetric stone blade, offset to one side of the haft.

    Drawn in the local XZ plane so the face turns with the weapon's roll: two
    horns at the socket, a curved edge sweeping out to -X.
    """
    outline = [
        (0.11, -0.52), (0.11, 0.54), (-0.24, 0.80), (-0.70, 0.78),
        (-1.02, 0.42), (-1.12, 0.02), (-0.98, -0.46), (-0.66, -0.74), (-0.22, -0.78),
    ]
    verts = [(x, -thickness, z) for x, z in outline] + [(x, thickness, z) for x, z in outline]
    count = len(outline)
    faces = [tuple(range(count)), tuple(reversed(range(count, count * 2)))]
    for index in range(count):
        nxt = (index + 1) % count
        faces.append((index, nxt, nxt + count, index + count))
    mesh = bpy.data.meshes.new(name + "_mesh")
    mesh.from_pydata(verts, [], faces)
    mesh.update()
    obj = bpy.data.objects.new(name, mesh)
    collection.objects.link(obj)
    obj.location = location
    blockout.assign(obj, mat)
    blockout.bevel(obj, 0.032, 2)
    return obj


def dong_son_star(name, location, normal, outer, inner, depth, mat, collection, points=12):
    """A radial Dong Son drum face. Vietnamese, not a Chinese cloud motif."""
    verts, faces = [], []
    count = points * 2
    for layer in (-depth / 2.0, depth / 2.0):
        for index in range(count):
            angle = 2.0 * math.pi * index / count
            radius = outer if index % 2 == 0 else inner
            verts.append((math.cos(angle) * radius, math.sin(angle) * radius, layer))
    faces.append(tuple(range(count)))
    faces.append(tuple(reversed(range(count, count * 2))))
    for index in range(count):
        nxt = (index + 1) % count
        faces.append((index, nxt, nxt + count, index + count))
    mesh = bpy.data.meshes.new(name + "_mesh")
    mesh.from_pydata(verts, [], faces)
    mesh.update()
    obj = bpy.data.objects.new(name, mesh)
    collection.objects.link(obj)
    blockout.assign(obj, mat)
    obj.rotation_mode = "QUATERNION"
    obj.rotation_quaternion = Vector(normal).to_track_quat("Z", "Y")
    obj.location = location
    blockout.bevel(obj, depth * 0.3, 2)
    return obj


def create_ornaments(human, coords, rig, joints, bvh, trunk, skin, collection, mats):
    pelvis = joints["pelvis"]
    neck = joints["neck"]
    head = joints["head"]
    crown_z = max(point.z for point in coords)

    def front_of(center, clearance):
        radius = ray_radius(trunk, center, Vector((0.0, -1.0, 0.0)), 3.2) or 0.4
        return center.y - radius - clearance

    # --- Dong Son drum face worn on the chest, holding a Long Ngoc shard ----
    chest_z = pelvis.z + (neck.z - pelvis.z) * 0.58
    chest_center = Vector((0.0, pelvis.y * 0.5, chest_z))
    chest_y = front_of(chest_center, 0.30)
    medallion = dong_son_star(
        "huy_hieu_trong_dong", (0.0, chest_y, chest_z), (0.0, -1.0, 0.14),
        0.26, 0.13, 0.065, mats["bronze"], collection, points=12,
    )
    core = blockout.sphere(
        "manh_long_ngoc", (0.0, chest_y - 0.070, chest_z), (0.105, 0.048, 0.105),
        mats["jade"], collection, 24, 14,
    )
    parent_to_bone(medallion, rig, "spine_03")
    parent_to_bone(core, rig, "spine_03")

    # --- woven headband, sitting on the brow rather than across the eyes ----
    eye = joints.get("l-eye")
    band_z = crown_z - 0.22
    print("HEAD crown=%.2f band=%.2f eye=%s" % (crown_z, band_z, None if eye is None else round(eye.z, 2)))
    band_axis = [Vector((0.0, head.y, band_z + offset)) for offset in (-0.055, 0.0, 0.055)]
    band_rings = measure_rings(bvh, band_axis, 26, gap=lambda t, a: 0.105, reach=1.2)
    band = loft("khan_dau_lac", band_rings, mats["red"], collection)
    solidify = band.modifiers.new("band_thickness", "SOLIDIFY")
    solidify.thickness = 0.030
    solidify.offset = 1.0
    parent_to_bone(band, rig, "head")

    band_y = front_of(Vector((0.0, head.y, band_z)), 0.015)
    stud = dong_son_star(
        "dinh_dong_khan", (0.0, band_y, band_z), (0.0, -1.0, 0.0),
        0.075, 0.035, 0.030, mats["bronze"], collection, points=8,
    )
    parent_to_bone(stud, rig, "head")

    # --- belt buckle --------------------------------------------------------
    buckle_z = pelvis.z - 0.14
    buckle_y = front_of(Vector((0.0, pelvis.y * 0.5, buckle_z)), 0.31)
    buckle = dong_son_star(
        "khoa_dai_dong", (0.0, buckle_y, buckle_z), (0.0, -1.0, 0.0),
        0.200, 0.098, 0.055, mats["bronze"], collection, points=10,
    )
    jade = blockout.sphere(
        "khoa_ngoc", (0.0, buckle_y - 0.050, buckle_z), (0.070, 0.032, 0.070),
        mats["jade"], collection, 20, 12,
    )
    parent_to_bone(buckle, rig, "pelvis")
    parent_to_bone(jade, rig, "pelvis")

    # --- bronze shoulder discs ----------------------------------------------
    # A disc on the deltoid, not a lofted tube. Lofting the A-pose shoulder
    # produced the gold blobs in the previous pass.
    for side, sign, bone in (("l", 1.0, "upperarm_l"), ("r", -1.0, "upperarm_r")):
        shoulder = joints[side + "-shoulder"]
        elbow = joints[side + "-elbow"]
        outward = (elbow - shoulder).normalized()
        center = shoulder + outward * 0.30
        radius = ray_radius(bvh, center, Vector((0.0, 0.0, 1.0)), 1.5) or 0.35
        disc = dong_son_star(
            "giap_vai_dong_" + side,
            tuple(center + Vector((0.0, 0.0, radius + 0.085))),
            (sign * 0.35, -0.10, 1.0),
            0.33, 0.17, 0.075, mats["bronze"], collection, points=12,
        )
        parent_to_bone(disc, rig, bone)


# ---------------------------------------------------------------------------
# pose
# ---------------------------------------------------------------------------


def aim_bone(rig, name, direction, roll_reference):
    """Point a bone along a world direction with a controlled roll.

    A bone's local +Y runs head to tail. ``roll_reference`` fixes the spin
    about that axis, which is exactly what the IK pole angle was getting
    wrong.
    """
    bone = rig.pose.bones.get(name)
    if not bone:
        return
    bpy.context.view_layer.update()
    axis_y = Vector(direction).normalized()
    reference = Vector(roll_reference)
    axis_x = reference.cross(axis_y)
    if axis_x.length < 1e-4:
        axis_x = Vector((0.0, 0.0, 1.0)).cross(axis_y)
    axis_x.normalize()
    axis_z = axis_x.cross(axis_y)
    matrix = Matrix((axis_x, axis_y, axis_z)).transposed().to_4x4()
    matrix.translation = bone.matrix.translation
    bone.matrix = matrix
    bpy.context.view_layer.update()


# World-space aim for every limb bone, parents before children. The character
# faces -Y and their left is +X. Weight sits on the left leg; the right leg is
# forward and turned out.
LIMB_POSE = (
    ("thigh_l", (0.05, -0.07, -1.00), (0.0, -1.0, 0.0)),
    ("calf_l", (0.02, 0.07, -1.00), (0.0, -1.0, 0.0)),
    ("foot_l", (0.14, -0.86, -0.49), (0.0, 0.0, 1.0)),
    ("ball_l", (0.09, -0.96, -0.26), (0.0, 0.0, 1.0)),
    ("thigh_r", (-0.13, -0.17, -0.98), (0.0, -1.0, 0.0)),
    ("calf_r", (-0.03, 0.13, -0.99), (0.0, -1.0, 0.0)),
    ("foot_r", (-0.30, -0.83, -0.47), (0.0, 0.0, 1.0)),
    ("ball_r", (-0.22, -0.95, -0.23), (0.0, 0.0, 1.0)),
    ("upperarm_l", (0.19, -0.13, -0.97), (0.0, 1.0, 0.0)),
    ("lowerarm_l", (0.05, -0.63, -0.77), (0.0, 1.0, 0.0)),
    ("hand_l", (0.04, -0.62, -0.78), (0.0, 1.0, 0.0)),
    ("upperarm_r", (-0.17, 0.05, -0.98), (0.0, 1.0, 0.0)),
    ("lowerarm_r", (-0.11, -0.31, -0.94), (0.0, 1.0, 0.0)),
    ("hand_r", (-0.11, -0.33, -0.94), (0.0, 1.0, 0.0)),
)


def ground_rig(rig):
    """Drop the rig so the soles touch the plinth.

    Aiming the bones leaves the feet wherever the chain lands, so the figure is
    settled onto the floor afterwards rather than by guessing a pelvis offset.
    """
    depsgraph = bpy.context.evaluated_depsgraph_get()
    lowest = None
    for obj in bpy.context.scene.objects:
        if obj.type != "MESH" or not (
            obj.name.startswith("giay_da_") or "boots" in obj.name.lower()
        ):
            continue
        evaluated = obj.evaluated_get(depsgraph)
        mesh = evaluated.to_mesh()
        for vertex in mesh.vertices:
            z = (evaluated.matrix_world @ vertex.co).z
            if lowest is None or z < lowest:
                lowest = z
        evaluated.to_mesh_clear()
    if lowest is not None:
        rig.location.z += 0.015 - lowest
        bpy.context.view_layer.update()
    return lowest


def pose_character(rig, controls):
    """Grounded contrapposto, axe shouldered in the left hand.

    The camera sits on the character's left, so the weapon reads in front of
    the silhouette rather than behind it.
    """
    rig.data.pose_position = "POSE"

    def rot(name, degrees):
        bone = rig.pose.bones.get(name)
        if not bone:
            return
        bone.rotation_mode = "XYZ"
        bone.rotation_euler = tuple(math.radians(v) for v in degrees)

    rot("pelvis", (1.0, -3.0, 5.0))
    rot("spine_01", (2.0, 2.0, -3.0))
    rot("spine_02", (2.0, 3.0, -3.0))
    rot("spine_03", (-2.0, 3.0, -2.0))
    rot("neck_01", (2.0, -2.0, 4.0))
    rot("head", (-4.0, 1.0, 10.0))
    rot("clavicle_l", (0.0, 7.0, 0.0))
    rot("clavicle_r", (0.0, -5.0, 0.0))
    bpy.context.view_layer.update()

    for name, direction, roll in LIMB_POSE:
        aim_bone(rig, name, direction, roll)

    # Left hand closes hard around the haft, right hand rests half open.
    for side, curl, thumb in (("l", 76.0, 42.0), ("r", 24.0, 12.0)):
        for finger in ("index", "middle", "ring", "pinky"):
            for joint, scale in (("01", 0.95), ("02", 1.15), ("03", 0.85)):
                rot(f"{finger}_{joint}_{side}", (curl * scale, 0.0, 0.0))
        for joint in ("01", "02", "03"):
            rot(f"thumb_{joint}_{side}", (thumb, 0.0, 0.0))

    bpy.context.view_layer.update()
    ground_rig(rig)

    for name in ("foot_l", "foot_r", "hand_l", "hand_r"):
        bone = rig.pose.bones.get(name)
        tail = rig.matrix_world @ bone.tail
        print("POSE %-9s tail=(%6.2f,%6.2f,%6.2f)" % (name, tail.x, tail.y, tail.z))


# ---------------------------------------------------------------------------
# weapon
# ---------------------------------------------------------------------------


def create_weapon(rig, collection, mats):
    """Riu Than Thach Son, planted head-down on the stone.

    Built along +Z in local space, then fitted to the measured left palm so the
    haft passes through the closed fist. v2 placed the axe in world space and
    the hand never actually met it.
    """
    haft_length = 4.85
    grip_from_butt = 1.05

    root = bpy.data.objects.new("Riu_Than_Thach_Son", None)
    collection.objects.link(root)
    root.empty_display_size = 0.3

    parts = [
        blockout.cylinder_between(
            "can_riu", (0.0, 0.0, 0.10), (0.0, 0.0, haft_length - 0.30), 0.098, mats["leather"], collection, 20
        ),
        blockout.sphere("chuoi_ngoc", (0.0, 0.0, 0.06), (0.150, 0.150, 0.20), mats["jade"], collection, 24, 14),
        blockout.cylinder("de_dong", (0.0, 0.0, haft_length - 0.58), 0.180, 0.52, mats["bronze"], collection, 22),
    ]
    for index in range(8):
        parts.append(blockout.torus(
            f"quan_can_{index}", (0.0, 0.0, 0.40 + index * 0.150), 0.108, 0.028, mats["dark_leather"], collection
        ))

    parts.append(axe_blade("luoi_riu_thach_son", (0.0, 0.0, haft_length), mats["stone"], collection))
    # Than khi burning along the cutting edge.
    for offset, half, tilt in ((0.44, 0.26, -0.46), (-0.04, 0.28, 0.0), (-0.50, 0.24, 0.44)):
        parts.append(blockout.cube(
            "than_khi_luoi", (-1.09, 0.0, haft_length + offset), (0.055, 0.165, half),
            mats["ember"], collection, rotation=(0.0, tilt, 0.0), bevel_width=0.022,
        ))
    # Bronze binding holding the blade to the haft.
    for z in (haft_length - 0.42, haft_length + 0.44):
        parts.append(blockout.cube(
            "nep_dong_luoi", (-0.16, 0.0, z), (0.40, 0.195, 0.055),
            mats["bronze"], collection, bevel_width=0.030,
        ))
    for y, normal in ((-0.175, (0.0, -1.0, 0.0)), (0.175, (0.0, 1.0, 0.0))):
        parts.append(dong_son_star(
            "dau_trong_dong_riu", (-0.44, y, haft_length + 0.02), normal,
            0.165, 0.080, 0.030, mats["bronze"], collection, points=10,
        ))

    for part in parts:
        local = part.matrix_world.copy()
        part.parent = root
        part.matrix_parent_inverse = Matrix.Identity(4)
        part.matrix_basis = local

    bpy.context.view_layer.update()
    hand = rig.pose.bones.get("hand_l")
    palm = rig.matrix_world @ hand.matrix @ Vector((0.0, 0.14, 0.0))

    # Head down and forward of the feet, butt up behind the shoulder.
    # Local +Z runs butt to blade, so +Z points down the planted haft. The
    # roll matters too: to_track_quat picks an arbitrary one and laid the blade
    # flat on the stone, so the basis is built by hand with the blade face
    # (local +Y) turned toward camera.
    direction = Vector((0.30, 0.30, 0.905)).normalized()
    face = Vector((0.86, -0.51, 0.0)).normalized()
    axis_x = face.cross(direction).normalized()
    axis_y = direction.cross(axis_x).normalized()
    root.rotation_mode = "QUATERNION"
    root.rotation_quaternion = Matrix((axis_x, axis_y, direction)).transposed().to_quaternion()
    root.location = palm - direction * grip_from_butt
    bpy.context.view_layer.update()

    parent_to_bone(root, rig, "hand_l")

    tip = root.matrix_world @ Vector((0.0, 0.0, haft_length))
    print("AXE head world =", tuple(round(v, 2) for v in tip), " grip =", tuple(round(v, 2) for v in palm))
    return root


# ---------------------------------------------------------------------------
# stage and presentation
# ---------------------------------------------------------------------------


def create_stage(collection, mats):
    blockout.cylinder("be_da_uot", (0.0, 0.0, -0.34), 3.9, 0.55, mats["stage"], collection, 96)
    for index, (x, y, z, scale, seed) in enumerate([
        (-3.05, 0.85, 0.22, 0.95, 0),
        (3.20, 1.05, 0.16, 0.72, 1),
        (-2.70, -1.55, 0.15, 0.52, 2),
        (2.85, -1.45, 0.12, 0.40, 3),
        (0.35, 2.85, 0.20, 0.62, 4),
    ]):
        rock = blockout.ico(f"da_bazan_{index}", (x, y, z), (scale * 0.55, scale * 0.42, scale), mats["stone"], collection, 2)
        rock.rotation_euler = (0.21 * seed, -0.14 * seed, 0.47 * seed)


def create_lights(collection):
    """Warm key carries the skin; the cool and ember lights are rim only.

    v2 did the opposite and the character read as a corpse.
    """
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
        return obj

    area("key_warm", (-5.6, -9.8, 9.6), 2100, (1.0, 0.86, 0.69), 7.0, (0.0, 0.0, 4.6))
    area("fill_soft", (7.4, -7.6, 4.6), 620, (0.58, 0.70, 0.92), 7.0, (0.0, 0.0, 4.2))
    area("rim_river_teal", (5.4, 6.6, 8.2), 4200, (0.18, 0.80, 0.84), 2.4, (0.3, 0.0, 5.2))
    area("rim_ember", (-6.0, 3.8, 4.4), 2600, (1.0, 0.30, 0.08), 2.2, (-0.4, 0.0, 4.2))
    area("eye_light", (-1.4, -6.4, 8.2), 90, (1.0, 0.90, 0.78), 1.5, (0.0, -0.25, 7.5))


def setup_render(collection, filepath, resolution, camera_location, camera_target, lens, samples=96):
    scene = bpy.context.scene
    scene.render.engine = "BLENDER_EEVEE_NEXT"
    scene.render.resolution_x, scene.render.resolution_y = resolution
    scene.render.resolution_percentage = 100
    scene.render.image_settings.file_format = "PNG"
    scene.render.filepath = str(filepath)
    scene.render.film_transparent = False
    scene.eevee.taa_render_samples = samples
    for attribute, value in (
        ("use_raytracing", True),
        ("use_shadows", True),
        ("shadow_ray_count", 2),
        ("shadow_step_count", 6),
    ):
        if hasattr(scene.eevee, attribute):
            setattr(scene.eevee, attribute, value)
    scene.view_settings.view_transform = "AgX"
    try:
        scene.view_settings.look = "AgX - Medium High Contrast"
    except Exception:
        pass

    scene.world.use_nodes = True
    background = scene.world.node_tree.nodes.get("Background")
    background.inputs["Color"].default_value = (0.014, 0.019, 0.028, 1.0)
    background.inputs["Strength"].default_value = 0.50

    camera = scene.camera
    if camera is None:
        data = bpy.data.cameras.new("Long_Nhan_Camera")
        camera = bpy.data.objects.new("Long_Nhan_Camera", data)
        collection.objects.link(camera)
        scene.camera = camera
    camera.location = camera_location
    camera.data.lens = lens
    camera.data.sensor_width = 36
    blockout.look_at(camera, camera_target)
    return camera


def setup_compositor():
    scene = bpy.context.scene
    scene.use_nodes = True
    nodes, links = scene.node_tree.nodes, scene.node_tree.links
    nodes.clear()
    render_layers = nodes.new("CompositorNodeRLayers")
    glare = nodes.new("CompositorNodeGlare")
    glare.glare_type = "FOG_GLOW"
    glare.quality = "HIGH"
    glare.threshold = 1.5
    glare.size = 7
    glare.mix = -0.92
    composite = nodes.new("CompositorNodeComposite")
    links.new(render_layers.outputs["Image"], glare.inputs["Image"])
    links.new(glare.outputs["Image"], composite.inputs["Image"])


# ---------------------------------------------------------------------------
# build
# ---------------------------------------------------------------------------


def build():
    blockout.clear_scene()
    body_collection = blockout.make_collection("LONG_NHAN_BODY")
    costume_collection = blockout.make_collection("LONG_NHAN_COSTUME")
    weapon_collection = blockout.make_collection("RIU_THAN_THACH_SON")
    controls_collection = blockout.make_collection("RIG_CONTROLS")
    stage_collection = blockout.make_collection("STAGE")

    human, rig, attachments = create_human(body_collection)
    mats = make_materials()
    for label, key in (("hair", "hair"), ("trousers", "indigo_dark"), ("boots", "leather")):
        obj = attachments.get(label)
        if obj:
            obj.data.materials.clear()
            blockout.assign(obj, mats[key])

    coords = shaped_coords(human)
    joints = joint_positions(human, coords)
    bvh, trunk = build_ray_targets(human, coords, joints)
    skin = body_skinning(human, coords)

    create_costume(
        human, rig, joints, bvh, trunk, skin, costume_collection, mats,
        skip={label for label in ("trousers", "boots") if label in attachments},
    )
    create_ornaments(human, coords, rig, joints, bvh, trunk, skin, costume_collection, mats)
    pose_character(rig, controls_collection)
    create_weapon(rig, weapon_collection, mats)
    create_stage(stage_collection, mats)
    create_lights(stage_collection)
    setup_compositor()
    controls_collection.hide_render = True

    human["character_id"] = "PLAYER-LONG-NHAN"
    human["asset_status"] = "v3_combat_concept"
    human["design_note"] = (
        "Ao giao linh cross-collar tunic, ao tu than hanging panels, Lac red sash, "
        "Dong Son radial bronze, river jade. No Chinese cloud, hanfu or imperial motifs."
    )
    human["library"] = "MPFB 2.0.17 / MakeHuman System Assets CC0"
    bpy.context.scene["project"] = "Huyet Mach Lac Long"
    bpy.context.scene["asset_scope"] = "Main character v3"

    bpy.ops.wm.save_as_mainfile(filepath=str(OUT_DIR / "long_nhan_v3.blend"))

    setup_render(
        stage_collection,
        OUT_DIR / "long_nhan_v3_hero.png",
        (1100, 1500),
        (9.2, -19.8, 5.4),
        (0.05, -0.15, 4.45),
        60,
        samples=160,
    )
    bpy.ops.render.render(write_still=True)

    setup_render(
        stage_collection,
        OUT_DIR / "long_nhan_v3_portrait.png",
        (900, 1100),
        (2.30, -6.60, 9.05),
        (0.0, -0.28, 8.45),
        105,
        samples=160,
    )
    bpy.ops.render.render(write_still=True)

    print(
        "V3_BUILD verts=%d objects=%d attachments=%s"
        % (len(human.data.vertices), len(bpy.context.scene.objects), sorted(attachments))
    )


if __name__ == "__main__":
    build()
