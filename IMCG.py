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
# join DF
merged = pd.merge(attr_df,IMCG_df,how="outer", on="PARTTYPE")
merged
merged.to_csv('data\merged.csv')
    
# %%
# list where CPT or CPC or GCS is null
# >>> df.iloc[df[(df.isnull().sum(axis=1) >=qty_of_nuls)].index]
mergedNulls = merged.iloc[merged[(merged.isnull().sum(axis=1) >=0)].index]
mergedNulls
#%%
CPT_nulls = merged[merged['CombinedPartType'].isnull().tolist()]
CPT_nulls
# %%
CPC_nulls = merged[merged['CombinedPartClass'].isnull().tolist()]
CPC_nulls

#%%
GCS_nulls = merged[merged['GCS'].isnull().tolist()]
GCS_nulls

#%%
CPT_nulls.to_csv('data\CPT_Nulls.csv')
CPC_nulls.to_csv('data\CPC_Nulls.csv')
GCS_nulls.to_csv('data\GCS_Nulls.csv')

# %%
IMCG_PT = IMCG_df.groupby('PARTTYPE').nunique()
IMCG_PT

# %%
attr_PT = attr_df.groupby('PARTTYPE').nunique()
attr_PT

# %%
attr_PT.dtypes
# %%
attr_PT.PARTTYPE.value_counts()
# %%
IMCG_PT.PARTTYPE.value_counts()
# %%
notin = IMCG_df.PARTTYPE.isin(attr_df.PARTTYPE).value_counts()

# %%
attr_df.PARTTYPE.isin(IMCG_df.PARTTYPE).value_counts()
# %%
merge = IMCG_df.merge(attr_df, how='left', indicator = True)
merge

#%%
merge[merge['_merge']=='left_only']

# %%
merged['_merge'].to_list

# %%
