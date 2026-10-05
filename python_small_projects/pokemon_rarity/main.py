import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("C:/Users/77192/.vscode/Python/Git-Study/python_small_projects/Pokemon.csv")
df.columns = df.columns.str.lower().str.replace(' ', '_').str.replace('.', '', regex=False)

STATS = ['hp', 'attack', 'defense', 'sp_atk', 'sp_def', 'speed']

# Task 2. How many legendaries are there, and what percentage of the dataset? Print both.
count = df.legendary.sum()
# print(f"There are {count} legendaries out of {len(df)} Pokemons ({((count / len(df))*100):.1f}%)")

# Task 3. Mean, median, and count of total for legendary vs non-legendary. One agg call.
agg = (df.groupby('legendary')['total']
       .agg(n='size',mean='mean',median='median')
       .rename({True:'Legendary',False:'Regular'})
       .rename_axis('Type')
       .round(1))
# print(agg)

# Task 4. What's the lowest-total legendary, and the highest-total non-legendary? Do they overlap?
legend = df[df.legendary]
regular = df[~df.legendary]

print(df.loc[legend.total.idxmin()]) # shows Articuno is a Legendary with lowest total stats
print(df.loc[regular.total.idxmax()]) # shows Mega Tyranitar is Non-Legendary with highest total stats

lo, hi = legend.total.min(), regular.total.max()
print((legend.total <= hi).sum())
print((regular.total >= lo).mean())
