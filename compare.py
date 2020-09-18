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


#%%

