import pandas as pd

# Load dataset
df = pd.read_csv(r"C:\Users\ammol\Downloads\Medicaldataset.csv")

# Display basic information
print("Dataset Information:")
print(df.info())

# Summary statistics
print("\nSummary Statistics:")
print(df.describe())

# Count of positive and negative results
print("\nHeart Disease Diagnosis Counts:")
print(df["Result"].value_counts())

# Average values by diagnosis
print("\nAverage Values by Diagnosis:")
print(df.groupby("Result").mean(numeric_only=True))

# Correlation matrix
print("\nCorrelation Matrix:")
print(df.corr(numeric_only=True))
