import pickle
from pathlib import Path

import pandas as pd
from sklearn.tree import DecisionTreeClassifier

_BASE_DIR = Path(__file__).resolve().parent
_CSV_PATH = _BASE_DIR / "Titanic-Dataset.csv"
_MODEL_PATH = _BASE_DIR / "titanic_decision_tree.pkl"


class Rose:
    def __init__(self):
        self.model = DecisionTreeClassifier(random_state=42)

    def has_saved_model(self):
        return _MODEL_PATH.exists()

    def save_decision_tree_model(self):
        df = pd.read_csv(_CSV_PATH)

        # 타깃과 피처 분리
        y = df["Survived"]
        x = df.drop(columns=["Survived"])

        # 숫자형 결측치 보정
        numeric_cols = x.select_dtypes(include=["number"]).columns
        x[numeric_cols] = x[numeric_cols].fillna(x[numeric_cols].median())

        # 범주형 결측치 보정 후 원-핫 인코딩
        categorical_cols = x.select_dtypes(include=["object"]).columns
        x[categorical_cols] = x[categorical_cols].fillna("Unknown")
        x = pd.get_dummies(x, drop_first=True)

        self.model.fit(x, y)

        with open(_MODEL_PATH, "wb") as model_file:
            pickle.dump(self.model, model_file)

        return str(_MODEL_PATH)
