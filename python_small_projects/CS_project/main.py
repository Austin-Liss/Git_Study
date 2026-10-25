import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('C:/Users/77192/.vscode/Python/Git-Study/python_small_projects/CS_project/cs_students.csv')
df.columns = df.columns.str.lower().str.replace(' ','_')
