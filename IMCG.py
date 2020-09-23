#%%
import pandas as pd
import os
import matplotlib
import numpy as np

#%%
# load data into DataFrames
global_attr = "data\W01027_A02.csv"
IMCG = "data\IMCG_21sep_20.csv"

IMCG_df = pd.read_csv(IMCG)
attr_df = pd.read_csv(global_attr)

# %%
# view column headers and sample data
print(
    f"{IMCG_df.head()}/n/n"
    f"{attr_df.head()}"
    )

#%%
# remove spaces from column names for later transformations
IMCG_df.columns = IMCG_df.columns.str.replace(" ", "")
attr_df.columns = attr_df.columns.str.replace(" ", "")

print(
    f"{IMCG_df.head()}/n/n"
    f"{attr_df.head()}"
    )
    
# %%
