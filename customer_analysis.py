import pandas as pd

# Project 2 — Customer Data Analysis

# Customer dataset
data = {
    "Customer_ID": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    "Age": [22, 35, 28, 42, 31, 25, 39, 45, 29, 33],
    "Gender": ["M", "F", "M", "F", "F", "M", "M", "F", "M", "F"],
    "City": [
        "Atlanta", "Marietta", "Atlanta", "Kennesaw", "Marietta",
        "Atlanta", "Kennesaw", "Atlanta", "Marietta", "Kennesaw"
    ],
    "Purchases": [4, 7, 3, 9, 6, 5, 8, 10, 2, 6],
    "Total_Spent": [120, 350, 90, 540, 280, 175, 420, 650, 60, 300]
}

customers = pd.DataFrame(data)

# Basic analysis
total_spent = customers["Total_Spent"].sum()
average_spent = customers["Total_Spent"].mean()
highest_spender = customers.loc[customers["Total_Spent"].idxmax()]
average_purchases = customers["Purchases"].mean()
oldest_customer = customers.loc[customers["Age"].idxmax()]
fewest_purchases = customers.loc[customers["Purchases"].idxmin()]

# Spending by city
total_spent_by_city = customers.groupby("City")["Total_Spent"].sum()
average_spent_by_city = customers.groupby("City")["Total_Spent"].mean()

# Purchases by city
total_purchases_by_city = customers.groupby("City")["Purchases"].sum()
average_purchases_by_city = customers.groupby("City")["Purchases"].mean()

# Filter customers
customers_over_300 = customers[customers["Total_Spent"] > 300]
customers_over_5_purchases = customers[customers["Purchases"] > 5]

# Average spending for customers with more than 5 purchases
average_spending_over_5_purchases = customers_over_5_purchases["Total_Spent"].mean()

# Spending per purchase
customers["Spent_Per_Purchase"] = (
    customers["Total_Spent"] / customers["Purchases"]
)

highest_spending_per_purchase = customers.loc[
    customers["Spent_Per_Purchase"].idxmax()
]

# Spending by gender
total_spent_by_gender = customers.groupby("Gender")["Total_Spent"].sum()
average_spent_by_gender = customers.groupby("Gender")["Total_Spent"].mean()

# Spending category
customers["Spending_Category"] = customers["Total_Spent"].apply(
    lambda x: "Low" if x < 200 else "Medium" if x < 400 else "High"
)

# Display final customer analysis
print(customers)

print("\nTotal spent:", total_spent)
print("Average spent:", average_spent)

print("\nHighest spender:")
print(highest_spender)

print("\nAverage purchases per customer:", average_purchases)

print("\nTotal spent by city:")
print(total_spent_by_city)

print("\nAverage spent by city:")
print(average_spent_by_city)

print("\nTotal purchases by city:")
print(total_purchases_by_city)

print("\nCustomers spending over $300:")
print(customers_over_300)

print("\nAverage spending for customers with more than 5 purchases:",
      average_spending_over_5_purchases)

print("\nOldest customer:")
print(oldest_customer)

print("\nAverage purchases by city:")
print(average_purchases_by_city)

print("\nHighest spending per purchase:")
print(highest_spending_per_purchase)

print("\nCustomer with fewest purchases:")
print(fewest_purchases)

print("\nTotal spent by gender:")
print(total_spent_by_gender)

print("\nAverage spent by gender:")
print(average_spent_by_gender)

print("\nFinal spending categories:")
print(customers[["Customer_ID", "Total_Spent", "Spending_Category"]])
