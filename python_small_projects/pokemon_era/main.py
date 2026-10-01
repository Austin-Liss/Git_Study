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

# Task 9. For each Pokémon, work out whether it leans physical (attack/defense) or special (sp_atk/sp_def). 
#   You decide how to define the lean — a difference, a ratio, something else. Be able to defend it in the README.
df['lean'] = (df['attack'] - df['sp_atk']) / (df['attack'] + df['sp_atk'])
df['specialty'] = np.select(
                [df['lean'] > 0 , df['lean'] < -0.1],
                ['Physical', 'Special Atk'],
                default= 'Balanced'
                )
sample = ['Alakazam','Machamp','Regirock','Regice','Shuckle','Snorlax','Magikarp','Blissey','Gengar','Garchomp']
# print(df.set_index('name').reindex(sample)[['attack','sp_atk','lean','specialty']].round(2))
