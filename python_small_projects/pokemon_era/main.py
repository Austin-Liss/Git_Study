import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("C:/Users/77192/.vscode/Python/Git-Study/python_small_projects/Pokemon.csv")
df.columns = df.columns.str.lower().str.replace(' ', '_').str.replace('.', '', regex=False)

STATS = ['hp', 'attack', 'defense', 'sp_atk', 'sp_def', 'speed']

# Checking dual type each gen
df['is_dual'] = df['type_2'].notna()
is_dual = df.groupby('generation')['is_dual'].mean().round(2)

# Checking distinct type dual

df['combo'] = df['type_1'] +'/' + df['type_2'].fillna('none')
first = df.groupby('combo')['generation'].min()
present = df.groupby('generation')['combo'].nunique()

# Task 5. For each Pokémon, measure how uneven its stats are. 
    #  A creature with 100 in everything is balanced; one with 180 attack and 30 defense is a specialist.
df['spread'] = df[STATS].std(1)
cols = ['name','spread'] + STATS
top_5 = df.nlargest(5,'spread')[cols].round(1)

# Task 6. Has that measure changed across generations? Compare mean and median per generation.
compare = df.groupby('generation')['spread'].agg(count='size',mean='mean',median='median',q75=lambda s : s.quantile(.75),max='max').round(1)

# Task 7. Is the trend the same for legendaries and non-legendaries?
trend = (df.groupby(['generation','legendary'])['spread']
         .agg(n='size',mean='mean',median='median')
         .unstack()
         .rename(columns={False:'Regular',True:'Legendary'})
         .round(2)
         )
