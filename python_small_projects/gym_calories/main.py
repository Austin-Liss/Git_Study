import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Task 1. Load and clean the column names. 
    # These are messier than Pokémon — Weight (kg), Workout_Frequency (days/week), Session_Duration (hours). Get them all to lowercase, underscores, no brackets or slashes.
df = pd.read_csv("C:/Users/77192/.vscode/Python/Git-Study/python_small_projects/gym_members_exercise_tracking.csv")
df.columns = df.columns.str.lower().str.replace(' ','_').str.replace('(','',regex=False).str.replace(')','',regex=False).str.replace('/','_',regex=False).str.replace(')','')
# print(df.columns)

# Task 2. Mean calories burned by workout type, with counts.    
    # Then compute the spread — highest mean minus lowest mean. As a percentage of the overall mean, is that spread big or small?
# tab = df.groupby('workout_type')['calories_burned'].agg(n='size',mean='mean')
# m = tab['mean']
# spread = m.max() - m.min()
# pct = (spread / df.calories_burned.mean()) * 100
# print(f"Spread: {spread:.1f} calories {pct:.1f}% of overall mean {df.calories_burned.mean():.1f} ")

# Task 3. Correlate every numeric column against calories_burned, sorted. Which variable dominates? Which are near zero? Any negative?
cor = df.corr(numeric_only=True)['calories_burned'].drop('calories_burned').sort_values()
negatives = cor[cor < 0]
near_zero = cor[cor.abs() < 0.1]
dominate = cor.abs().idxmax()
print(f'Negatives : {list(negatives.index)}')
print(f'Near zeros : {list(near_zero.index)}')
print(f'Dominate : {dominate} ({cor[dominate]:.2f})')

