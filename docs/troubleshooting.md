# Troubleshooting

## No lattice is created

Check that:

- The active object is a mesh.
- You are in Weight Paint mode.
- There is an active vertex group.
- At least one vertex has weight above the threshold.

## The lattice does not update

Make sure the mesh still has a lattice modifier linked to the active vertex group.

## The lattice cannot be applied

Make sure the active object is the lattice and that the mesh it controls still exists.

## The brush does not activate

Some Blender versions handle tool activation differently. If needed, open the standard brush tools manually and retry.

## The addon panel does not appear

Check that the addon is enabled and that you are in a supported mode for the relevant panel.

## The deformation is too weak

Increase the lattice modifier strength in the properties panel or in the addon preferences.

## The bounding box is too tight

Increase the padding value in the addon preferences before generating the lattice again.
