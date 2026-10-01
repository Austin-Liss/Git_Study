import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("C:/Users/77192/.vscode/Python/Git-Study/python_small_projects/Pokemon.csv")
df.columns = df.columns.str.lower().str.replace(' ', '_').str.replace('.', '', regex=False)

STATS = ['hp', 'attack', 'defense', 'sp_atk', 'sp_def', 'speed']

# Task 2. How many legendaries are there, and what percentage of the dataset? Print both.
count = df.legendary.sum()
print(f"There are {count} legendaries out of {len(df)} Pokemons ({((count / len(df))*100):.1f}%)")