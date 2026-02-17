# Task 1

import pandas as pd

# Sample dataset
df = pd.DataFrame({
    "Transmission": ["Automatic", "Manual", "Automatic", "Manual"],
    "Color": ["Red", "Blue", "Green", "Red"]
})

print("Original Data:")
print(df)

df["Transmission"] = df["Transmission"].map({
    "Automatic": 1,
    "Manual": 0
})
df = pd.get_dummies(df, columns=["Color"], drop_first=True)

print("\nEncoded Data:")
print(df)



#Task 2

data = {
"Age": [20,35,40,45,50],
"Salary": [20000, 35000, 23300, 10000,50000]}
df = pd.DataFrame(data)
print(df)
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaled_data = scaler.fit_transform(df)
print(scaled_data)
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
normalised_data = scaler.fit_transform(df)
print(normalised_data)
import matplotlib.pyplot as plt

# Before scaling
plt.hist(df["Salary"])
plt.title("Salary Before Scaling")
plt.show()

#After Standardization
plt.hist(scaled_data[:, 1])
plt.title("Salary After Standardization")
plt.show()


#Task3

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
# Input values
X = np.array([1, 2, 3, 4, 5])
X = X.reshape(-1, 1)   # Make it 2D (required for sklearn)

# Output values (curved)
y = np.array([1, 4, 9, 16, 25])
plt.scatter(X, y)
plt.title("Curved Data")
plt.show()
model1 = LinearRegression()
model1.fit(X, y)

r2_normal = model1.score(X, y)

print("R2 without polynomial:", r2_normal)
poly = PolynomialFeatures(degree=2)

X_poly = poly.fit_transform(X)
model2 = LinearRegression()
model2.fit(X_poly, y)

r2_poly = model2.score(X_poly, y)

print("R2 with polynomial:", r2_poly)