# CH-01 State and Handoff

## Initial state

```yaml
chapter: CH-01
location: seabed_stone_egg
weapon: rusted_short_sword
long_ngoc: []
variables:
  memory_recovered: 0
  mercy_marks: 0
  tribal_trust: 0
  dragon_hunger: 0
  relics_purified: 0
flags:
  - CH01_STARTED
  - LONG_NHAN_UNNAMED
boss_fates: {}
final_decision: null
```

## Required flags

| Flag | Set at | Meaning |
|---|---|---|
| `CH01_STARTED` | S01 | Chapter started |
| `LONG_NHAN_UNNAMED` | S01 | Player identity remains unresolved |
| `CH01_LINH_RESCUED` | S03 | Linh was freed by player |
| `CH01_LINH_ABANDONED` | S03 | Player chose the current trail over Linh |
| `CH01_GLYPHS_READ_1` | S04 | First glyph understood |
| `CH01_GLYPHS_READ_2` | S04 | Second glyph understood |
| `CH01_GLYPHS_READ_3` | S04 | Third glyph understood |
| `CH01_BOSS_NAMED_WOUND` | S05 | Player recognized abandonment |
| `CH01_BOSS_CONDEMNED` | S05 | Player condemned the harm first |
| `CH01_BOSS_HEARD` | S05 | Player stayed silent and observed |
| `CH01_BOSS_LISTENED` | S05 | Full pre-boss memory was heard |
| `CH01_ANCHOR_1_ACTIVE` | B01 | First promise anchor activated |
| `CH01_ANCHOR_2_ACTIVE` | B01 | Second promise anchor activated |
| `CH01_ANCHOR_3_ACTIVE` | B01 | Third promise anchor activated |
| `Q_CH01_002_COMPLETE` | Optional | Three bells restored |
| `Q_CH01_003_COMPLETE` | S07 | Bond requirement completed |
| `CH01_END_RELEASED` | S07 | Ngư Tinh released |
| `CH01_END_FORCE` | S07 | Ngư Tinh defeated by force |
| `CH01_END_ABSORBED` | S07 | Ngư Tinh essence absorbed |
| `CH01_COMPLETE` | S08 | Chapter complete |

## State transition matrix

| Event | Variables | Flags | Player-facing feedback |
|---|---|---|---|
| Take rusted sword | none | `WEAPON_SHORT_SWORD` | Moveset opens; sword visibly damaged |
| Rescue Linh | `tribal_trust +1` | `CH01_LINH_RESCUED` | Lamp stays lit, dialogue support |
| Abandon Linh | none initially | `CH01_LINH_ABANDONED` | Lamp goes dark, later warning absent |
| Read 3 glyphs | none | `CH01_GLYPHS_READ_3` | Bond clue becomes legible |
| Confirm the empty seal mark | none | `TRUTH_SEAL_WAS_NEVER_BROKEN` | The third glyph shows an absence, not a broken lock |
| Break promise tablet | `dragon_hunger +1` | `CH01_TABLET_BROKEN` | Shortcut opens; glyph route lost |
| Use Thủy Ảnh in S06 | none | `SPELL_THUY_ANH_AWAKENED` | First perfect-dodge water burst |
| Activate anchor | none | `CH01_ANCHOR_*` | Bell/memory/arena safe region |
| Release boss | `memory_recovered +1`, `mercy_marks +1`, `relics_purified +1` | `CH01_END_RELEASED` | Warm light, clear water |
| Leave essence untouched | none | `CH01_END_FORCE` | Broken memory, cold light |
| Absorb essence | `dragon_hunger +1` | `CH01_END_ABSORBED` | Black current under skin |
| Chapter exit | none | `CH01_COMPLETE`, `LG01_ACQUIRED` | CH-02 hook becomes available |

## State invariants

- `LG-01` is acquired exactly once.
- Only one of `CH01_END_RELEASED`, `CH01_END_FORCE`, `CH01_END_ABSORBED` may be true.
- `CH01_END_RELEASED` implies all three anchor flags; it never appears from dialogue alone.
- `memory_recovered` increases at most once in CH-01.
- `relics_purified` increases only on release, never on force or absorption.
- Rìu Thần Thạch Sơn is unavailable before `CH01_COMPLETE`.
- `dragon_hunger` cannot decrease during CH-01.
- `TRUTH_SEAL_WAS_NEVER_BROKEN` is a clue/flag after CH-01, not a complete global proof until CH-06.

## Handoff: gameplay

### Required experience

- Third-person underwater traversal.
- Basic attack and dodge before S02.
- A readable perfect-dodge window for `Thủy Ảnh` in S06/B01.
- Three stance hooks, introduced contextually:
  - `Thế Trảm`: clear clustered mutated fish.
  - `Thế Đột`: punish exposed tail scar.
  - `Thế Ngự`: answer tail sweep and observe boss pause.
- Arena with three promise anchors and changing safe zones.
- Boss must support a non-release victory path and a release path.

### Explicitly deferred

- Damage, health, stamina and resource numbers.
- Hitbox/frame data.
- Save serialization implementation.
- Exact movement controller and swimming technology.

## Handoff: art

- Stone egg with dragon-scale seams, not a generic fantasy egg.
- Dead coral that communicates sickness without relying only on black color.
- Submerged temple with three readable promise glyphs.
- Linh's shell lamp as a persistent state prop: lit, flickering, extinguished.
- Ngư Tinh silhouette first, body reveal later; fire tail contrasts with cold deep sea.
- Long Ngọc appears as memory material, not a generic loot gem.
- Rìu Thần Thạch Sơn emergence after boss fate.

## Handoff: audio

- Low-pressure underwater bed with gaps for dialogue.
- Three bell language: travel, return, no-return.
- Distinct sound for water depression before whirlpool.
- Tail fire sounds wet/pressurized, not ordinary campfire.
- Boss voice arrives with delayed reverb, but key words remain intelligible.
- Release: water clears, bells resolve.
- Absorption: low pulse under the dialogue, never a loud “evil sting”.

## Handoff: localization

- Keep `Long Nhân`, `Long Ngọc`, `Long Khí`, `Ngư Tinh`, `Thủy Ảnh`, `Rìu Thần Thạch Sơn` in glossary.
- Preserve distinction between “bị bỏ lại” and “bị ruồng bỏ”; they become different themes later.
- Do not translate `Thủy tộc` as a generic “water monsters” faction.
- Keep dialogue lines short enough for combat subtitles; long reveal lines need cinematic subtitle budget.
