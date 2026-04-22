# Interface

WeightLattice exposes its tools through a dedicated sidebar panel and through the right-click context menus of the 3D Viewport. The panel adapts to the active mode, so the same **WeightLattice** tab covers the full creation and editing cycle.

## Object Mode

In Object Mode the sidebar panel exposes the entry point used to start a new lattice on the active mesh. Existing WeightLattice modifiers on the object are listed below with quick access to their strength slider.

![WeightLattice panel in Object Mode](./_static/images/ui_object_mode.png)

The same entry is available from the right-click context menu of the 3D Viewport.

![Object Mode right-click menu](./_static/images/finestra_tastDX.png)

## Weight Paint

During Weight Paint the panel shows the active vertex group and tracks whether a lattice already exists for it. The main button creates or updates the cage, a secondary button jumps to Edit Lattice, and a compact shortcut box recalls every key used during painting.

![WeightLattice panel in Weight Paint](./_static/images/ui_weight_paint.png)

## Edit Lattice

In Edit Lattice the panel drives the cage itself: resolution on U, V, W, interpolation per axis, and the linked modifier's strength and visibility. The bottom section contains the **Apply**, **Remove**, **Properties**, and **Back to Weight Paint** operators used to close the workflow.

When the cage is shared across multiple meshes (see Multi-mesh workflows), the **Strength** slider is propagated to every lattice modifier bound to the cage: moving the slider once updates all linked meshes in real time.

![WeightLattice panel in Edit Lattice](./_static/images/ui_edit_mode.png)

The same actions are reachable from the right-click context menu of the lattice.

![Edit Lattice right-click menu](./_static/images/finestra_tastDX_edit_mode.png)
