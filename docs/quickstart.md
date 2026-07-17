# Quick Start

Your first deformation in five steps.

## 1. Create a new Weight Lattice

Select a mesh in Object Mode, open the sidebar (`N`), go to the **WeightLattice** tab and click **New Weight Lattice**. Blender switches to Weight Paint with a fresh vertex group active.

```{image} _static/images/quickstart_01_new_weight_lattice.png
:alt: New Weight Lattice button in the Object Mode sidebar
:width: 100%
```

## 2. Paint the area to deform

Paint the region you want to control. Use `B` for the draw brush, `L` / `R` for linear / radial gradients, `Ctrl+Scroll` to adjust the brush weight.

```{image} _static/images/quickstart_02_paint.png
:alt: Painting weights on the region to deform
:width: 100%
```

## 3. Press Enter — the cage appears

A lattice cage is generated around the weighted region, already linked to the mesh through a Lattice modifier, and Blender switches to Edit Lattice.

```{image} _static/images/quickstart_03_cage_created.png
:alt: Lattice cage generated around the painted region
:width: 100%
```

## 4. Reshape the cage

Move, rotate or scale the lattice control points. The mesh follows in real time. Adjust the resolution (U/V/W) and interpolation from the N-panel if you need more control points.

```{image} _static/images/quickstart_04_reshape.png
:alt: Reshaping the lattice cage in Edit Lattice
:width: 100%
```

## 5. Press Enter to apply

The deformation is baked into the mesh and the helper objects are cleaned up. Press `ESC` instead to remove the lattice without applying.

```{image} _static/images/quickstart_05_applied.png
:alt: Final result after applying the lattice
:width: 100%
```

That's the whole loop: **paint, Enter, reshape, Enter.**

Next: read the [Workflow](workflow.md) page for refitting, multi-mesh cages and the Edit Mesh tools.
