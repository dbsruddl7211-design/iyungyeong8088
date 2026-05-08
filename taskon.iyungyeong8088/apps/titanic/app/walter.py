import pandas as pd
from pathlib import Path

_CSV_PATH = Path(__file__).resolve().parent / "Titanic-Dataset.csv"


class Walter(object):
    def __init__(self):
        pass

        
    def get_data(self):
        df = pd.read_csv(_CSV_PATH)
        # 첫 번째 행 1개를 DataFrame 형태로 반환
        return df.iloc[[0]].astype(object).where(df.iloc[[0]].notna(), None)

    def get_count(self):
        df = pd.read_csv(_CSV_PATH)
        # 전체 승객 수 반환
        return len(df)

    def get_survived(self):
        df = pd.read_csv(_CSV_PATH)
        # 생존 여부를 0(사망), 1(생존)으로 구분해 개수 반환
        survived_counts = df["Survived"].value_counts().to_dict()
        return {
            "0": int(survived_counts.get(0, 0)),
            "1": int(survived_counts.get(1, 0)),
        }