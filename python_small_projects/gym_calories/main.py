import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Task 1. Load and clean the column names. 
    # These are messier than Pokémon — Weight (kg), Workout_Frequency (days/week), Session_Duration (hours). Get them all to lowercase, underscores, no brackets or slashes.
df = pd.read_csv("C:/Users/77192/.vscode/Python/Git-Study/python_small_projects/gym_members_exercise_tracking.csv")
df.columns = df.columns.str.lower().str.replace(' ','_').str.replace('(','',regex=False).str.replace(')','',regex=False).str.replace('/','_',regex=False).str.replace(')','')
print(df.columns)

