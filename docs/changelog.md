# Changelog

All notable changes to **WeightLattice** are documented here. The project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## 1.0.0 — 2026-07-12

First release.

### Workflow

- Weight Paint to lattice creation driven by the active vertex group: paint an area, press `Enter`, and a lattice cage is generated around the weighted region and linked to the mesh. Reshape the cage and press `Enter` to apply, or `ESC` to remove.
- Lattice refit (`U`) that updates the bounding cage to the current weights and resets the control points to their rest positions.
- Multi-mesh shared cages: multiple meshes selected in Object Mode, or multiple meshes in multi-object Edit Mode, build a single cage shared across all of them.
- **Lattice from Selection** in Edit Mesh: build a cage directly from the current vertex/edge/face selection.

### Shortcuts

- All shortcuts live in native Blender keymaps and only respond while a session is active, so they never shadow Blender's own keys.
- Rebindable from the addon preferences, with live key capture and per-shortcut / global reset.

### Interface

- N-panel for Object Mode, Weight Paint, Edit Mesh and Edit Lattice, plus right-click menu entries.
- Apply / Remove, Apply All / Remove All, **All Lattices On/Off** non-destructive preview and **Clean Orphan Weights**.
- Shared-cage Strength slider updating every linked mesh in real time.
- Viewport status line shown only while a session is active.
- Preferences for default resolution, padding, strength, interpolation, modifier position and cleanup behaviour.

### Compatibility

- Blender 4.2 LTS and newer (4.2, 4.3, 4.4, 5.0). Windows, macOS, Linux.
