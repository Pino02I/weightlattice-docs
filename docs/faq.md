# FAQ

## Does it work with modifiers already on the mesh?

Yes. The Lattice modifier is inserted according to the **Modifier Position** preference, and the rest of your stack is untouched.

## Can I keep the lattice instead of applying it?

Yes — just leave the session (`ESC` from Weight Paint, or simply switch modes). The lattice and its modifier stay live on the mesh. You can re-open it later with `Enter` in Weight Paint, or manage it from the Object Mode panel.

## Can I have more than one lattice on the same mesh?

Yes. Each painted vertex group gets its own cage. The Object Mode panel lists them all, and **Apply All / Remove All** act on every one.

## Does it work on multiple meshes at once?

Yes. Select several meshes in Object Mode (or use multi-object Edit Mode) before creating: one shared cage drives all of them.

## Will the shortcuts conflict with my Blender keys?

No. Every WeightLattice operator checks the active session in its `poll()`, so while no session is running the keys fall through to Blender's native shortcuts. You can also rebind everything in the preferences.

## Is it destructive?

Nothing is baked until you press `Enter` in Edit Lattice (or click Apply). `ESC` and Remove discard the cage and leave the mesh untouched. The **All Lattices On/Off** toggle previews the result non-destructively.

## Which Blender versions are supported?

Blender 4.2 LTS and newer (4.2, 4.3, 4.4, 5.0), on Windows, macOS and Linux.
