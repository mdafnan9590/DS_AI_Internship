import pandas as pd
import matplotlib.pyplot
import seaborn as sb
#Improve plot appearance

#---------------------------------------------------------

#STEP 2 Load / Create Dataset

# (In real projects: df = pd.read_csv("dataset.csv"))

#-------------------------------------------------------------


data = {
         "Age": [25,30,35,40, 28, 32,45,50,23,36,29,41],

        "Salary": [30000, 40000, 50000,65000,42000,48000, 80000, 90000, 28000, 52000,46000, 70000],
         "Department": ["IT", "HR", "IT", "Finance", "HR", "IT", "Finance", "Finance", "HR", "IT", "HR", "Finance"],

        "Experience": [1,3,7,10,2,5,15,20,1,8,4,12],

        "Gender": ["M", "F", "M","M", "F","F", "M", "M", "F","F", "M", "F"]
}
df = pd.DataFrame(data)


"""understand data age, salary, experience of the company, age nothing to do, experince high, dalary high"""

#-----------------------------------------------------------------------

# TOPIC 1 DATASET INSPECTION

#----------------------------------------------------------------------

#View first and last rows

print("\nFirst 5 rows:")

print(df.head())




import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import skew, kurtosis

# Sample dataset (replace with your actual dataset)
np.random.seed(42)
df = pd.DataFrame({
    'Price': np.random.lognormal(mean=12, sigma=0.5, size=1000),
    'City': np.random.choice(['New York', 'Los Angeles', 'Chicago', 'Houston'], 
                             size=1000, p=[0.4, 0.3, 0.2, 0.1])
})

# -------------------------
# Histogram + KDE (Price)
# -------------------------
plt.figure()
plt.hist(df['Price'], bins=30, density=True)
df['Price'].plot(kind='kde')
plt.title("Histogram with KDE - Price")
plt.xlabel("Price")
plt.ylabel("Density")
plt.show()

# Skewness and Kurtosis
print("Skewness:", skew(df['Price']))
print("Kurtosis:", kurtosis(df['Price']))

# -------------------------
# Count Plot (City)
# -------------------------
city_counts = df['City'].value_counts()

plt.figure()
plt.bar(city_counts.index, city_counts.values)
plt.title("Count Plot - City")
plt.xlabel("City")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.show()

print(city_counts)




#TASK 1 : The Pattern Finder

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample housing dataset
df = pd.read_excel("Housing_with_City.xlsx")

# 1. Histogram with KDE

sns.histplot(df["price"], kde=True)
plt.title("Distribution of Housing prices")
plt.xlabel("price")
plt.ylabel("Frequency")
plt.show()

# 2. Skewness and Kurtosis
print("Skewness:", df["price"].skew())
print("Kurtosis:", df["price"].kurt())

# 3. Count Plot for categorical column
sns.countplot(x="City", data=df)
plt.title("City Frequency")
plt.show()


#TASK 2: The Relationship Map


plt.subplot(1,2,1)
plt.scatter(x="area", y='price', data=df)
plt.title('Area vs Price')
plt.xlabel('Area')
plt.ylabel('Price')
plt.show()
plt.subplot(1,2,2)
sns.boxplot(x=df['furnishingstatus'],y=df['price'])
plt.xlabel('Furnishing Status')
plt.ylabel('Price')
plt.show()
plt.tight_layout()
print("AS FURNISHING STATUS INCREASES PRICE OF HOUSE ALSO INCREASES")


#TASK 3: The Pattern Finder


plt.subplot(1,2,1)
corr_matrix=df.corr(numeric_only=True)
print(corr_matrix)
print("There are no two variables with correlation score higher than 0.8")
sns.heatmap(corr_matrix,annot=True)
plt.show()
plt.subplot(1,2,2)
sns.boxplot(x=df ['price'])
plt.xlabel('Price')
plt.show()
plt.tight_layout()


