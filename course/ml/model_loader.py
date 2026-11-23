import joblib
from config import MODEL_FILES, METRICS_FILE

def load_all_models() -> dict:
    loaded = {}
    for key, (title, path) in MODEL_FILES.items():
        if path.exists():
            loaded[key] = {"title": title, "model": joblib.load(path)}
    return loaded

def load_metrics() -> dict:
    if METRICS_FILE.exists():
        return joblib.load(METRICS_FILE)
    return {}
