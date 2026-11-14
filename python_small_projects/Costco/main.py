import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Set up
df = pd.read_csv('C:/Users/77192/.vscode/Python/Git-Study/python_small_projects/Costco/costco_data.csv',dtype={'zip_code':str})

# Task 2 : Check the primary key - supplier_id is supposed to uniquely identify a supplier. Verify that it actually does.
# print(df.supplier_id.duplicated().sum()) # -> shows how many duplicated ID
# print(df[df.supplier_id.duplicated(keep=False)])
clean_df = df.drop_duplicates() # -> Drop the duplicated rows, keep the first one

# Task 3 : Find every missing value, which column it’s in, what percentage of the file that is, and which suppliers are affected.
count_na = df.isna().sum()
percentage = (count_na / len(df)) * 100
# print(count_na[count_na > 0])
# print(percentage[percentage > 0].round(2))
# print(df[df.lead_time_days.isna()])

# Task 4 : Range checks on the numeric columns 
    # Check whether lead_time_days and quality_rating contain values that are possible in principle but implausible in practice.
# print(df[['lead_time_days','quality_rating']].describe())

# Task 5 : Normalize the supplier names
    # Find and fix names with leading/trailing whitespace and inconsistent capitalization.
ws = df.supplier_name != df.supplier_name.str.strip()
print(f'Whitespace problems: {ws.sum()}')
print(df.loc[ws,'supplier_name'].to_string())
print(df.loc[ws,'supplier_name'].apply(repr).to_string()) # points out apply(repr) makes difference
stripped = df.supplier_name.str.strip()
casing = stripped != stripped.str.title()
print(f'Casing problems: {casing.sum()}')
print(df.loc[casing,'supplier_name'].to_string())
print(df.loc[casing,'supplier_name'].apply(repr).to_string())
df['clean_name'] = df.supplier_name.str.strip().str.title()
changed = df.clean_name != df.supplier_name
print(f'Total changes: {changed.sum()}')
print(df.loc[changed,['supplier_id','supplier_name','clean_name']].to_string(index=False))
print(f'Spaces remaining: {(df.clean_name != df.clean_name.str.strip()).sum()}')