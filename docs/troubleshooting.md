# Troubleshooting

## No lattice is created

Check that:

- The active object is a mesh.
- You are in Weight Paint mode.
- There is an active vertex group.
- At least one vertex has weight above the threshold.

Tip: use **Alt+F** to quickly fill the active group at weight 1.0 if you want every vertex to be considered.

## The lattice does not update after repainting

This is by design. Pressing **Enter** on a vertex group that already has a lattice opens the existing cage in Edit Lattice without altering it, so a shape you have already sculpted is never lost by accident.

To recompute the bounding box against the current weights, press **U** in Weight Paint. Refit also resets the control points to their rest positions, so the new cage starts clean.

## The lattice cannot be applied

Make sure the active object is the lattice and that every mesh it controls still exists. Apply propagates to every mesh that references the same cage.

## Q does not switch modes

**Q** is mapped by the addon for Weight Paint ↔ Edit Lattice. If the shortcut is inactive:

- Confirm the addon is enabled.
- Confirm you are in Weight Paint on a mesh with a WeightLattice group, or in Edit Lattice on a WeightLattice cage.
- Check that no other addon is consuming **Q** in the same keymap.

Older internal builds used `W` for this action; v1.0.0 uses `Q`.

## Alt+F does not fill

**Alt+F** is the Fill shortcut in Weight Paint. Make sure the active vertex group is selected and that the mesh has a valid WeightLattice group. Plain **F** is reserved for Blender's brush-size shortcut.

## The brush does not activate

Some Blender versions handle tool activation differently. If needed, open the standard brush tools manually and retry.

## The addon panel does not appear

Check that the addon is enabled and that you are in a supported mode for the relevant panel (Object Mode, Weight Paint, Edit Mesh, or Edit Lattice).

## The deformation is too weak

Increase the lattice modifier strength in the Edit Lattice panel or in the addon preferences.

## The bounding box is too tight

Increase the **Padding** value in the addon preferences before generating the lattice again.

## The shared cage does not cover every mesh

For a shared cage, select all the target meshes in Object Mode (or enter multi-object Edit Mesh and select the relevant vertices) before running the command. If a mesh is added later, run the command again to rebuild the cage.

## Ctrl+Z after Apply takes more than one press

Apply performs several actions in sequence: baking the deformation into each mesh that uses the cage, cleaning the related vertex group when appropriate, and removing the lattice object. To stay stable on the broadest range of Blender versions, WeightLattice records each of these as its own undo entry instead of one atomic step, so a full rollback may take two or three **Ctrl+Z** presses.
