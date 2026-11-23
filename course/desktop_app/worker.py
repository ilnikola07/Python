from PySide6.QtCore import QThread, Signal

class PredictWorker(QThread):
    finished_ok = Signal(dict)
    failed = Signal(str)

    def __init__(self, service, user_data: dict, model_key: str):
        super().__init__()
        self.service = service
        self.user_data = user_data
        self.model_key = model_key

    def run(self):
        try:
            res = self.service.predict_and_save(self.user_data, model_key=self.model_key, source="Desktop")
            self.finished_ok.emit(res)
        except Exception as e:
            self.failed.emit(str(e))


class BatchPredictWorker(QThread):
    finished_ok = Signal(object)
    failed = Signal(str)

    def __init__(self, data_service, df, pipe):
        super().__init__()
        self.data_service = data_service
        self.df = df
        self.pipe = pipe

    def run(self):
        try:
            res_df = self.data_service.batch_predict(self.df, self.pipe)
            self.finished_ok.emit(res_df)
        except Exception as e:
            self.failed.emit(str(e))
