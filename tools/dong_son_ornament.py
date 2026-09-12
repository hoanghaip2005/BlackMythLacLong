"""Dong Son ornament vocabulary.

The decorative language of the Dong Son bronze drums, built as real relief
geometry rather than painted on. Everything here is drawn from the documented
motif set: the many-rayed sun at the drum's centre, concentric bands of
tangent circles, saw-tooth and dotted bands, rope twist, and the ring of Lac
birds flying anticlockwise.

Deliberately excluded: Chinese cloud scrolls, dragons, imperial and hanfu
motifs, and anything Japanese. Those are the borrowings this project keeps
being at risk of and they are not Dong Son.

Every function draws in the XY plane, raised along +Z, so a motif can be laid
onto any flat face by parenting it to an object with the right transform.
"""

import math

import bpy
from mathutils import Vector


def _mesh_from_outline(name, outline, height, collection, mat, base_z=0.0):
    """Extrude a closed 2D outline (list of (x, y)) upward into a prism."""
    count = len(outline)
    verts = [(x, y, base_z) for x, y in outline]
    verts += [(x, y, base_z + height) for x, y in outline]
    faces = [tuple(reversed(range(count))), tuple(range(count, count * 2))]
    for index in range(count):
        nxt = (index + 1) % count
        faces.append((index, nxt, nxt + count, index + count))
    mesh = bpy.data.meshes.new(name + "_mesh")
    mesh.from_pydata(verts, [], faces)
    mesh.update()
    obj = bpy.data.objects.new(name, mesh)
    collection.objects.link(obj)
    if mat:
        obj.data.materials.append(mat)
    return obj


def _join(name, objects, collection):
    """Merge a set of relief pieces into one object to keep scenes tidy."""
    objects = [o for o in objects if o is not None]
    if not objects:
        return None
    bpy.ops.object.select_all(action="DESELECT")
    for obj in objects:
        obj.select_set(True)
    bpy.context.view_layer.objects.active = objects[0]
    if len(objects) > 1:
        bpy.ops.object.join()
    merged = bpy.context.view_layer.objects.active
    merged.name = name
    return merged


# ---------------------------------------------------------------------------
# individual motifs
# ---------------------------------------------------------------------------


def sun_star(name, radius, rays, height, collection, mat, inner=0.42):
    """The many-rayed sun at the centre of a drum face.

    Real drums carry 8, 10, 12, 14 or 16 rays; 12 and 14 are the most common.
    """
    outline = []
    for index in range(rays * 2):
        angle = math.pi / 2.0 + 2.0 * math.pi * index / (rays * 2)
        r = radius if index % 2 == 0 else radius * inner
        outline.append((math.cos(angle) * r, math.sin(angle) * r))
    return _mesh_from_outline(name, outline, height, collection, mat)


def dot_band(name, radius, count, dot_radius, height, collection, mat, segments=8):
    """A ring of raised dots. The simplest of the drum's filler bands."""
    pieces = []
    for index in range(count):
        angle = 2.0 * math.pi * index / count
        outline = [
            (
                radius * math.cos(angle) + dot_radius * math.cos(a),
                radius * math.sin(angle) + dot_radius * math.sin(a),
            )
            for a in [2.0 * math.pi * s / segments for s in range(segments)]
        ]
        pieces.append(_mesh_from_outline(f"{name}_{index}", outline, height, collection, mat))
    return _join(name, pieces, collection)


def saw_tooth_band(name, radius, count, depth, height, collection, mat):
    """Hoa van rang cua - the saw-tooth band."""
    outline = []
    for index in range(count):
        base = 2.0 * math.pi * index / count
        step = 2.0 * math.pi / count
        for angle, r in (
            (base, radius),
            (base + step * 0.5, radius + depth),
            (base + step, radius),
        ):
            outline.append((math.cos(angle) * r, math.sin(angle) * r))
    inner = radius - depth * 0.35
    for index in reversed(range(count * 3)):
        angle = 2.0 * math.pi * index / (count * 3)
        outline.append((math.cos(angle) * inner, math.sin(angle) * inner))
    return _mesh_from_outline(name, outline, height, collection, mat)


def tangent_circles(name, radius, count, circle_radius, height, collection, mat, segments=14):
    """Vong tron tiep tuyen - circles joined by their tangents.

    One of the most recognisable Dong Son bands, and one that is almost never
    reproduced correctly: the circles must touch, with the connecting line
    running tangent to both, not merely sit side by side.
    """
    pieces = []
    for index in range(count):
        angle = 2.0 * math.pi * index / count
        centre = Vector((math.cos(angle) * radius, math.sin(angle) * radius))
        ring = []
        for step in range(segments):
            a = 2.0 * math.pi * step / segments
            ring.append((centre.x + circle_radius * math.cos(a), centre.y + circle_radius * math.sin(a)))
        pieces.append(_mesh_from_outline(f"{name}_c{index}", ring, height, collection, mat))

        nxt = 2.0 * math.pi * (index + 1) / count
        other = Vector((math.cos(nxt) * radius, math.sin(nxt) * radius))
        span = other - centre
        if span.length < 1e-6:
            continue
        normal = Vector((-span.y, span.x)).normalized() * (circle_radius * 0.18)
        bar = [
            (centre.x + normal.x, centre.y + normal.y),
            (other.x + normal.x, other.y + normal.y),
            (other.x - normal.x, other.y - normal.y),
            (centre.x - normal.x, centre.y - normal.y),
        ]
        pieces.append(_mesh_from_outline(f"{name}_t{index}", bar, height * 0.7, collection, mat))
    return _join(name, pieces, collection)


# Chim Lac: long beak, raised wing, trailing tail plumes, legs tucked back.
# Drawn nose-to-tail along +X, flying anticlockwise on the drum face.
LAC_BIRD = [
    (-0.52, 0.02),
    (-0.34, -0.04),
    (-0.10, -0.09),
    (0.14, -0.08),
    (0.20, -0.26),
    (0.27, -0.26),
    (0.26, -0.06),
    (0.42, 0.00),
    (0.50, 0.09),
    (0.92, 0.11),
    (0.50, 0.19),
    (0.40, 0.30),
    (0.18, 0.20),
    (0.00, 0.42),
    (-0.20, 0.20),
    (-0.38, 0.24),
]


def lac_bird_ring(name, radius, count, scale, height, collection, mat):
    """Chim Lac flying anticlockwise, the signature band of a drum face."""
    pieces = []
    for index in range(count):
        angle = 2.0 * math.pi * index / count
        # tangent direction, so each bird faces the way it flies
        forward = Vector((-math.sin(angle), math.cos(angle)))
        side = Vector((-forward.y, forward.x))
        centre = Vector((math.cos(angle) * radius, math.sin(angle) * radius))
        outline = [
            (
                centre.x + (forward.x * x + side.x * y) * scale,
                centre.y + (forward.y * x + side.y * y) * scale,
            )
            for x, y in LAC_BIRD
        ]
        pieces.append(_mesh_from_outline(f"{name}_{index}", outline, height, collection, mat))
    return _join(name, pieces, collection)


def rope_twist(name, radius, minor, collection, mat, strands=48):
    """Thung ben - the braided rope that edges many drum panels."""
    bpy.ops.mesh.primitive_torus_add(
        major_radius=radius, minor_radius=minor,
        major_segments=strands, minor_segments=6, location=(0.0, 0.0, 0.0),
    )
    obj = bpy.context.object
    obj.name = name
    if mat:
        obj.data.materials.append(mat)
    for collection_ref in list(obj.users_collection):
        collection_ref.objects.unlink(obj)
    collection.objects.link(obj)
    modifier = obj.modifiers.new("braid", "SIMPLE_DEFORM")
    modifier.deform_method = "TWIST"
    modifier.angle = math.radians(360.0)
    return obj


# ---------------------------------------------------------------------------
# the complete drum face
# ---------------------------------------------------------------------------


def drum_face(name, radius, collection, mat, rays=14, birds=10, relief=0.012):
    """A full drum tympanum: sun, then concentric bands worked outward.

    The band order follows real drums - sun at the centre, geometric filler
    bands, then the figurative bird ring nearer the rim.
    """
    pieces = [
        sun_star(name + "_sun", radius * 0.30, rays, relief * 1.6, collection, mat),
        dot_band(name + "_dots_inner", radius * 0.40, 28, radius * 0.020, relief, collection, mat),
        saw_tooth_band(name + "_teeth", radius * 0.50, 24, radius * 0.045, relief, collection, mat),
        tangent_circles(name + "_circles", radius * 0.63, 12, radius * 0.055, relief, collection, mat),
        lac_bird_ring(name + "_birds", radius * 0.80, birds, radius * 0.20, relief * 1.3, collection, mat),
        dot_band(name + "_dots_outer", radius * 0.94, 40, radius * 0.016, relief, collection, mat),
    ]
    return _join(name, pieces, collection)
