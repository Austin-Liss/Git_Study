import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Set up
df = pd.read_csv('C:/Users/77192/.vscode/Python/Git-Study/python_small_projects/Costco/costco_data.csv',dtype={'zip_code':str})
print(df.dtypes)