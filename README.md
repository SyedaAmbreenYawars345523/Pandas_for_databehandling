## Practice repository for data handling using Pandas

In this repository we cover pandas step by step, starting from the basics to more advanced concepts, while focusing on practical examples.

## Goals:
1. Load data, handle missing values, and clean the data for analysis.
2. Transform data and perform aggregation.
3. Merge and join datasets and create pivot tables.


## Important key functions:
1. Data Loading and Cleaning:

pd.read_csv(), pd.read_excel(), pd.read_sql() to load data.
df.head(), df.tail(), df.info(), df.describe() to inspect data.
df.isnull(), df.dropna(), df.fillna(), df.replace() to clean data.


2. Data Transformation:

df.apply(), df.map(), df.applymap() to apply functions.
df.astype(), df.astype('category') to change data types.


3. Aggregation and Grouping:

df.groupby(), df.agg(), df.transform() for grouping and aggregation.
df.groupby().agg(), df.groupby().size() for simple aggregation.


4. Merging and Joining:

pd.merge() for merging DataFrames.
df.join() for joining DataFrames by index.
df.concat() for concatenating DataFrames along rows/columns.


5. Pivoting and Reshaping:

df.pivot(), df.pivot_table(), df.melt(), df.stack(), df.unstack() for reshaping data.