# Troubleshooting

## Enter does not create a lattice

- Make sure the **WeightLattice vertex group is active** and has painted weights above the threshold (default 0.001).
- The status line must be visible at the top of the viewport — if it is not, no session is active: start from **New Weight Lattice** or **Create / Open Lattice** in the panel.

## The cage does not follow my new painting

Press `U` (Refit) in Weight Paint: the bounding cage is recalculated from the current weights.

## The mesh does not move when I edit the cage

- Check the modifier **Strength** (a value of 0 disables the deformation).
- Check that the Lattice modifier is still on the mesh and its vertex group is set.

## Leftover vertex groups

If lattices were deleted manually, use **Clean Orphan Weights** in the Object Mode panel to remove WeightLattice groups that no longer have a cage.

## Shortcuts do not respond

- They are only active during a session (status line visible).
- If you rebound keys, check **Preferences > Add-ons > WeightLattice > Shortcuts** and use **Reset All** if needed.

## Installation fails

- WeightLattice requires **Blender 4.2 or newer** — the extension format is not supported in 4.1 and older.
- Install the `.zip` directly; do not unzip it first.

## Still stuck?

Contact the author through the Superhive product page with your Blender version and a description of the issue.
