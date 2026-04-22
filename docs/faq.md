# FAQ

## Can I use an existing vertex group?

Yes. WeightLattice works with the active vertex group, whether you created it manually or with the addon.

## Can I build a lattice from Edit Mode selection?

Yes. Use **Lattice from Selection** in the Edit Mesh N-panel. The cage is built around the selected vertices, edges, or faces.

## Can I share a single cage between multiple meshes?

Yes. WeightLattice supports two shared-cage cases:

- In **Object Mode**, select more than one mesh and run **New Weight Lattice**. A single cage that encloses every selected mesh is created, each mesh receives a lattice modifier, and the view switches directly to Edit Lattice. No vertex group is generated in this case.
- In **Edit Mesh** with multi-object edit, select vertices across several meshes and run **Lattice from Selection**. A shared cage is built around those vertices and every mesh gets its own vertex group at weight 1.0 on the selected vertices.

## How do I fill the whole vertex group at weight 1.0?

Press **Alt+F** in Weight Paint. Every vertex of the active group is filled at 1.0. This is useful when you want the whole mesh, or the whole selection, to be influenced uniformly by the lattice.

## How do I switch between Weight Paint and Edit Lattice?

Press **Q** in either mode to jump to the matching side of the workflow. **Q** replaces the older `W` binding used in internal builds.

## Can I go back from lattice editing to weight painting?

Yes. Press **Q** in Edit Lattice or use the **Back to Weight Paint** button.

## Can I remove the lattice without applying the deformation?

Yes. Press **ESC** in Edit Lattice or use the **Remove** button. The lattice is removed from every mesh that referenced it.

## Can I edit the lattice resolution later?

Yes. The Edit Lattice N-panel exposes resolution (U, V, W), interpolation and modifier settings. **Numpad +/−** increase or decrease resolution on all axes at once.

## Does Apply affect every mesh that uses the shared cage?

Yes. **Apply** bakes the deformation into every mesh that references the active lattice. **Remove** likewise clears the modifier from every mesh.

## How do I refit the lattice after painting more weight?

Press **U** in Weight Paint. The bounding box is recomputed against the current weights and the cage is reset to its rest shape, so the new pass does not inherit the deformation of the previous one. Pressing **Enter** instead only opens the existing cage in Edit Lattice — it never refits on its own, to avoid overwriting a shape you have already sculpted.

## Does moving the Strength slider affect all meshes in a shared cage?

Yes. When a cage is shared across multiple meshes, the **Strength** slider is propagated to every lattice modifier bound to that cage, so a single change updates the whole group of meshes in real time.

## Why does Ctrl+Z after Apply take more than one press?

To stay stable on every supported Blender version, Apply is recorded as a sequence of undo entries rather than a single atomic step. A full rollback may therefore take two or three **Ctrl+Z** presses: first the cage reappears, then the lattice modifier is restored on each mesh. The final state is exactly the one that was in place before Apply.

## Is the addon intended for technical artists?

Yes. It is built for practical deformation workflows and fits both artist-friendly and technical setups.
