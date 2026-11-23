import pandas as pd
from config import FEATURE_COLS

class DataService:
    @staticmethod
    def load_csv(filepath: str) -> pd.DataFrame:
        return pd.read_csv(filepath)

    @staticmethod
    def preprocess(df: pd.DataFrame) -> pd.DataFrame:
        df = df.copy()
        cols_to_drop = ['Ad Topic Line', 'City']
        df = df.drop([c for c in cols_to_drop if c in df.columns], axis=1)

        if 'Timestamp' in df.columns:
            ts = pd.to_datetime(df['Timestamp'])
            df['Month'] = ts.dt.month
            df['DayOfWeek'] = ts.dt.dayofweek
            df['Hour'] = ts.dt.hour
            df = df.drop('Timestamp', axis=1)

        if 'Age' in df.columns:
            df['Age_Group'] = pd.cut(df['Age'], bins=[0, 25, 35, 50, 100], labels=['18-25', '26-35', '36-50', '51+']).astype(str)
        return df

    @staticmethod
    def batch_predict(df: pd.DataFrame, pipe) -> pd.DataFrame:
        df_proc = DataService.preprocess(df)
        missing = [c for c in FEATURE_COLS if c not in df_proc.columns]
        if missing:
            raise ValueError(f"В таблице не хватает столбцов: {missing}")
        X = df_proc[FEATURE_COLS]
        df_res = df_proc.copy()
        df_res['Predicted_Click'] = pipe.predict(X)
        df_res['Click_Probability'] = pipe.predict_proba(X)[:, 1].round(4)
        return df_res
