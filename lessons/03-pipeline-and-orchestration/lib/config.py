from pathlib import Path

CATEGORICAL_COLS = ["PULocationID", "DOLocationID", "passenger_count"]

# [3] means go up 3 levels from the current file -> from ./lessons/03/lib/config.py to ./
PROJECT_ROOT = Path(__file__).resolve().parents[3]
DATA_DIRPATH = str(PROJECT_ROOT / "data")
MODELS_DIRPATH = str(PROJECT_ROOT / "models")


if __name__ == "__main__":
    print("Current file:", Path(__file__).resolve())
    print("Project root:", PROJECT_ROOT)
    print("Data dir:", DATA_DIRPATH)
    print("Models dir:", MODELS_DIRPATH)
