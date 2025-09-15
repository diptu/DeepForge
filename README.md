# DeepForge
  DeepForge is a monorepo of production-ready deep learning project templates.
It includes:

- PyTorch Research: experiment scaffold with configs, training loop, tests.

- FastAPI Service: deploy trained models as APIs with Docker + CI/CD.

- Kaggle Baseline: clean starter kit for competitions with notebooks + pipelines.

All templates follow best practices: uv package manager, ruff, mypy, pytest, pre-commit, and GitHub Actions CI. Perfect for researchers, students, and engineers who want to go from prototype to production quickly and cleanly.


## Tagline
- Production-ready deep learning templates for research, APIs, and Kaggle.


## 📁 Repository layout

DL-Project-Templates/
├─ README.md
├─ pyproject.toml
├─ uv.lock
├─ Dockerfile
├─ docker-compose.yml
├─ Taskfile.yml
├─ main.py
├─ scripts/
│ ├─ train.py
│ ├─ export.py
│ └─ benchmark.py
├─ app/
│ ├─ __init__.py
│ ├─ main.py
│ ├─ api/
│ │ ├─ __init__.py
│ │ ├─ routes_health.py
│ │ ├─ routes_inference.py
│ │ └─ routes_train.py
│ ├─ core/
│ │ ├─ config.py
│ │ └─ logger.py
│ ├─ data/
│ │ └─ raw/.gitkeep
│ ├─ models/
│ │ ├─ __init__.py
│ │ ├─ model.py
│ │ └─ weights/.gitkeep
│ ├─ schemas/
│ │ ├─ __init__.py
│ │ ├─ request.py
│ │ └─ response.py
│ ├─ services/
│ │ ├─ __init__.py
│ │ ├─ loader.py
│ │ ├─ inference_service.py
│ │ └─ training_service.py
│ └─ utils/
│ ├─ __init__.py
│ ├─ file_utils.py
│ ├─ preprocessing.py
│ └─ postprocessing.py
└─ tests/
├─ __init__.py
├─ test_api.py
├─ test_end_to_end.py
├─ test_inference.py
├─ test_inference_sample.py
└─ test_training.py

### 🔗 Root Level

- README.md → Overview and usage instructions for the microservice.

- pyproject.toml → Python packaging, dependencies, and dev tools config.

- uv.lock → Lockfile to pin exact versions of dependencies.

- Dockerfile → Container definition for running the API in production.

- docker-compose.yml → Local dev/CI orchestration (API, volumes, ports).

- Taskfile.yml → Task runner shortcuts (e.g. task run, task lint).

- main.py → Entry point for scripts (can load/run app or tasks).

- scripts/ → Standalone scripts for model lifecycle tasks (train, export, benchmark).

- tests/ → Unit + integration tests for endpoints, inference, and training.

🗂 app/

- init.py → Marks folder as a package.

- main.py → FastAPI application instance and router wiring.

- app/api/

- init.py → Package marker.

- routes_health.py → Health endpoint for monitoring (/api/health).

- routes_inference.py → Inference endpoint (/api/predict).

- routes_train.py → Training endpoint (/api/train).

- app/core/

- config.py → Centralized settings (paths, env vars, seeds).

- logger.py → Logger setup (Loguru) for consistent logging.

- app/data/

- raw/ → Placeholder for raw datasets used in training.

- .gitkeep → Ensures empty dir is tracked in git.

- app/models/

- init.py → Package marker.

- model.py → ML model definition (pipeline, architecture).

- weights/ → Directory for trained artifacts (.joblib, .pkl, .h5).

- app/schemas/

- init.py → Package marker.

- request.py → Pydantic schema for request validation (input features).

- response.py → Pydantic schema for response (predicted label, probabilities).

- app/services/

- init.py → Package marker.

- loader.py → Loads latest model artifact from weights/.

- inference_service.py → Contains inference logic (predict_proba).

- training_service.py → Training pipeline, saves new model artifacts.

- app/utils/

- init.py → Package marker.

- file_utils.py → Helpers for file/directory operations.

- preprocessing.py → Input preprocessing (clean/transform features).

- postprocessing.py → Output postprocessing (map probabilities to labels).

- ⚙️ scripts/

- train.py → CLI to trigger training and save a model artifact.

- export.py → CLI to export trained model to ONNX/TorchScript (future extension).

- benchmark.py → CLI to benchmark endpoint latency/throughput.

- 🧪 tests/

- init.py → Package marker.

- test_api.py → Tests API routes (health, predict).

- test_end_to_end.py → Tests full workflow (train → predict).

- test_inference.py → Unit tests for inference logic.

- test_inference_sample.py → Sample-based inference test with known inputs.

- test_training.py → Unit tests for training logic and artifact creation.

## 🧩 Template: `templates/fastapi-ml-microservice`


A complete FastAPI microservice for training + inference, mirroring the
layout you shared. Includes health, training, and inference endpoints;
model loader; preprocessing; and test suite.


