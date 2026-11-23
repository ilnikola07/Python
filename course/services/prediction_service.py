from ml.predictor import Predictor
from services.db_service import DBService

class PredictionService:
    def __init__(self):
        self.predictor = Predictor()
        self.db = DBService()

    def predict_and_save(self, user_data: dict, model_key: str = "lr", source: str = "Desktop") -> dict:
        result = self.predictor.predict(user_data, model_key=model_key)
        self.db.add_record(
            source=source,
            model_name=result["model_name"],
            features=user_data,
            probability=result["probability"],
            prediction_text=result["message"]
        )
        return result
