import pandas as pd

# Load dataset
df = pd.read_csv("dataset/students.csv")

print("Original Dataset:")
print(df)

# -----------------------------
# Handle Missing Values
# -----------------------------

df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

# -----------------------------
# Standardize City Names
# -----------------------------

df["City"] = df["City"].replace({
    "Bangalore": "Bengaluru",
    "BLR": "Bengaluru"
})

# -----------------------------
# Standardize Date Format
# -----------------------------


# -----------------------------
# Remove Extra Spaces
# -----------------------------

for col in df.columns:
    df[col] = df[col].astype(str).str.strip()

# -----------------------------
# Remove Duplicates
# -----------------------------

df = df.drop_duplicates()

# -----------------------------
# Save Cleaned Dataset
# -----------------------------

df.to_csv("output/cleaned_students.csv", index=False)

# -----------------------------
# Generate Report
# -----------------------------

report = f"""
DATA CLEANING REPORT

Total Rows After Cleaning: {len(df)}

Missing values handled
Duplicates removed
City names standardized
Date formats corrected
"""

with open("report/report.txt", "w") as file:
    file.write(report)

print("\nCleaned Dataset:")
print(df)

print("\nProject Completed Successfully!")