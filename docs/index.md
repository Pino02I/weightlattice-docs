# WeightLattice

**Paint. Press Enter. Reshape. Apply.**

WeightLattice is a Blender addon that turns a painted vertex group into a lattice cage in one keystroke. It replaces the manual lattice setup — create lattice, scale, position, add modifier, assign vertex group — with a four-step workflow driven entirely from the viewport.

```{image} _static/images/hero.png
:alt: WeightLattice in action
:width: 100%
```

## How it works

1. Select a mesh and click **New Weight Lattice**.
2. Paint the area you want to deform in Weight Paint.
3. Press `Enter` — a lattice cage is generated around the weighted region, already linked to the mesh.
4. Reshape the cage, then press `Enter` again to apply (or `ESC` to discard).

Multi-mesh workflows are supported: selecting more than one mesh builds a single cage shared across all of them.

## Compatibility

- Blender **4.2 LTS and newer** (4.2, 4.3, 4.4, 5.0)
- Windows, macOS, Linux

## Contents

```{toctree}
:maxdepth: 2

installation
quickstart
workflow
interface
shortcuts
preferences
faq
troubleshooting
changelog
```

## License

WeightLattice is distributed under the GNU General Public License v3.0 or later.

Author: **Pino Iulio**
