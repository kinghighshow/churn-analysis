from pathlib import Path

import pandas as pd


def list_data_collect():
    
    project_root = Path(__file__).resolve().parent.parent
    csv_path = project_root / "data" / "churn_dataset.csv"

    churn_data = pd.read_csv(csv_path)
    return churn_data
