import pandas as pd

# 1. Creating a DataFrame
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Age": [25, 30, 35, 40, 28],
    "Salary": [50000, 60000, 75000, 80000, 62000],
    "Department": ["HR", "IT", "Finance", "IT", "HR"]
}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

# 2. Selecting Specific Columns
print("\nSelecting 'Name' and 'Salary' columns:")
print(df[["Name", "Salary"]])

# 3. Filtering Rows (Employees with Salary > 60,000)
filtered_df = df[df["Salary"] > 60000]
print("\nEmployees with Salary > 60,000:")
print(filtered_df)

# 4. Sorting by Age
sorted_df = df.sort_values(by="Age", ascending=True)
print("\nDataFrame Sorted by Age:")
print(sorted_df)

# 5. Grouping by Department and Finding Average Salary
grouped = df.groupby("Department")["Salary"].mean()
print("\nAverage Salary by Department:")
print(grouped)

# 6. Adding a New Column (Bonus = 10% of Salary)
df["Bonus"] = df["Salary"] * 0.1
print("\nDataFrame with Bonus Column:")
print(df)

# 7. Handling Missing Values (Filling NaN with Default Value)
df.loc[5] = ["Frank", None, 72000, "Finance", None]  # Adding a row with missing value
df_filled = df.fillna({"Age": df["Age"].mean(), "Bonus": 0})
print("\nDataFrame after Handling Missing Values:")
print(df_filled)

# 8. Writing Data to CSV
df.to_csv("employee_data.csv", index=False)
print("\nData written to 'employee_data.csv'")

# 9. Reading from CSV
df_read = pd.read_csv("employee_data.csv")
print("\nData read from 'employee_data.csv':")
print(df_read)
