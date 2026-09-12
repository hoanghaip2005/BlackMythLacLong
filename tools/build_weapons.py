"""Dong Son weapon set for Huyet Mach Lac Long.

No open-source library carries Vietnamese Bronze Age weapons - the CC0 packs on
the MakeHuman repository hold a war hammer, a crude sword, a dagger, a bow and
a sceptre, all generic Western fantasy. So this set is authored, working from
the documented Dong Son corpus rather than from fantasy-game conventions.

The eight pieces:

  1. dao_gam_can_tuong   Dagger with a standing human figure as its hilt. The
                         single most recognisable Dong Son artefact.
  2. doan_kiem_ri_set    The rusted short sword Long Nhan wakes beside in
                         CH-01. Canon: it shatters when the axe awakens.
  3. riu_xeo_chien_binh  Rifle-shaped "boot axe" - riu luoi xeo - the
                         asymmetric Dong Son battle axe. Common soldier's.
  4. riu_than_thach_son  The hero weapon, the same riu xeo silhouette taken to
                         ceremonial scale with a drum face on the cheek.
  5. qua_dong            Bronze dagger-axe, blade set square to the haft.
  6. giao_dong           Socketed leaf-blade spear with a raised midrib.
  7. no_than             The crossbow of the An Duong Vuong legend.
  8. moc_khien           Round shield carrying a full drum tympanum.

Scale matches the character rig: 4.77 units per metre, so any of these can be
appended straight into the Long Nhan scene and parented to a hand bone.

Run:
    blender -b -P tools/build_weapons.py
"""

import math
import sys
from pathlib import Path

import bpy
from mathutils import Vector

TOOLS = Path(__file__).resolve().parent
ROOT = TOOLS.parent
OUT_DIR = ROOT / "assets" / "weapons"
OUT_DIR.mkdir(parents=True, exist_ok=True)
sys.path.insert(0, str(TOOLS))
import build_long_nhan as blockout
import dong_son_ornament as ornament

# Units per metre, matching the MPFB character build.
M = 4.77


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


def bronze_material(name, patina=0.26, polish=0.42):
    """Cast bronze, patina collecting in the recesses.

    Dong Son bronze is a high-tin alloy: warmer and darker than brass, and it
    weathers to a green-black rather than to verdigris blue.
    """
    mat, tree, bsdf = _principled(name)
    nodes, links = tree.nodes, tree.links
    coord = nodes.new("ShaderNodeTexCoord")
    noise = nodes.new("ShaderNodeTexNoise")
    noise.inputs["Scale"].default_value = 110.0
    noise.inputs["Detail"].default_value = 9.0
    ramp = nodes.new("ShaderNodeValToRGB")
    ramp.color_ramp.elements[0].position = patina
    ramp.color_ramp.elements[0].color = (0.034, 0.058, 0.044, 1.0)
    ramp.color_ramp.elements[1].position = polish
    ramp.color_ramp.elements[1].color = (0.355, 0.215, 0.092, 1.0)
    metallic = nodes.new("ShaderNodeMapRange")
    metallic.inputs["From Min"].default_value = patina
    metallic.inputs["From Max"].default_value = polish
    metallic.inputs["To Min"].default_value = 0.30
    metallic.inputs["To Max"].default_value = 1.0
    rough = nodes.new("ShaderNodeMapRange")
    rough.inputs["From Min"].default_value = patina
    rough.inputs["From Max"].default_value = polish
    rough.inputs["To Min"].default_value = 0.72
    rough.inputs["To Max"].default_value = 0.22
    bump = nodes.new("ShaderNodeBump")
    bump.inputs["Strength"].default_value = 0.18
    bump.inputs["Distance"].default_value = 0.004
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


def corroded_material(name):
    """Bronze eaten by centuries of seawater, for the CH-01 short sword.

    Mostly dead oxide with a few surviving flashes of metal, so the sword reads
    as a survival tool rather than as a weapon of destiny.
    """
    mat, tree, bsdf = _principled(name)
    nodes, links = tree.nodes, tree.links
    coord = nodes.new("ShaderNodeTexCoord")
    rot = nodes.new("ShaderNodeTexNoise")
    rot.inputs["Scale"].default_value = 95.0
    rot.inputs["Detail"].default_value = 9.0
    rot.inputs["Roughness"].default_value = 0.75
    ramp = nodes.new("ShaderNodeValToRGB")
    ramp.color_ramp.elements[0].position = 0.36
    ramp.color_ramp.elements[0].color = (0.052, 0.060, 0.048, 1.0)
    ramp.color_ramp.elements[1].position = 0.66
    ramp.color_ramp.elements[1].color = (0.175, 0.115, 0.055, 1.0)
    metallic = nodes.new("ShaderNodeMapRange")
    metallic.inputs["From Min"].default_value = 0.60
    metallic.inputs["From Max"].default_value = 0.72
    metallic.inputs["To Min"].default_value = 0.0
    metallic.inputs["To Max"].default_value = 0.85
    bump = nodes.new("ShaderNodeBump")
    bump.inputs["Strength"].default_value = 0.62
    bump.inputs["Distance"].default_value = 0.010
    links.new(coord.outputs["Object"], rot.inputs["Vector"])
    links.new(rot.outputs["Fac"], ramp.inputs["Fac"])
    links.new(rot.outputs["Fac"], metallic.inputs["Value"])
    links.new(rot.outputs["Fac"], bump.inputs["Height"])
    links.new(ramp.outputs["Color"], bsdf.inputs["Base Color"])
    links.new(metallic.outputs["Result"], bsdf.inputs["Metallic"])
    links.new(bump.outputs["Normal"], bsdf.inputs["Normal"])
    bsdf.inputs["Roughness"].default_value = 0.86
    return mat


def wood_material(name, dark=(0.030, 0.017, 0.009), light=(0.135, 0.082, 0.040)):
    mat, tree, bsdf = _principled(name)
    nodes, links = tree.nodes, tree.links
    coord = nodes.new("ShaderNodeTexCoord")
    stretch = nodes.new("ShaderNodeMapping")
    stretch.inputs["Scale"].default_value = (14.0, 14.0, 0.7)
    grain = nodes.new("ShaderNodeTexNoise")
    grain.inputs["Scale"].default_value = 9.0
    grain.inputs["Detail"].default_value = 7.0
    ramp = nodes.new("ShaderNodeValToRGB")
    ramp.color_ramp.elements[0].position = 0.36
    ramp.color_ramp.elements[0].color = (*dark, 1.0)
    ramp.color_ramp.elements[1].position = 0.66
    ramp.color_ramp.elements[1].color = (*light, 1.0)
    bump = nodes.new("ShaderNodeBump")
    bump.inputs["Strength"].default_value = 0.30
    bump.inputs["Distance"].default_value = 0.004
    links.new(coord.outputs["Object"], stretch.inputs["Vector"])
    links.new(stretch.outputs["Vector"], grain.inputs["Vector"])
    links.new(grain.outputs["Fac"], ramp.inputs["Fac"])
    links.new(ramp.outputs["Color"], bsdf.inputs["Base Color"])
    links.new(grain.outputs["Fac"], bump.inputs["Height"])
    links.new(bump.outputs["Normal"], bsdf.inputs["Normal"])
    bsdf.inputs["Roughness"].default_value = 0.72
    return mat


def simple_material(name, color, metallic=0.0, roughness=0.6, emission=None):
    return blockout.material(name, color, metallic, roughness, emission)


def make_materials():
    return {
        "bronze": bronze_material("dong_dong_son"),
        "bronze_dark": bronze_material("dong_xam", patina=0.40, polish=0.58),
        "corroded": corroded_material("dong_muc_nuoc_bien"),
        "wood": wood_material("go_lim"),
        "wood_pale": wood_material("go_sang", (0.062, 0.040, 0.020), (0.215, 0.150, 0.082)),
        "cord": simple_material("day_quan_gai", (0.055, 0.030, 0.016), 0.0, 0.88),
        "leather": simple_material("da_trau", (0.055, 0.028, 0.013), 0.0, 0.62),
        "stone": simple_material("da_thach_son", (0.038, 0.040, 0.044), 0.05, 0.80),
        "jade": simple_material("long_ngoc", (0.020, 0.185, 0.120), 0.10, 0.16,
                                emission=((0.02, 0.40, 0.26), 0.7)),
        "ember": simple_material("than_khi", (0.32, 0.050, 0.012), 0.2, 0.32,
                                 emission=((1.0, 0.20, 0.03), 7.0)),
        "red": simple_material("do_lac", (0.30, 0.035, 0.018), 0.0, 0.78),
    }


# ---------------------------------------------------------------------------
# geometry helpers
# ---------------------------------------------------------------------------


def prism(name, outline, thickness, mat, collection, bevel=0.0):
    """Extrude a 2D outline given in the XZ plane, thickness along Y.

    Weapon blades are flat objects, so they are drawn in profile and given
    depth, which keeps the silhouette editable as a list of points.
    """
    count = len(outline)
    verts = [(x, -thickness / 2.0, z) for x, z in outline]
    verts += [(x, thickness / 2.0, z) for x, z in outline]
    faces = [tuple(range(count)), tuple(reversed(range(count, count * 2)))]
    for index in range(count):
        nxt = (index + 1) % count
        faces.append((index, nxt, nxt + count, index + count))
    mesh = bpy.data.meshes.new(name + "_mesh")
    mesh.from_pydata(verts, [], faces)
    mesh.update()
    obj = bpy.data.objects.new(name, mesh)
    collection.objects.link(obj)
    obj.data.materials.append(mat)
    if bevel:
        blockout.bevel(obj, bevel, 2)
    return obj


def tube(name, start, end, radius, mat, collection, sides=16):
    obj = blockout.cylinder_between(name, start, end, radius, mat, collection, sides)
    blockout.move_to_collection(obj, collection)
    return obj


def wrap_bands(name, start, end, radius, count, mat, collection):
    """Cord binding on a haft or a hilt."""
    start, end = Vector(start), Vector(end)
    pieces = []
    for index in range(count):
        t = (index + 0.5) / count
        centre = start.lerp(end, t)
        obj = blockout.torus(
            f"{name}_{index}", tuple(centre), radius, radius * 0.24, mat, collection,
        )
        blockout.move_to_collection(obj, collection)
        pieces.append(obj)
    return pieces


def lay_flat(obj, angle=math.radians(90.0)):
    obj.rotation_euler = (angle, 0.0, 0.0)
    return obj


def place(objects, location):
    """Move a finished weapon to its slot on the contact sheet."""
    for obj in objects:
        if obj and obj.parent is None:
            obj.location = Vector(obj.location) + Vector(location)


# ---------------------------------------------------------------------------
# 1. dao gam can tuong - dagger with a human-figure hilt
# ---------------------------------------------------------------------------


def build_dagger(collection, mats):
    """The figure-hilted dagger.

    The hilt is a standing person with hands on hips and a wide skirt, which is
    how the surviving examples are modelled. Kept blocky on purpose: these were
    cast, not carved, and the originals are stylised.
    """
    made = []
    blade = [
        (0.000, 0.000), (0.021, 0.012), (0.026, 0.055), (0.019, 0.125),
        (0.008, 0.168), (0.000, 0.182),
        (-0.008, 0.168), (-0.019, 0.125), (-0.026, 0.055), (-0.021, 0.012),
    ]
    blade = [(x * M, z * M) for x, z in blade]
    made.append(prism("dao_gam_luoi", blade, 0.009 * M, mats["bronze"], collection, bevel=0.004 * M))

    # midrib
    rib = [(0.006, 0.012), (0.006, 0.150), (0.000, 0.172), (-0.006, 0.150), (-0.006, 0.012)]
    rib = [(x * M, z * M) for x, z in rib]
    made.append(prism("dao_gam_song_luoi", rib, 0.016 * M, mats["bronze"], collection))

    guard = blockout.cube(
        "dao_gam_chan", (0.0, 0.0, -0.004 * M), (0.036 * M, 0.013 * M, 0.007 * M),
        mats["bronze"], collection, bevel_width=0.003 * M,
    )
    blockout.move_to_collection(guard, collection)
    made.append(guard)

    # standing figure: skirt, torso, arms on hips, head, topknot
    figure = [
        ("vay", (0.0, 0.0, -0.034 * M), (0.036 * M, 0.020 * M, 0.030 * M), 0.007),
        ("than", (0.0, 0.0, -0.080 * M), (0.021 * M, 0.015 * M, 0.030 * M), 0.006),
        ("vai", (0.0, 0.0, -0.110 * M), (0.036 * M, 0.016 * M, 0.010 * M), 0.005),
    ]
    for label, location, scale, bevel in figure:
        obj = blockout.cube("dao_gam_tuong_" + label, location, scale, mats["bronze"], collection,
                            bevel_width=bevel * M)
        blockout.move_to_collection(obj, collection)
        made.append(obj)
    for side in (-1.0, 1.0):
        arm = blockout.cube(
            "dao_gam_tuong_tay", (side * 0.027 * M, 0.0, -0.082 * M),
            (0.009 * M, 0.010 * M, 0.028 * M), mats["bronze"], collection, bevel_width=0.003 * M,
        )
        blockout.move_to_collection(arm, collection)
        made.append(arm)
    head = blockout.sphere("dao_gam_tuong_dau", (0.0, 0.0, -0.134 * M),
                           (0.018 * M, 0.017 * M, 0.021 * M), mats["bronze"], collection, 20, 12)
    blockout.move_to_collection(head, collection)
    made.append(head)
    knot = blockout.sphere("dao_gam_tuong_bui_toc", (0.0, 0.007 * M, -0.155 * M),
                           (0.011 * M, 0.011 * M, 0.011 * M), mats["bronze"], collection, 14, 8)
    blockout.move_to_collection(knot, collection)
    made.append(knot)

    sun = ornament.sun_star("dao_gam_hoa_van", 0.013 * M, 10, 0.004 * M, collection, mats["bronze"])
    sun.rotation_euler = (math.radians(-90.0), 0.0, 0.0)
    sun.location = (0.0, -0.016 * M, -0.080 * M)
    made.append(sun)
    return made


# ---------------------------------------------------------------------------
# 2. doan kiem ri set - the rusted short sword of CH-01
# ---------------------------------------------------------------------------


def build_short_sword(collection, mats):
    """Canon: Long Nhan wakes beside this and it shatters when the axe wakes.

    So it is modelled already failing - the edge is notched away and the tip is
    gone, which is what makes it read as a temporary tool.
    """
    made = []
    blade = [
        (0.000, 0.000), (0.026, 0.020), (0.030, 0.120), (0.024, 0.230),
        (0.026, 0.290), (0.014, 0.352), (0.004, 0.366),
        (-0.011, 0.350), (-0.021, 0.286), (-0.014, 0.232),
        (-0.028, 0.176), (-0.019, 0.118), (-0.029, 0.050), (-0.024, 0.016),
    ]
    blade = [(x * M, z * M) for x, z in blade]
    made.append(prism("doan_kiem_luoi", blade, 0.008 * M, mats["corroded"], collection, bevel=0.003 * M))

    guard = blockout.cube("doan_kiem_chan_kiem", (0.0, 0.0, -0.008 * M),
                          (0.044 * M, 0.014 * M, 0.008 * M), mats["corroded"], collection,
                          bevel_width=0.004 * M)
    blockout.move_to_collection(guard, collection)
    made.append(guard)

    grip = tube("doan_kiem_can", (0.0, 0.0, -0.016 * M), (0.0, 0.0, -0.106 * M),
                0.013 * M, mats["leather"], collection)
    made.append(grip)
    made.extend(wrap_bands("doan_kiem_day_quan", (0.0, 0.0, -0.024 * M), (0.0, 0.0, -0.098 * M),
                           0.015 * M, 6, mats["cord"], collection))
    pommel = blockout.sphere("doan_kiem_chuoi", (0.0, 0.0, -0.115 * M),
                             (0.019 * M, 0.019 * M, 0.014 * M), mats["corroded"], collection, 20, 12)
    blockout.move_to_collection(pommel, collection)
    made.append(pommel)
    return made


# ---------------------------------------------------------------------------
# riu luoi xeo - the asymmetric Dong Son boot axe
# ---------------------------------------------------------------------------

# Profile of the classic riu luoi xeo: a narrow socket with the blade sweeping
# out and down to one side, so the cutting edge sits well off the haft axis.
# This asymmetry is the single most identifiable Vietnamese Bronze Age shape,
# and it is what the earlier generic slab-shaped axe head was missing.
RIU_XEO = [
    (0.033, 0.020), (0.033, -0.120), (0.012, -0.160), (-0.030, -0.205),
    (-0.070, -0.268), (-0.098, -0.340), (-0.170, -0.330), (-0.232, -0.288),
    (-0.262, -0.220), (-0.228, -0.196), (-0.160, -0.166), (-0.092, -0.120),
    (-0.044, -0.070), (-0.033, -0.030), (-0.033, 0.020),
]


def build_axe(collection, mats, name, scale, haft_length, hero=False):
    made = []
    outline = [(x * scale * M, z * scale * M) for x, z in RIU_XEO]
    head_material = mats["bronze"] if not hero else mats["bronze_dark"]
    head = prism(name + "_luoi", outline, 0.022 * scale * M, head_material, collection,
                 bevel=0.009 * scale * M)
    made.append(head)

    socket = blockout.cylinder(name + "_hong_riu", (0.0, 0.0, -0.048 * scale * M),
                               0.036 * scale * M, 0.150 * scale * M, mats["bronze"], collection, 18)
    blockout.move_to_collection(socket, collection)
    made.append(socket)

    haft = tube(name + "_can", (0.0, 0.0, 0.012 * scale * M),
                (0.0, 0.0, -haft_length * M), 0.017 * M, mats["wood"], collection)
    made.append(haft)
    made.extend(wrap_bands(name + "_day_quan", (0.0, 0.0, -0.10 * M), (0.0, 0.0, -0.30 * M),
                           0.019 * M, 9, mats["cord"], collection))

    # Drum motifs on the cheek of the blade, on both faces.
    for side in (-1.0, 1.0):
        sun = ornament.sun_star(name + "_mat_troi", 0.055 * scale * M, 12,
                                0.013 * scale * M, collection, mats["bronze"])
        sun.rotation_euler = (math.radians(-90.0 * side), 0.0, 0.0)
        sun.location = (-0.132 * scale * M, side * 0.011 * scale * M, -0.222 * scale * M)
        made.append(sun)

    if hero:
        # Long Khi burning along the cutting edge.
        edge = [
            (-0.098, -0.340), (-0.170, -0.330), (-0.232, -0.288), (-0.262, -0.220),
            (-0.244, -0.214), (-0.220, -0.274), (-0.164, -0.312), (-0.100, -0.320),
        ]
        edge = [(x * scale * M, z * scale * M) for x, z in edge]
        made.append(prism(name + "_than_khi", edge, 0.030 * scale * M, mats["ember"], collection))

        for index, z in enumerate((-0.16, -0.44)):
            band = blockout.torus(f"{name}_nep_dong_{index}", (0.0, 0.0, z * M),
                                  0.021 * M, 0.008 * M, mats["bronze"], collection)
            blockout.move_to_collection(band, collection)
            made.append(band)
        gem = blockout.sphere(name + "_manh_long_ngoc", (0.0, 0.0, -haft_length * M - 0.015 * M),
                              (0.030 * M, 0.030 * M, 0.038 * M), mats["jade"], collection, 24, 14)
        blockout.move_to_collection(gem, collection)
        made.append(gem)
    else:
        butt = blockout.sphere(name + "_chuoi", (0.0, 0.0, -haft_length * M),
                               (0.021 * M, 0.021 * M, 0.020 * M), mats["wood"], collection, 16, 10)
        blockout.move_to_collection(butt, collection)
        made.append(butt)
    return made


# ---------------------------------------------------------------------------
# 5. qua dong - bronze dagger-axe
# ---------------------------------------------------------------------------


def build_ge(collection, mats):
    """A qua: the blade is mounted square to the haft, edge downward.

    An infantry weapon for hooking and pulling a rider down, not for chopping.
    """
    made = []
    blade = [
        (0.018, 0.030), (0.072, 0.042), (0.152, 0.048), (0.242, 0.041),
        (0.334, 0.013), (0.250, -0.005), (0.166, -0.013), (0.096, -0.026),
        (0.050, -0.052), (0.028, -0.064), (0.018, -0.032),
    ]
    blade = [(x * M, z * M) for x, z in blade]
    made.append(prism("qua_luoi", blade, 0.010 * M, mats["bronze"], collection, bevel=0.004 * M))

    tang = blockout.cube("qua_chuoi_ngang", (0.016 * M, 0.0, 0.0),
                         (0.020 * M, 0.016 * M, 0.052 * M), mats["bronze"], collection,
                         bevel_width=0.004 * M)
    blockout.move_to_collection(tang, collection)
    made.append(tang)

    haft = tube("qua_can", (0.0, 0.0, 0.075 * M), (0.0, 0.0, -0.92 * M),
                0.017 * M, mats["wood"], collection)
    made.append(haft)
    made.extend(wrap_bands("qua_day_buoc", (0.0, 0.0, 0.040 * M), (0.0, 0.0, -0.040 * M),
                           0.020 * M, 5, mats["cord"], collection))
    cap = blockout.cylinder("qua_boc_dong", (0.0, 0.0, -0.90 * M),
                            0.020 * M, 0.055 * M, mats["bronze"], collection, 14)
    blockout.move_to_collection(cap, collection)
    made.append(cap)

    sun = ornament.sun_star("qua_hoa_van", 0.018 * M, 8, 0.004 * M, collection, mats["bronze"])
    sun.rotation_euler = (math.radians(-90.0), 0.0, 0.0)
    sun.location = (0.075 * M, 0.007 * M, 0.014 * M)
    made.append(sun)
    return made


# ---------------------------------------------------------------------------
# 6. giao dong - socketed leaf-blade spear
# ---------------------------------------------------------------------------


def build_spear(collection, mats):
    made = []
    blade = [
        (0.000, 0.000), (0.030, 0.040), (0.041, 0.120), (0.034, 0.210),
        (0.018, 0.272), (0.000, 0.300),
        (-0.018, 0.272), (-0.034, 0.210), (-0.041, 0.120), (-0.030, 0.040),
    ]
    blade = [(x * M, z * M) for x, z in blade]
    made.append(prism("giao_luoi", blade, 0.009 * M, mats["bronze"], collection, bevel=0.004 * M))

    rib = [(0.009, 0.010), (0.009, 0.240), (0.000, 0.286), (-0.009, 0.240), (-0.009, 0.010)]
    rib = [(x * M, z * M) for x, z in rib]
    made.append(prism("giao_song_luoi", rib, 0.019 * M, mats["bronze"], collection))

    socket = blockout.cylinder("giao_hong", (0.0, 0.0, -0.045 * M),
                               0.022 * M, 0.105 * M, mats["bronze"], collection, 18)
    blockout.move_to_collection(socket, collection)
    made.append(socket)

    haft = tube("giao_can", (0.0, 0.0, -0.020 * M), (0.0, 0.0, -1.80 * M),
                0.016 * M, mats["wood_pale"], collection)
    made.append(haft)
    made.extend(wrap_bands("giao_day_quan", (0.0, 0.0, -0.10 * M), (0.0, 0.0, -0.22 * M),
                           0.018 * M, 5, mats["cord"], collection))
    heel = blockout.cylinder("giao_du", (0.0, 0.0, -1.80 * M),
                             0.018 * M, 0.070 * M, mats["bronze"], collection, 14)
    blockout.move_to_collection(heel, collection)
    made.append(heel)

    circles = ornament.tangent_circles("giao_vong_tron", 0.024 * M, 7, 0.008 * M,
                                       0.003 * M, collection, mats["bronze"])
    if circles:
        circles.rotation_euler = (0.0, 0.0, 0.0)
        circles.location = (0.0, 0.0, -0.096 * M)
        made.append(circles)
    return made


# ---------------------------------------------------------------------------
# 7. no than - the crossbow of the An Duong Vuong legend
# ---------------------------------------------------------------------------


def build_crossbow(collection, mats):
    """No than. In the legend Cao Lo's crossbow loosed a thousand bolts at once
    and the kingdom fell when its trigger was stolen, so the trigger housing is
    given its own bronze casing here."""
    made = []
    stock = blockout.cube("no_bang_sung", (0.0, 0.0, -0.12 * M),
                          (0.040 * M, 0.046 * M, 0.330 * M), mats["wood"], collection,
                          bevel_width=0.012 * M)
    blockout.move_to_collection(stock, collection)
    made.append(stock)

    # bow limbs: a shallow arc swept from the stock head
    points = []
    span, depth, steps = 0.40, 0.105, 11
    for index in range(steps):
        t = index / (steps - 1)
        x = (t - 0.5) * 2.0 * span
        y = -depth * (1.0 - (2.0 * t - 1.0) ** 2) - 0.030
        points.append((x * M, y * M, 0.170 * M))
    for index in range(len(points) - 1):
        made.append(tube(f"no_canh_cung_{index}", points[index], points[index + 1],
                         (0.023 - 0.011 * abs(index / (len(points) - 2) - 0.5) * 2.0) * M,
                         mats["wood_pale"], collection, 10))

    string = tube("no_day_cung", points[0], points[-1], 0.006 * M, mats["cord"], collection, 8)
    made.append(string)

    housing = blockout.cube("no_hop_lay_co", (0.0, 0.0, -0.075 * M),
                            (0.034 * M, 0.038 * M, 0.045 * M), mats["bronze"], collection,
                            bevel_width=0.006 * M)
    blockout.move_to_collection(housing, collection)
    made.append(housing)
    trigger = blockout.cube("no_lay_co", (0.0, -0.006 * M, -0.135 * M),
                            (0.008 * M, 0.020 * M, 0.038 * M), mats["bronze"], collection,
                            bevel_width=0.004 * M)
    blockout.move_to_collection(trigger, collection)
    made.append(trigger)

    groove = blockout.cube("no_ranh_ten", (0.0, -0.026 * M, 0.030 * M),
                           (0.008 * M, 0.006 * M, 0.150 * M), mats["wood_pale"], collection,
                           bevel_width=0.002 * M)
    blockout.move_to_collection(groove, collection)
    made.append(groove)

    sun = ornament.sun_star("no_hoa_van", 0.020 * M, 10, 0.004 * M, collection, mats["bronze"])
    sun.rotation_euler = (math.radians(90.0), 0.0, 0.0)
    sun.location = (0.0, -0.042 * M, -0.075 * M)
    made.append(sun)
    return made


# ---------------------------------------------------------------------------
# 8. moc khien - round shield carrying a full drum tympanum
# ---------------------------------------------------------------------------


def build_shield(collection, mats):
    """The drum face belongs on a shield more than anywhere else: a tympanum is
    already a disc organised in concentric bands around a sun."""
    made = []
    radius = 0.280 * M
    board = blockout.cylinder("khien_van_go", (0.0, 0.0, 0.0), radius, 0.030 * M,
                              mats["wood"], collection, 64)
    board.rotation_euler = (math.radians(90.0), 0.0, 0.0)
    blockout.move_to_collection(board, collection)
    made.append(board)

    rim = blockout.torus("khien_vanh_dong", (0.0, 0.0, 0.0), radius, 0.017 * M,
                         mats["bronze"], collection)
    rim.rotation_euler = (math.radians(90.0), 0.0, 0.0)
    blockout.move_to_collection(rim, collection)
    made.append(rim)

    face = ornament.drum_face("khien_mat_trong", radius * 0.90, collection, mats["bronze"],
                              rays=14, birds=10, relief=0.0075 * M)
    if face:
        face.rotation_euler = (math.radians(-90.0), 0.0, 0.0)
        face.location = (0.0, -0.016 * M, 0.0)
        made.append(face)

    boss = blockout.sphere("khien_num_dong", (0.0, -0.020 * M, 0.0),
                           (0.042 * M, 0.030 * M, 0.042 * M), mats["bronze"], collection, 40, 24)
    blockout.move_to_collection(boss, collection)
    made.append(boss)

    grip = tube("khien_tay_cam", (-0.075 * M, 0.038 * M, 0.0), (0.075 * M, 0.038 * M, 0.0),
                0.014 * M, mats["wood"], collection)
    made.append(grip)
    return made


# ---------------------------------------------------------------------------
# assembly and contact sheet
# ---------------------------------------------------------------------------


# key, caption, builder, kwargs, display rotation for the contact sheet
WEAPONS = (
    ("dao_gam_can_tuong", "Dao gam can tuong", build_dagger, {}),
    ("doan_kiem_ri_set", "Doan kiem ri set  (CH-01)", build_short_sword, {}),
    ("riu_xeo_chien_binh", "Riu luoi xeo", build_axe,
     {"name": "riu_xeo", "scale": 0.72, "haft_length": 0.62}),
    ("riu_than_thach_son", "Riu Than Thach Son", build_axe,
     {"name": "riu_than", "scale": 1.15, "haft_length": 0.98, "hero": True}),
    ("qua_dong", "Qua dong", build_ge, {}),
    ("giao_dong", "Giao dong", build_spear, {}),
    ("no_than", "No than", build_crossbow, {}, (math.radians(-58.0), 0.0, 0.0)),
    ("moc_khien", "Moc khien", build_shield, {}),
)


def label(text, location, collection, mat, size):
    bpy.ops.object.text_add(location=location)
    obj = bpy.context.object
    obj.data.body = text
    obj.data.align_x = "CENTER"
    obj.data.size = size
    obj.data.extrude = 0.004 * M
    obj.rotation_euler = (math.radians(90.0), 0.0, 0.0)
    obj.data.materials.append(mat)
    blockout.move_to_collection(obj, collection)
    return obj


def setup_scene(sheet, mats, width, centre_z):
    scene = bpy.context.scene
    scene.render.engine = "BLENDER_EEVEE_NEXT"
    scene.render.resolution_x = 2200
    scene.render.resolution_y = 1300
    scene.render.image_settings.file_format = "PNG"
    scene.render.filepath = str(OUT_DIR / "dong_son_weapons_sheet.png")
    scene.eevee.taa_render_samples = 160
    for attribute, value in (("use_raytracing", True), ("use_shadows", True)):
        if hasattr(scene.eevee, attribute):
            setattr(scene.eevee, attribute, value)
    scene.view_settings.view_transform = "AgX"
    try:
        scene.view_settings.look = "AgX - Medium High Contrast"
    except Exception:
        pass
    scene.world.use_nodes = True
    background = scene.world.node_tree.nodes.get("Background")
    background.inputs["Color"].default_value = (0.016, 0.018, 0.024, 1.0)
    background.inputs["Strength"].default_value = 0.75

    def area(name, location, energy, color, size, target):
        data = bpy.data.lights.new(name, "AREA")
        data.energy = energy
        data.color = color
        data.shape = "DISK"
        data.size = size
        obj = bpy.data.objects.new(name, data)
        sheet.objects.link(obj)
        obj.location = location
        blockout.look_at(obj, target)
        return obj

    aim = (0.0, 0.0, centre_z)
    area("key", (-3.0 * M, -3.4 * M, centre_z + 2.0 * M), 11000, (1.0, 0.88, 0.74), 3.2 * M, aim)
    area("fill", (3.2 * M, -2.8 * M, centre_z), 3200, (0.60, 0.72, 0.94), 3.6 * M, aim)
    area("rim", (1.2 * M, 3.0 * M, centre_z + 1.4 * M), 8000, (0.20, 0.80, 0.84), 2.2 * M, aim)
    area("ember", (-2.4 * M, 2.2 * M, centre_z - 0.8 * M), 3000, (1.0, 0.32, 0.09), 1.8 * M, aim)

    data = bpy.data.cameras.new("sheet_camera")
    camera = bpy.data.objects.new("sheet_camera", data)
    sheet.objects.link(camera)
    data.type = "ORTHO"
    data.ortho_scale = width
    camera.location = (0.0, -6.0 * M, centre_z)
    blockout.look_at(camera, (0.0, 0.0, centre_z))
    scene.camera = camera

    scene.use_nodes = True
    nodes, links = scene.node_tree.nodes, scene.node_tree.links
    nodes.clear()
    layers = nodes.new("CompositorNodeRLayers")
    glare = nodes.new("CompositorNodeGlare")
    glare.glare_type = "FOG_GLOW"
    glare.quality = "HIGH"
    glare.threshold = 1.6
    glare.size = 7
    glare.mix = -0.92
    composite = nodes.new("CompositorNodeComposite")
    links.new(layers.outputs["Image"], glare.inputs["Image"])
    links.new(glare.outputs["Image"], composite.inputs["Image"])


def build():
    blockout.clear_scene()
    mats = make_materials()
    sheet = blockout.make_collection("CONTACT_SHEET")

    spacing = 0.62 * M
    start = -(len(WEAPONS) - 1) / 2.0 * spacing
    collections = {}
    tallest = 0.0
    for index, entry in enumerate(WEAPONS):
        key, caption, builder, kwargs = entry[:4]
        display_rotation = entry[4] if len(entry) > 4 else None
        collection = blockout.make_collection(key.upper())
        collections[key] = collection
        made = builder(collection, mats, **kwargs)

        roots = [obj for obj in made if obj and obj.parent is None]
        if display_rotation:
            pivot = bpy.data.objects.new(key + "_display", None)
            collection.objects.link(pivot)
            for obj in roots:
                obj.parent = pivot
                obj.matrix_parent_inverse = pivot.matrix_world.inverted()
            pivot.rotation_euler = display_rotation
            bpy.context.view_layer.update()
            roots = [pivot]
        offset = Vector((start + index * spacing, 0.0, 0.0))
        measured = [obj for obj in made if obj and obj.type == "MESH"]
        bpy.context.view_layer.update()
        lowest = min(
            (obj.matrix_world @ Vector(corner)).z
            for obj in measured for corner in obj.bound_box
        )
        offset.z = -lowest + 0.06 * M
        for obj in roots:
            obj.location = Vector(obj.location) + offset
        highest = max(
            (obj.matrix_world @ Vector(corner)).z
            for obj in measured for corner in obj.bound_box
        )
        # matrix_world is stale straight after moving the objects, so the top
        # is derived from the pre-move span rather than re-read.
        tallest = max(tallest, highest - lowest + 0.06 * M)
        base, top = 0.06 * M, highest - lowest + 0.06 * M
        collections[key] = (offset.x, base, top)
        label(caption, (offset.x, -0.35 * M, 0.012 * M), sheet, mats["red"], 0.042 * M)
        print("WEAPON %-20s parts=%d" % (key, len(made)))

    width = spacing * (len(WEAPONS) + 0.6)
    centre_z = tallest / 2.0
    setup_scene(sheet, mats, width, centre_z)

    bpy.context.scene["project"] = "Huyet Mach Lac Long"
    bpy.context.scene["asset_scope"] = "Dong Son weapon set"
    bpy.context.scene["units_per_metre"] = M
    bpy.ops.wm.save_as_mainfile(filepath=str(OUT_DIR / "dong_son_weapons.blend"))
    bpy.ops.render.render(write_still=True)

    # Close-ups. The motifs that carry the Dong Son reading are all a few
    # centimetres across and none of them survive at contact-sheet scale.
    scene = bpy.context.scene
    camera = scene.camera
    details = (
        ("chi_tiet_can_tuong", "dao_gam_can_tuong", 0.22, 0.40),
        ("chi_tiet_mat_trong", "moc_khien", 0.50, 0.66),
        ("chi_tiet_luoi_riu", "riu_than_thach_son", 0.87, 0.90),
    )
    scene.render.resolution_x = 1100
    scene.render.resolution_y = 1100
    for name, key, fraction, scale in details:
        x, base, top = collections[key]
        z = base + (top - base) * fraction
        camera.data.ortho_scale = scale * M
        camera.location = (x, -6.0 * M, z)
        blockout.look_at(camera, (x, 0.0, z))
        scene.render.filepath = str(OUT_DIR / (name + ".png"))
        bpy.ops.render.render(write_still=True)
        print("DETAIL %-22s x=%.2f z=%.2f" % (name, x, z))

    print("WEAPONS_BUILD objects=%d" % len(bpy.context.scene.objects))


if __name__ == "__main__":
    build()
