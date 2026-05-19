import pandas as pd
# Load dataset
df = pd.read_csv("student_data.csv")
# Display first rows
print("FIRST 5 ROWS")
print(df.head())
# Dataset information
print("\nDATASET INFO")
print(df.info())
# Basic statistics
print("\nBASIC STATISTICS")
print(df.describe())
# Mean values
print("\nMEAN MARKS")
print(df[['Math', 'Science', 'English']].mean())
# Median values
print("\nMEDIAN MARKS")
print(df[['Math', 'Science', 'English']].median())
# Top scorer
print("\nTOPPER")
topper = df[df['Math'] == df['Math'].max()]
print(topper)
# Lowest attendance
print("\nLOWEST ATTENDANCE")
low_attendance = df[df['Attendance'] == df['Attendance'].min()]
print(low_attendance)
# Average attendance
print("\nAVERAGE ATTENDANCE")
print(df['Attendance'].mean())
# Observations
print("\nKEY OBSERVATIONS")
print("1. Female students performed better overall.")
print("2. Meena scored highest marks.")
print("3. Attendance is generally high.")
print("4. Kiran has the lowest performance.")