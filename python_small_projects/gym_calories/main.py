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
# cor = df.corr(numeric_only=True)['calories_burned'].drop('calories_burned').sort_values()
# negatives = cor[cor < 0]
# near_zero = cor[cor.abs() < 0.1]
# dominate = cor.abs().idxmax()
# print(f'Negatives : {list(negatives.index)}')
# print(f'Near zeros : {list(near_zero.index)}')
# print(f'Dominate : {dominate} ({cor[dominate]:.2f})')

# Task 5. Add a column calories_per_hour = calories divided by session duration. 
    # Now redo Task 2 using this instead. Does the ranking of workout types change?
df['calories_per_hour'] = df['calories_burned'] / df['session_duration_hours']
# t = df.groupby('workout_type')['calories_per_hour'].agg(n='size',mean='mean',median='median',std='std').round(1).sort_values('mean',ascending=False)
# print(t)

# Task 6. Compare mean session duration by workout type. Are the four groups even training for comparable lengths of time?
# mean = (df.groupby('workout_type')['session_duration_hours']
#         .agg(n='size',hours='mean',median='median',std='std',
#              q25 = lambda s : s.quantile(0.25), q75 = lambda s : s.quantile(.75), min='min',max='max')
#         .assign(minutes = lambda h : h.hours * 60)
#         .round(3)
#         .sort_values('hours',ascending=False))
# print(mean)

# Task 7. Bin session duration into four buckets, then compare workout types within each bucket. 
    # Does any type win consistently across all four?
df['duration_bucket'] = pd.qcut(df.session_duration_hours,4,labels=['Q1','Q2','Q3','Q4'])
# counts = pd.crosstab(df.duration_bucket,df.workout_type)
# print(f'Cell sizes: \n {counts}')
# rate = df.pivot_table(index='duration_bucket',columns='workout_type',values='calories_per_hour',aggfunc='mean',observed=True).round(2)
# print(f'Mean per workout type: \n {rate}')
# rank = rate.rank(axis=1,ascending=False).astype(dtype=int)
# print("Rank within each bucket (1 = highest):\n", rank, "\n")

# print("Winner per bucket:", rate.idxmax(axis=1).tolist())
# print("Spread within each bucket:", (rate.max(axis=1) - rate.min(axis=1)).round(1).tolist())

# consistent = (rank == 1).all()                     # all() down each column
# winner = consistent[consistent].index.tolist()
# print("Wins every bucket:", winner if winner else "none")

# Task 8. For each experience level, compute mean session duration, 
    # mean weekly frequency, and mean calories burned. Look at all three together.
# tab = (df.groupby('experience_level').agg(
#         n = ('experience_level','size'),
#         hours = ('session_duration_hours','mean'),
#         freq = ('workout_frequency_days_week','mean'),
#         cal_per_hour = ('calories_burned','mean'),
# ).round(2))
# tab['weekly_hours'] = (tab.hours * tab.freq).round(2)
# tab['cal_per_week'] = (tab.cal_per_hour * tab.weekly_hours).round(2)
# print(tab)

# Task 9. Experience level clearly relates to calories. But is that because experienced people burn faster, or because they train longer? 
    # Compare calories_per_hour by experience level and see whether the gap survives.
    # Hint: if the raw gap is large and the per-hour gap is small, duration was doing the work.
tab = pd.crosstab(df.experience_level,df.calories_per_hour)
print(tab)