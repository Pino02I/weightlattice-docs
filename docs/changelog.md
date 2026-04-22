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

- **Enter** creates the lattice in Weight Paint, or opens the existing one in Edit Lattice without modifying it. In Edit Lattice it applies the deformation to every mesh bound to the cage.
- **U** refits the lattice bounding box to the current weights and resets the control points to their rest positions, so a new paint pass never inherits deformations from the previous cage.
- **Q** switches between Weight Paint and Edit Lattice (replaces the older internal `W` binding).
- **Alt+F** fills the active vertex group at weight 1.0 on every vertex.
- **B / L / R** activate the Draw brush, Linear gradient, and Radial gradient in Weight Paint.
- **I / X / S** invert, delete, or smooth weights on the active vertex group.
- **Numpad +/−** change lattice resolution on all axes at once in Edit Lattice.

### Modifier

- The **Strength** slider on the Edit Lattice panel is shared across every mesh that uses the cage: changing the value updates each linked modifier in real time.

### Integration

- N-panel for Object Mode, Weight Paint, Edit Mesh, and Edit Lattice.
- Context-menu entries for the main operators in every relevant mode.
- Status bar hints showing the active shortcuts.
- Addon preferences for resolution, padding, strength, interpolation, and cleanup behavior.
