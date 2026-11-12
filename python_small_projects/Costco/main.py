import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Set up
df = pd.read_csv('C:/Users/77192/.vscode/Python/Git-Study/python_small_projects/Costco/costco_data.csv',dtype={'zip_code':str})

# Task 2 : Check the primary key - supplier_id is supposed to uniquely identify a supplier. Verify that it actually does.
print(df.supplier_id.duplicated().sum()) # -> shows how many duplicated ID
print(df[df.supplier_id.duplicated(keep=False)])
clean_df = df.drop_duplicates() # -> Drop the duplicated rows, keep the first one