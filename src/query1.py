from src.list_load import list_data_collect

import pandas as pd
import numpy as np 

def query1():
    churn_list = list_data_collect()

    query1_result = churn_list[(churn_list['SeniorCitizen'] == 1) & (churn_list['Dependents'] == 'Yes') & (churn_list['gender'] == 'Female')].copy()

    return query1_result
