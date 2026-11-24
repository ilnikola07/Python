import joblib
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score, roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier

from config import FEATURE_COLS, METRICS_FILE, MODEL_FILES, MODELS_DIR


def train_models(df: pd.DataFrame):
    """Обучает LR, DT и MLP на переданном датафрейме и сохраняет пайплайны и метрики."""
    MODELS_DIR.mkdir(parents=True, exist_ok=True)

    target_col = "Clicked on Ad"
    missing = [c for c in FEATURE_COLS + [target_col] if c not in df.columns]
    if missing:
        raise ValueError(f"В датасете отсутствуют необходимые столбцы: {missing}")

    X = df[FEATURE_COLS]
    y = df[target_col]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    pipelines = {
        "lr": make_pipeline(StandardScaler(), LogisticRegression(max_iter=500, random_state=42)),
        "dt": make_pipeline(StandardScaler(), DecisionTreeClassifier(max_depth=5, random_state=42)),
        "mlp": make_pipeline(StandardScaler(), MLPClassifier(hidden_layer_sizes=(64, 32), max_iter=500, random_state=42)),
    }

    metrics_summary = {}

    for key, pipe in pipelines.items():
        title, model_path = MODEL_FILES[key]
        pipe.fit(X_train, y_train)
        joblib.dump(pipe, model_path)

        y_pred = pipe.predict(X_test)
        y_prob = pipe.predict_proba(X_test)[:, 1]

        metrics_summary[key] = {
            "name": title,
            "accuracy": float(accuracy_score(y_test, y_pred)),
            "precision": float(precision_score(y_test, y_pred)),
            "recall": float(recall_score(y_test, y_pred)),
            "f1": float(f1_score(y_test, y_pred)),
            "roc_auc": float(roc_auc_score(y_test, y_prob)),
            "y_test": y_test.tolist(),
            "y_pred": y_pred.tolist(),
        }

    joblib.dump(metrics_summary, METRICS_FILE)
