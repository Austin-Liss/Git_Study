import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("C:/Users/77192/.vscode/Python/Git-Study/Pokemon.csv")
df.columns = df.columns.str.lower().str.replace(' ', '_').str.replace('.', '', regex=False)

# Counting Legendaries
# print(df['legendary'].value_counts()) # Only 65 legendaries out of 800 Pokemons

# Comparing Legendary vs Non-Legendary
stats = (df.groupby('legendary')['total']
         .agg(n='count',mean='mean',median='median',deviation='std')
         .round(1)
         .rename(index={False:'Regular', True:'Legendary'})
         .rename_axis('group'))
# print(stats.shape)

# compare all six stats.
STATS = ['hp', 'attack', 'defense', 'sp_atk', 'sp_def', 'speed']
mean = df.groupby('legendary')[STATS].mean().round(1)
gap = mean.loc[True] - mean.loc[False]
percentage =( (mean.loc[True] / mean.loc[False] -1) * 100).round(1)
table = (pd.DataFrame({
        'regular' : mean.loc[False],
        'Legendary' : mean.loc[True],
        'Gap' : gap,
        "Percentage" : percentage
}))
# print(table)

# Charting using matplotlib
fig , axes = plt.subplots(figsize=(9,5))

x = np.arange(6)
w = 0.4

b1 = plt.bar(x - w/2,mean.loc[False],w,label="Regular",color='C0')
b2 = plt.bar(x + w/2,mean.loc[True],w,label="Legendary",color='C1')

axes.bar_label(b1, fmt="%.0f", padding=2, fontsize=8)
axes.bar_label(b2, fmt="%.0f", padding=2, fontsize=8)

axes.set_xticks(x, STATS)
axes.set_title("Mean base stats: legendary vs regular")
axes.set_ylabel("Mean value")
axes.set_ylim(0, 125)
axes.legend(frameon=False)
axes.grid(True, axis="y", alpha=0.3)
axes.set_axisbelow(True)
axes.spines["top"].set_visible(False)
axes.spines["right"].set_visible(False)

plt.show()