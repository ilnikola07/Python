import pandas as pd
import numpy as np
import joblib
from sklearn.preprocessing import StandardScaler

DEFAULT_MODEL_PATH = 'models/lr_model.pkl'


def load_csv(filepath: str) -> pd.DataFrame:
    """Загрузка CSV-файла."""
    return pd.read_csv(filepath)


def preprocess(df: pd.DataFrame) -> pd.DataFrame:
    """Полная предобработка данных."""
    df = df.copy()
    
    # Удаление неинформативных столбцов
    cols_to_drop = ['Ad Topic Line', 'City', 'Country']
    df = df.drop([c for c in cols_to_drop if c in df.columns], axis=1)
    
    # Преобразование Timestamp
    if 'Timestamp' in df.columns:
        df['Timestamp'] = pd.to_datetime(df['Timestamp'])
        df['Year'] = df['Timestamp'].dt.year
        df['Month'] = df['Timestamp'].dt.month
        df['DayOfWeek'] = df['Timestamp'].dt.dayofweek
        df['Hour'] = df['Timestamp'].dt.hour
        df = df.drop('Timestamp', axis=1)
    
    # Создание Age_Group
    df['Age_Group'] = pd.cut(df['Age'],
                              bins=[0, 25, 35, 50, 100],
                              labels=['18-25', '26-35', '36-50', '51+'])
    
    return df


def load_model(filepath: str = DEFAULT_MODEL_PATH):
    """Загрузка модели через joblib."""
    return joblib.load(filepath)


def predict_user(model, user_data: dict, scaler=None) -> dict:
    """Предсказание для одного пользователя."""
    df_user = pd.DataFrame([user_data])
    df_user = preprocess(df_user)
    df_user = pd.get_dummies(df_user, columns=['Age_Group'], prefix='Age', drop_first=True)
    
    expected_cols = ['Daily Time Spent on Site', 'Age', 'Area Income',
                     'Daily Internet Usage', 'Male', 'Year', 'Month',
                     'DayOfWeek', 'Hour', 'Age_26-35', 'Age_36-50', 'Age_51+']
    
    for col in expected_cols:
        if col not in df_user.columns:
            df_user[col] = 0
    
    df_user = df_user[expected_cols]
    
    if scaler is not None:
        num_cols = ['Daily Time Spent on Site', 'Age', 'Area Income',
                    'Daily Internet Usage', 'Year', 'Month', 'DayOfWeek', 'Hour']
        df_user[num_cols] = scaler.transform(df_user[num_cols])
    
    prediction = model.predict(df_user)[0]
    probability = model.predict_proba(df_user)[0][1]
    
    return {
        'class': int(prediction),
        'probability': round(float(probability), 4),
        'message': 'Кликнет' if prediction == 1 else 'Не кликнет'
    }
