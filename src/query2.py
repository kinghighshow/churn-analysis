from src.list_load import list_data_collect

import pandas as pd
import numpy as np


def query2():
    churn_list = list_data_collect()

    query2_result = churn_list[
        (churn_list['InternetService'] == 'DSL') &
        (churn_list['tenure'] < 20)
    ]

    return query2_result