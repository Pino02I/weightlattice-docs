# Troubleshooting

## No lattice is created

Check that:

- The active object is a mesh.
- You are in Weight Paint mode.
- There is an active vertex group.
- At least one vertex has weight above the threshold.

Tip: use **Alt+F** to quickly fill the active group at weight 1.0 if you want every vertex to be considered.

## The lattice does not update

Make sure the mesh still has a lattice modifier linked to the active vertex group. Press **Enter** to recreate or update the cage, or press **U** to refit only the bounding box.

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
