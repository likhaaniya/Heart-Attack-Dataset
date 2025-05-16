import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv(r"C:\Users\ammol\Downloads\Medicaldataset.csv")

# Set style
sns.set_style("whitegrid")

# Plot distribution of heart rate by diagnosis
plt.figure(figsize=(8, 6))
sns.histplot(data=df, x="Heart rate", hue="Result", kde=True, bins=30)
plt.title("Heart Rate Distribution by Diagnosis")
plt.xlabel("Heart Rate")
plt.ylabel("Count")
plt.legend(title="Diagnosis", labels=["Negative", "Positive"])
plt.show()

# Scatter plot of blood sugar vs. troponin levels
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x="Blood sugar", y="Troponin", hue="Result", alpha=0.7)
plt.title("Blood Sugar vs Troponin Levels by Diagnosis")
plt.xlabel("Blood Sugar")
plt.ylabel("Troponin Levels")
plt.legend(title="Diagnosis", labels=["Negative", "Positive"])
plt.show()
