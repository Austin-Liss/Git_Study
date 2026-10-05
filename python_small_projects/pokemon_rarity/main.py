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

# print(df.loc[legend.total.idxmin()]) # shows Articuno is a Legendary with lowest total stats
# print(df.loc[regular.total.idxmax()]) # shows Mega Tyranitar is Non-Legendary with highest total stats

lo, hi = legend.total.min(), regular.total.max()
# print((legend.total <= hi).sum())
# print((regular.total >= lo).mean())

# Task 5. Mean of all six stats for both groups. Then add a row showing the gap between them. Which stat has the biggest gap? The smallest?
mean = df.groupby('legendary')[STATS].mean()
gap = mean.loc[True] - mean.loc[False]
mean.loc['Gap'] = gap
mean = mean.rename({False: 'Regular', True: 'Legendary'}).rename_axis('group').round(2)
# print(mean)
# print(gap.idxmax(),gap.max().round(2))
# print(gap.idxmin(),gap.min().round(2))

# Task 6. Which types have the most legendaries? Show the count and the percentage of that type that's legendary — they give different answers.
count = df.groupby(['legendary','type_1']).size().unstack(fill_value=0)
n = df.groupby('type_1').size()
pct = (count / n).round(2)
tab_6 = df.groupby('type_1').agg(
    total=('legendary', 'size'),
    legendary=('legendary', 'sum'),
    pct=('legendary', 'mean'),
)
tab_6['regular'] = tab_6.total - tab_6.legendary
tab_6['pct_legendary'] = (tab_6.pop('pct') * 100).round(1)
print(tab_6.legendary.nlargest(3)) # shows top 3 type has high legendary rate
print(df.query("type_1 == 'Psychic' and legendary")) # print out all Psychic Legendaries 