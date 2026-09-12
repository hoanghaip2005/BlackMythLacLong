# 3D Generation Libraries

## Modly

Modly is installed locally at `assets/libraries/modly` for image-to-3D mesh generation and mesh processing. It is used as an optional asset-generation tool; Blender remains the scene assembly and validation tool.

- Repository: https://github.com/lightningpixel/modly
- Installed revision: `1476fd0b1c19c9ab177c1ca3ee4d1842119e9f65`
- Application version: `0.4.2`
- License: MIT; retain the attribution in `assets/libraries/modly/LICENSE` when distributing Modly or a derivative app.
- Runtime: embedded Python `3.11.9`.
- Current state: Node dependencies installed, Python backend environment installed, production build passed.

### Installed components

- Electron/React/Three.js application dependencies via `npm install`.
- Python backend dependencies from `api/requirements.txt`.
- FastAPI, Trimesh, PyMeshLab, Hugging Face Hub and CLI runtime.
- Python standalone runtime under `resources/python-embed`.

### Run locally

From `assets/libraries/modly`:

```powershell
npm run preview
```

The local automation API is available at `http://127.0.0.1:8765` while the desktop app is running. Check it with:

```powershell
resources/python-embed/python.exe tools/modly-cli/agent.py health
```

No AI model weights or extensions are installed yet. Install only an extension/model compatible with the machine GPU after the Phase 1 generation workflow is selected.

### Project usage rule

Use Modly to generate or refine a mesh from an approved visual reference. Record source image, model/extension, revision, license and output path in the asset manifest. Do not treat an AI-generated mesh as culturally approved; review it against `docs/harness/chapter-01/08-visual-design.md` before import into Blender.
