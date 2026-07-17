# WeightLattice — Documentation

Sphinx + MyST documentation for the [WeightLattice](https://superhivemarket.com/) Blender addon, hosted on Read the Docs.

## Publish (one-time setup)

1. Create a new GitHub repository (e.g. `weightlattice-docs`) and push this folder to it:
   ```
   git init
   git add .
   git commit -m "WeightLattice documentation 1.0.0"
   git branch -M main
   git remote add origin https://github.com/<your-username>/weightlattice-docs.git
   git push -u origin main
   ```
2. Go to <https://readthedocs.org/>, sign in with GitHub and click **Import a Project**.
3. Select the `weightlattice-docs` repository. Set the project slug/name to **weightlattice-docs** so the URL is `https://weightlattice-docs.readthedocs.io/` (the URL used inside the addon).
4. Read the Docs detects `.readthedocs.yaml` automatically and builds. Every future `git push` rebuilds the docs.

## Images

Screenshots go in `docs/_static/images/` — see the shot list in `docs/_static/images/README.txt`. PNG or JPG, viewport shots ideally 1600px wide or more.

## Build locally (optional)

```
pip install -r requirements.txt
sphinx-build -b html docs docs/_build/html
```

Open `docs/_build/html/index.html` in a browser.
