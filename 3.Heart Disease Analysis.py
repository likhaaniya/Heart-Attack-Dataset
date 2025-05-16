import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset (Ensure correct file path)
df = pd.read_csv(r"C:\Users\ammol\Downloads\Medicaldataset.csv")

# Handling missing values
df = df.dropna()

# Convert categorical column 'Result' to numerical (0: Negative, 1: Positive)
df["Result"] = df["Result"].map({"negative": 0, "positive": 1})

# Display dataset information
print("Dataset Information:")
print(df.info())

# Summary statistics
print("\nSummary Statistics:")
print(df.describe())

# Count of heart disease diagnoses
print("\nHeart Disease Diagnosis Counts:")
print(df["Result"].value_counts())

# Average values for each diagnosis
print("\nAverage Values by Diagnosis:")
print(df.groupby("Result").mean())

# Correlation matrix
print("\nCorrelation Matrix:")
print(df.corr())

# Visualization: Heart Rate vs. Blood Sugar
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x="Blood sugar", y="Heart rate", hue="Result", alpha=0.7)
plt.title("Heart Rate vs Blood Sugar by Diagnosis")
plt.xlabel("Blood Sugar Level")
plt.ylabel("Heart Rate")
plt.legend(title="Diagnosis", labels=["Negative", "Positive"])
plt.show()

# Visualization: CK-MB vs. Troponin Levels
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x="CK-MB", y="Troponin", hue="Result", alpha=0.7)
plt.title("CK-MB vs Troponin Levels by Diagnosis")
plt.xlabel("CK-MB")
plt.ylabel("Troponin Levels")
plt.legend(title="Diagnosis", labels=["Negative", "Positive"])
plt.show()

# Visualization: Correlation Heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Feature Correlation Heatmap")
plt.show()
