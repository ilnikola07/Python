import sqlite3
import json
from datetime import datetime
from config import DB_PATH

class DBService:
    def __init__(self, db_path=DB_PATH):
        self.db_path = db_path
        self._init_db()

    def _init_db(self):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS history (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    created_at TEXT NOT NULL,
                    source TEXT NOT NULL,
                    model_name TEXT NOT NULL,
                    features_json TEXT NOT NULL,
                    probability REAL NOT NULL,
                    prediction_text TEXT NOT NULL
                )
            """)

    def add_record(self, source: str, model_name: str, features: dict, probability: float, prediction_text: str):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute(
                "INSERT INTO history (created_at, source, model_name, features_json, probability, prediction_text) VALUES (?, ?, ?, ?, ?, ?)",
                (datetime.now().strftime("%Y-%m-%d %H:%M:%S"), source, model_name, json.dumps(features, ensure_ascii=False), probability, prediction_text)
            )

    def get_records(self, source_filter: str = "Все") -> list[tuple]:
        with sqlite3.connect(self.db_path) as conn:
            if source_filter == "Все":
                cur = conn.execute("SELECT id, created_at, source, model_name, features_json, probability, prediction_text FROM history ORDER BY id DESC")
            else:
                cur = conn.execute(
                    "SELECT id, created_at, source, model_name, features_json, probability, prediction_text FROM history WHERE source = ? ORDER BY id DESC",
                    (source_filter,)
                )
            return cur.fetchall()

    def clear_records(self):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("DELETE FROM history")
