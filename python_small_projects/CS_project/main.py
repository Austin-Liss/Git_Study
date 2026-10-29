import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('C:/Users/77192/.vscode/Python/Git-Study/python_small_projects/CS_project/cs_students.csv')
df.columns = df.columns.str.lower().str.replace(' ','_')
fig,axes = plt.subplots(figsize=(9,5))

# Task 2 : Find the useless columns
useless = df.nunique().idxmin()
# print(f'The column with the least unique value is column [{useless}] : [{df[useless].unique()[0]}]')

# Task 3 : Hunt for duplicate rows
drop = df.columns.drop('student_id')
dup = df.duplicated(subset=drop)
alloc = df.duplicated(subset=drop,keep=False)
# print(f'Duplicated rows in dataset [{dup.sum()}], {(dup.sum()/df.shape[0])*100:.1f}% out of 180')
# print(f'Rows included : [{alloc.sum()}] from {df[alloc].drop_duplicates(subset=drop).shape[0]} distinct records')
# print(f'Flagged ids: {df.loc[dup,'student_id'].tolist()}')
df_clean = df.drop_duplicates(subset=drop).reset_index(drop=True)
# print(f'\nRows changes from {len(df)} -> {len(df_clean)}')
# print(f'Gpa mean changes from {df.gpa.mean():.2f} -> {df_clean.gpa.mean():.2f}')
# print(f'Age mean changes from {df.age.mean():.2f} -> {df_clean.age.mean():.2f}')

# Task 4 : Check the age distribution
# age = df.age.value_counts().sort_index()
# axes.hist(df.age,bins=range(20,39),color='C0',edgecolor='white')
# axes.set_xlabel('Age')
# axes.set_ylabel('Students')
# axes.grid(axis='y', alpha=0.3) 
# axes.set_axisbelow(True)
# plt.show()

# Task 5 : Encode the skill columns
SKILLS = ['python','sql','java']
LEVELS = {'Weak':1,'Average':2,'Strong':3}
for skill in SKILLS :
    df[skill + '_n'] = df[skill].map(LEVELS)
print(df[[c + '_n' for c in SKILLS]].isna().sum())