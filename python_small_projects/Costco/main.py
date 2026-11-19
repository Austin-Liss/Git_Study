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
# print(f'Whitespace problems: {ws.sum()}')
# print(df.loc[ws,'supplier_name'].to_string())
# print(df.loc[ws,'supplier_name'].apply(repr).to_string()) # points out apply(repr) makes difference
stripped = df.supplier_name.str.strip()
casing = stripped != stripped.str.title()
# print(f'Casing problems: {casing.sum()}')
# print(df.loc[casing,'supplier_name'].to_string())
# print(df.loc[casing,'supplier_name'].apply(repr).to_string())
df['clean_name'] = df.supplier_name.str.strip().str.title()
changed = df.clean_name != df.supplier_name
# print(f'Total changes: {changed.sum()}')
# print(df.loc[changed,['supplier_id','supplier_name','clean_name']].to_string(index=False))
# print(f'Spaces remaining: {(df.clean_name != df.clean_name.str.strip()).sum()}')

# Task 6 — Extract the entity type from the name
    # The last word of each supplier name describes what kind of business it is — 
    # Trading, Imports, Partners, Works, Co, and so on. Pull that out into its own column and count them.
df['entity'] = df.clean_name.str.strip().str.split().str[-1]
# print(df.clean_name.str.strip().str.split().str[-1].value_counts(ascending=True))
# print(df.head(2))

# Task 7 — Parse the dates and compute tenure
    # contract_start is currently text. Convert it to a real date, then compute how many years each supplier has been under contract.
df.contract_start = pd.to_datetime(df.contract_start)
# print(f'Check NaN values: {df.contract_start.isna().sum()}')
START = pd.Timestamp('2026-11-14')
today = START - df.contract_start
df['contract_days'] = today.dt.days
df['contract_years'] = (today.dt.days / 365.25).round(1)

# Task 9 — Check state against country
    #   Every row has a state and a country. Find out whether they’re consistent.
    # How:
    # Build a set of valid US state codes. 
    # Type out the two-letter codes as a Python set — or at minimum the ten that appear in this file. 
    # Check which states are actually present first: df['state'].unique().
    # Create a boolean column: does this row have a recognized US state code?
    # Cross-tabulate state against country: pd.crosstab(df['state'], df['country'])
    # Count the rows where the state is a US state code but the country is not USA.
US_STATES = {'AL','AK','AZ','AR','CA','CO','CT','DE','FL','GA','HI','ID','IL','IN','IA','KS','KY',
             'LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC','ND',
             'OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VT','VA','WA','WV','WI','WY','DC'}
df['is_us_states'] = df.state.isin(US_STATES)
# print(pd.crosstab(df.state,df.country))
bug = df.is_us_states & (df.country != 'USA')
# print(f'\nUS state but not in US: {bug.sum()} ({(bug.mean() * 100):.1f}%)')
# print(df.loc[bug,['supplier_id','supplier_name','city','state','zip_code','country']].to_string(index=False))

# Task 10 — Write a validation function
    # Do this: Write one function that takes a row and returns which checks it fails.
def check_row(row) :
    problems = []
    if pd.isna(row.lead_time_days) :
        problems.append('Missing lead day')
    if pd.isna(row.zip_code) :
        problems.append('Missing zipcode')
    if row.is_us_states and row.country != 'USA' :
        problems.append("Supplier's inconsistency")
    if row.clean_name != row.supplier_name :
        problems.append('Supplier name needs normalization')
    return problems
df['problems'] = df.apply(check_row,axis=1)
df['n_problems'] = df.problems.str.len()
print(f"rows with >=1 problem: {(df.n_problems > 0).sum()} of {len(df)}")
print(df.problems.explode().value_counts())