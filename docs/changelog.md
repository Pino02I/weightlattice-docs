# Changelog

## 1.0.0

First commercial release of WeightLattice.

### Workflow

- Weight Paint to lattice creation workflow driven by the active vertex group.
- Lattice refit that updates the bounding cage after new weights are painted.
- Edit Lattice support with resolution, interpolation, and modifier controls.
- Apply and Remove actions that propagate to every mesh using the lattice.

### Multi-mesh shared cages

- **Object Mode** with multiple meshes selected: `New Weight Lattice` builds a single cage around every selected mesh. Each mesh receives a lattice modifier and no vertex group is created.
- **Edit Mesh** multi-object edit: `Lattice from Selection` builds a shared cage around the selected vertices across all active meshes. Each mesh gets its own vertex group at weight 1.0 on those vertices.

### Shortcuts

- **Enter** creates or updates the lattice in Weight Paint and applies it in Edit Lattice.
- **Q** switches between Weight Paint and Edit Lattice (replaces the older internal `W` binding).
- **Alt+F** fills the active vertex group at weight 1.0 on every vertex.
- **U** refits the lattice bounding box to the current weights without switching modes.
- **B / L / R** activate the Draw brush, Linear gradient, and Radial gradient in Weight Paint.
- **I / X / S** invert, delete, or smooth weights on the active vertex group.
- **Numpad +/−** change lattice resolution on all axes at once in Edit Lattice.

### Integration

- N-panel for Object Mode, Weight Paint, Edit Mesh, and Edit Lattice.
- Context-menu entries for the main operators in every relevant mode.
- Status bar hints showing the active shortcuts.
- Addon preferences for resolution, padding, strength, interpolation, and cleanup behavior.
