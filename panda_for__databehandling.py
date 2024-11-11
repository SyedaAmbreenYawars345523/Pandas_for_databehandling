import pandas as pd


#fillna(): Fills missing values with a specified value (mean, median, etc.).
#dropna(): Drops rows with missing values.

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', None],
    'Age': [25, 30, 35, None, 40],
    'City': ['New York', 'Los Angeles', None, 'Chicago', 'Miami']
}

df = pd.DataFrame(data)

print("original Dataframe:")
print(df)


# Cleaning: Handling missing values
# Fill missing 'Age' with the mean of the column

df['Age'] = df['Age'].fillna(df['Age'].mean())
print("\n\nFilled misisng value of age in DataFrame:")
print(df)

# now removing the rows which have missing data:
# here missing value in name and city

df = df.dropna(subset=['Name', 'City'])

print("\n\nCleaned DataFrame:")
print(df)


#-------------------------------------------------#
# Data transformation and Aggregation 
#-------------------------------------------------#

# Adding a new column based on a transformation
df['Age_after_5_years'] = df['Age'] + 5
# checking dataframe now
print("\n\nUpgraded Dataframe after column addition")
print(df)

# Adding a new row i.e data to the dataframe:


#For adding a single row, loc[] is typically the most efficient and clear method.
#append() is deprecated,so it's better to use concat() or loc[] for adding rows.


## loc[] implementation:

new_row = {'Name': 'Charles', 'Age': 40, 'City': 'Miami','Age_after_5_years': 45}
df = df.reset_index(drop=True)
#The reason resetting the index before adding a row works is due to how pandas handles row indexing internally.

#Why It Works:
#Indexing and Row Addition:

#df.loc[len(df)] is used to add a new row at the end of the DataFrame.
#When you reset the index using df.reset_index(drop=True), you are reassigning the index to be a simple sequential number starting from 0. This is crucial because pandas uses the index to identify the position where new data should be added.
#By resetting the index, you ensure that the index starts from 0 and goes sequentially, allowing len(df) to give the next available index value correctly (i.e., the row number where the new row will be inserted).
#Issue Before Resetting Index:

#Without resetting the index, if your DataFrame has custom or non-sequential indices (for example, if you added rows previously or performed operations that change the index), the len(df) could give an unexpected result.
#If the index is non-sequential or contains gaps, df.loc[len(df)] might not add the new row in the correct place because it’s interpreting len(df) based on the current index, not necessarily the next available index.

df.loc[len(df)] = new_row
print("\n\nUpgraded Dataframe after row addition using loc[]")
print(df)


#concat():

new_row_2 = pd.DataFrame([{'Name': 'Charlott', 'Age': 30, 'City': 'Miami','Age_after_5_years': 35}])

#new_row_2_df = pd.DataFrame(new_row_2)

#df = df.reset_index(drop=True)
df = pd.concat([df, new_row_2], ignore_index=True)
print("\n\nUpdated dataFrame after addding row using concat()")
print(df)



## aggregating data
sales_data = {
    'City': ['New York', 'New York', 'Los Angeles', 'Chicago', 'Chicago'],
    'Sales': [200, 300, 150, 400, 500]
}
sales_df = pd.DataFrame(sales_data)
print("\n\nSales DataFrame is: ")
print(sales_df)

# Aggregating sales by city (sum of sales)
agg_sales = sales_df.groupby('City').agg({'Sales': 'sum'}).reset_index()
print("\n\nAggregated Sales Data:")
print("\nAgg sales are:")
print(agg_sales)

agg_ages = df.groupby('City').agg({'Age_after_5_years':'mean'}).reset_index()
print("\n\nAggregated Age Data:")
print("\nAgg agess are:")
print(agg_ages)


#--------------------------------#
#Merging joining pivot table
#--------------------------------#

# Sample datasets for merging
employee_data = {
    'EmployeeID': [1, 2, 3],
    'Name': ['Alice', 'Bob', 'Charlie'],
    'DepartmentID': [101, 102, 103]
}


department_data = {
    'DepartmentID': [101, 102, 103],
    'DepartmentName': ['HR', 'Engineering', 'Finance']
}


df_employees = pd.DataFrame(employee_data)
df_departments = pd.DataFrame(department_data)

merged_df = pd.merge(df_employees, df_departments, on = 'DepartmentID', how='inner')
#pd.merge(): Combines two DataFrames based on a common column.

print("\n\nMerged Dataframe:")
print(merged_df)

# Creating a pivot table
sales_data = {
    'City': ['New York', 'New York', 'Los Angeles', 'Chicago', 'Chicago'],
    'Product': ['A', 'B', 'A', 'A', 'B'],
    'Sales': [200, 300, 150, 400, 500]
}

sales_data_df =pd.DataFrame(sales_data)

# Pivot table: Sum of sales by City and Product

pivot_df = sales_data_df.pivot_table(values='Sales', index='City', columns='Product', aggfunc='sum', fill_value=0)
# pivot_table(): Creates a pivot table that summarizes data.

print("\n\nPivot Table:")
print(pivot_df)