import pandas as pd
from config import FEATURE_COLS
from ml.model_loader import load_all_models, load_metrics

class Predictor:
    def __init__(self):
        self.models = load_all_models()
        self.metrics = load_metrics()

    def predict(self, user_data: dict, model_key: str = "lr") -> dict:
        if model_key not in self.models:
            raise ValueError(f"Модель '{model_key}' не найдена. Запустите ячейку сохранения в ноутбуке.")

        row = {col: [float(user_data[col])] for col in FEATURE_COLS}
        df_input = pd.DataFrame(row)[FEATURE_COLS]

        model_info = self.models[model_key]
        pipe = model_info["model"]

        pred_class = int(pipe.predict(df_input)[0])
        prob = float(pipe.predict_proba(df_input)[0][1])

        return {
            "model_key": model_key,
            "model_name": model_info["title"],
            "class": pred_class,
            "probability": round(prob, 4),
            "message": "Пользователь КЛИКНЕТ по рекламе" if pred_class == 1 else "Пользователь НЕ КЛИКНЕТ по рекламе"
        }
