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
NewNotNull = attr_df.notnull().sum()
NewIsNull = attr_df.isnull().sum()

IMCGnotNull = IMCG_df.notnull().sum()
IMCGisNull = IMCG_df.isnull().sum()

print(
    f"{NewNotNull}\n\n"
    f"{NewIsNull}\n\n"
    f"New Attribute data types:\n{attr_df.dtypes}\n\n"
    f"{IMCGnotNull}\n\n"
    f"{IMCGisNull}\n\n"
    f"IMCG Data types:\n{IMCG_df.dtypes}\n"
    )

#%%
# compare Part Type values in tables
IMCG_df["In Agile?"] = np.where(attr_df['PARTTYPE'] == IMCG_df['PARTTYPE'])
IMCG_df

#%%
# Applying upper() method on 'PARTTYPE' column in GNS table

attr_df['PARTTYPE'] = attr_df['PARTTYPE'].apply(lambda x: x.upper())

# ignore case
# df2 = attr_df['PARTTYPE'].str.contains(IMCG_df['PARTTYPE'], case=False)

# comparing Part Type columns of truth tables
IMCG_true = IMCG_df['PARTTYPE'].isin(attr_df['PARTTYPE']).value_counts()

Attr_true = attr_df['PARTTYPE'].isin(IMCG_df['PARTTYPE']).value_counts()

#%%
print(
    f"IMCG part types in GNS:\n{IMCG_true}\n\n"
    f"GNS part types in IMCG:\n{Attr_true}\n\n"
    )
# %%
IMCG_df['IsinGNS?'] = np.where(IMCG_df['seniority'] == True, 'senior', 'Non-senior')

newDF['IsinGNS?'] = IMCG_df['PARTTYPE'].isin(attr_df['PARTTYPE'])

# %%
newDF['IsinGNS?'].value_counts()

# %%
IMCG_df['hasPT?'] = np.where(IMCG_df['PARTTYPE'] == attr_df['PARTTYPE'])
# df['hasimage'] = np.where(df['photos']!= '[]', True, False)
IMCG_df['hasPT?']

# %%
# join DF
merged = pd.merge(attr_df,IMCG_df,how="outer", on="PARTTYPE")
merged
merged.to_csv('data\merged.csv')
# %%
IMCG_df['hasPT?'] = np.where(IMCG_df['PARTTYPE'] == attr_df['PARTTYPE'])
# df['hasimage'] = np.where(df['photos']!= '[]', True, False)
IMCG_df['hasPT?']

# %%
# count unique values in part type column of IMCG
IMCG_df.PARTTYPES.value_counts()
# %%
c = IMCG_df.groupby('PARTTYPE').nunique()
c
# %%
