import matplotlib.pyplot as plt

# Monthly sales data
months = ["January", "February", "March", "April", "May"]
sales = [25000, 30000, 28000, 35000, 40000]

# Bar Chart
plt.figure(figsize=(8, 5))
plt.bar(months, sales)
plt.title("Monthly Sales - Bar Chart")
plt.xlabel("Months")
plt.ylabel("Sales (Rs.)")
plt.show()

# Line Graph
plt.figure(figsize=(8, 5))
plt.plot(months, sales, marker='o', linewidth=2)
plt.title("Monthly Sales - Line Graph")
plt.xlabel("Months")
plt.ylabel("Sales (Rs.)")
plt.grid(True)
plt.show()
