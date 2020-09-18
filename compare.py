#%%
import os
import csv
import pandas as pd
import numpy as np
import matplotlib
from sqlalchemy import create_engine
from config import db_password

#%%
# load data into DataFrames
IMCG_load = "data\emeaIMCG8Jun20.csv"
GNS_load = "data\W01027.csv"

df_IMCG = pd.read_csv(IMCG_load)
df_GNS = pd.read_csv(GNS_load)

#%%
# check data frames
# df_GNS
df_IMCG

#%%
ImcgNotNull = df_IMCG.notnull().sum()
ImcgIsNull = df_IMCG.isnull().sum()
print(
    f"{ImcgNotNull}\n\n"
    f"{ImcgIsNull}\n\n"
    f"Data Types:\n{df_IMCG.dtypes}"
    )

#%%
GnsNotNull = df_GNS.notnull().sum()
GnsIsNull = df_GNS.isnull().sum()
print(
    f"{GnsNotNull}\n\n"
    f"{GnsIsNull}\n\n"
    f"Data Types:/n  {df_GNS.dtypes}"
    )
