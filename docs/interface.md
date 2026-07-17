# Interface

WeightLattice lives in the 3D Viewport sidebar (`N` > **WeightLattice** tab). The panel changes with the mode.

```{image} _static/images/panel_object_mode.png
:alt: The WeightLattice tab in the 3D Viewport sidebar
:width: 100%
```

## Object Mode panel

Create new lattices and manage existing ones: **New Weight Lattice**, the list of the mesh's lattices with per-lattice Strength, **Apply / Remove**, **Apply All / Remove All**, the **All Lattices On/Off** preview toggle and **Clean Orphan Weights**.

```{image} _static/images/sidebar_object_mode.png
:alt: WeightLattice panel in Object Mode
:width: 45%
```

With no lattice on the mesh only **New Weight Lattice** is active; with several lattices, each one gets its own entry and Strength slider:

```{image} _static/images/sidebar_object_mode_multi.png
:alt: Object Mode panel with multiple lattices
:width: 45%
```

## Weight Paint panel

The active group and whether it already has a cage, the Strength slider, **Create / Open Lattice [Enter]**, navigation buttons and **Select Weighted Verts**.

```{image} _static/images/sidebar_weight_paint.png
:alt: WeightLattice panel in Weight Paint
:width: 45%
```

## Edit Lattice panel

Modifier Strength and **Show in Edit Mode**, lattice **Resolution** (U/V/W), **Interpolation**, navigation, **Apply [Enter]**, **Remove [ESC]** and **Properties [Alt+C]**.

```{image} _static/images/sidebar_edit_lattice.png
:alt: WeightLattice panel in Edit Lattice
:width: 45%
```

## Edit Mesh panel

Active lattice and group info, **Add / Remove Selected**, **Select Weighted Verts**, navigation, and **Lattice from Selection** to build a cage straight from the mesh selection.

```{image} _static/images/sidebar_edit_mesh.png
:alt: WeightLattice panel in Edit Mesh
:width: 45%
```

The `Alt+C` popup groups the same controls in a floating dialog, handy when the sidebar is closed:

```{image} _static/images/popup_properties_edit_mesh.png
:alt: Edit Mesh properties popup (Alt+C)
:width: 55%
```

## Right-click menus

The most-used actions are also in the context menus: **New Weight Lattice** in Object Mode; Add/Remove/Select and **WeightLattice from Selection** in Edit Mesh; Apply/Remove/Properties in Edit Lattice.

```{image} _static/images/menu_edit_lattice.png
:alt: WeightLattice entries in the Edit Lattice right-click menu
:width: 45%
```

```{image} _static/images/context_menus.png
:alt: WeightLattice entries in the right-click menu, in context
:width: 100%
```

## Status line

While a session is active, a one-line reminder of the available keys is drawn at the top of the viewport — one per mode:

```{image} _static/images/overlay_status_weight_paint.png
:alt: Status line in Weight Paint
:width: 100%
```

```{image} _static/images/overlay_status_edit_lattice.png
:alt: Status line in Edit Lattice
:width: 100%
```

```{image} _static/images/overlay_status_edit_mesh.png
:alt: Status line in Edit Mesh
:width: 100%
```
