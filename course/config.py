from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
MODELS_DIR = BASE_DIR / "models"
DATA_PATH = BASE_DIR / "advertising.csv"
DB_PATH = BASE_DIR / "history.db"

FEATURE_COLS = [
    'Daily Time Spent on Site',
    'Age',
    'Area Income',
    'Daily Internet Usage',
    'Male',
    'Month',
    'DayOfWeek',
    'Hour'
]

MODEL_FILES = {
    "lr": ("Логистическая регрессия (LR)", MODELS_DIR / "lr_pipeline.joblib"),
    "dt": ("Дерево решений (DT)", MODELS_DIR / "dt_pipeline.joblib"),
    "mlp": ("Нейросеть (MLP)", MODELS_DIR / "mlp_pipeline.joblib"),
}
METRICS_FILE = MODELS_DIR / "metrics_summary.joblib"

import os
from dotenv import load_dotenv

load_dotenv(BASE_DIR / ".env")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")

