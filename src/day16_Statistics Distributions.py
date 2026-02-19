#Task 1
# Compare Normal, Right-Skewed and Left-Skewed Data

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Make results reproducible
np.random.seed(42)

# ----------------------------
# 1. Create Datasets
# ----------------------------

# Normal Distribution (Heights)
heights = np.random.normal(170, 10, 1000)

# Right-Skewed Distribution (Income)
incomes = np.random.exponential(50000, 1000)

# Left-Skewed Distribution (Easy Exam Scores)
scores = 100 - np.random.exponential(10, 1000)
scores = np.clip(scores, 0, 100)

# Store in dictionary
datasets = {
    "Heights (Normal)": heights,
    "Incomes (Right-Skewed)": incomes,
    "Scores (Left-Skewed)": scores
}

# ----------------------------
# 2. Analyze and Plot
# ----------------------------

for name, data in datasets.items():
    
    df = pd.DataFrame(data, columns=["Values"])
    
    mean = df["Values"].mean()
    median = df["Values"].median()
    
    print("\n", name)
    print("Mean:", round(mean, 2))
    print("Median:", round(median, 2))
    
    # Check skew type
    if mean > median:
        print("This data is Right-Skewed")
    elif mean < median:
        print("This data is Left-Skewed")
    else:
        print("This data is Normally Distributed")
    
    # Plot Histogram
    plt.figure()
    plt.hist(df["Values"], bins=30)
    plt.title(name)
    plt.xlabel("Values")
    plt.ylabel("Frequency")
    plt.show()


#Task 2

# Z-Score Outlier Detection

import numpy as np
import pandas as pd

# 1. Create Sample Dataset
np.random.seed(42)
data = np.random.normal(loc=70, scale=10, size=1000)

# Add extreme values
data = np.append(data, [30, 120])

df = pd.DataFrame(data, columns=["Value"])

# 2. Calculate Mean and Standard Deviation
mean = df["Value"].mean()
std_dev = df["Value"].std()

# 3. Create Z-Score Column
df["z_score"] = (df["Value"] - mean) / std_dev

# 4. Identify Outliers (|Z| > 3)
outliers = df[abs(df["z_score"]) > 3]

# 5. Return Results
print("Mean (μ):", round(mean, 2))
print("Standard Deviation (σ):", round(std_dev, 2))
print("\nOutliers (|Z| > 3):")
print(outliers)
print("\nTotal Outliers:", len(outliers))



#Task3

import numpy as np
import matplotlib.pyplot as plt
np.random.seed(42)

# Skewed population (e.g., incomes)
population = np.random.lognormal(mean=10, sigma=1.0, size=100_000)

sample_means = []

for _ in range(1000):
    sample = np.random.choice(population, size=30, replace=False)
    sample_means.append(sample.mean())
plt.figure(figsize=(7,4))
plt.hist(sample_means, bins=30)
plt.title("Distribution of Sample Means (n = 30, samples = 1000)")
plt.xlabel("Sample Mean")
plt.ylabel("Frequency")
plt.show()

