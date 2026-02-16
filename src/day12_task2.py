#task2
# dashboard.py

import matplotlib.pyplot as plt

# Data for bar chart
categories = ['Electronics', 'Clothing', 'Home']
sales = [300, 450, 200]

# Data for line plot (example monthly trend)
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
trend_sales = [200, 250, 300, 280, 350]

# Create first subplot (1 row, 2 columns, position 1)
plt.subplot(1, 2, 1)
plt.bar(categories, sales)
plt.title("Sales by Category")
plt.xlabel("Product Category")
plt.ylabel("Sales")

# Create second subplot (1 row, 2 columns, position 2)
plt.subplot(1, 2, 2)
plt.plot(months, trend_sales, marker='o')
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")

# Prevent overlapping
plt.tight_layout()

# Show the dashboard
plt.show()

