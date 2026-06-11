#SHOW CSV 
import pandas as pd

df = pd.read_csv("student_datacsv.csv")
# FIRST FIVE ROW
print(df.head())

# DATASET SHAPE TELL HOOW MANY ROWS AND COLUMNS IT CONTAIN
print("\nDATASET SHAPE:")
print(df.shape)

# HOW MANY COLUMN DATA SET CONTAIN
print("\nCOLUMN NAMES:")
print(df.columns)

# TELL HOW MANY STUDENT ARE BURNOUT
print("\nBURNOUT COUNT:")
print(df['Burnout'].value_counts())

# TO COUNT AVERAGE STUDY HOURS , SLEEP, MAX ATTENDANCE
print("\nDATASET SUMMARY:\n")
print(df.describe())

#ANY MISSING VALUE IN IT
print("\nMISSING VALUES:\n")
print(df.isnull().sum())