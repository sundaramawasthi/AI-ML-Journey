# Pandas = Python library to work with structured (table-shaped) data.
# Think of it as "Excel inside Python".
# Install once (only needed if it isn't already installed):
# !pip install pandas

import numpy as np
import pandas as pd  # pandas -> real library name, pd -> short alias everyone uses

print("Pandas version:", pd.__version__)


# ---------------------------------------------------------------------------
# 1. WHAT IS A DATAFRAME?
# ---------------------------------------------------------------------------
# A DataFrame is a 2D table: rows + columns + data, exactly like a spreadsheet.

# 1a. Creating a DataFrame from a plain list -> becomes a single column
df_single = pd.DataFrame([14, 27, 39], columns=['Value'])
print("\n--- DataFrame from a list ---")
print(df_single)
print("type ->", type(df_single))  # <class 'pandas.core.frame.DataFrame'>
# The numbers 0, 1, 2 on the left are NOT data, they are the auto-generated index.

# 1b. Creating a DataFrame from a dictionary of lists -> the most common way.
# Each dictionary KEY becomes a COLUMN name, each list becomes that column's values.
data = {
    'Name': ['Aarav', 'Neha', 'Kabir', 'Meera'],
    'Age': [22, 24, 21, 26],
    'Score': [85, 91, 76, 88]
}
df = pd.DataFrame(data)
print("\n--- DataFrame from a dictionary ---")
print(df)


# ---------------------------------------------------------------------------
# 2. FIRST LOOK AT A DATAFRAME (exploration functions)
# ---------------------------------------------------------------------------
print("\n--- head() / tail() ---")
print(df.head(2))   # first 2 rows (default is 5 if you don't pass a number)
print(df.tail(2))   # last 2 rows

print("\n--- shape ---")
print(df.shape)     # (rows, columns) -> (4, 3) here

print("\n--- columns ---")
print(df.columns)   # lists every column name

# Renaming a column: dict is {old_name: new_name}
# inplace=True means "change df itself" instead of returning a new copy.
df.rename(columns={'Score': 'Exam_Score'}, inplace=True)
print("\n--- after renaming Score -> Exam_Score ---")
print(df)

print("\n--- info(): rows, dtypes, non-null counts, memory ---")
df.info()

print("\n--- describe(): quick statistics for numeric columns ---")
print(df.describe())
# count = how many values, mean = average, std = spread, min/25%/50%/75%/max = distribution.
# In ML, describe() is the fastest way to sanity-check a new dataset.


# ---------------------------------------------------------------------------
# 3. SAVING AND LOADING CSV FILES
# ---------------------------------------------------------------------------
csv_path = 'student_data.csv'

# index=False -> don't write the 0,1,2,3 index as an extra column in the file.
df.to_csv(csv_path, index=False)
print(f"\nSaved DataFrame to {csv_path}")

loaded_df = pd.read_csv(csv_path)
print("--- loaded back from CSV ---")
print(loaded_df)

# Typical ML data-loading flow:
# CSV file -> pd.read_csv() -> DataFrame -> clean -> feed into a model


# ---------------------------------------------------------------------------
# 4. SELECTING ROWS AND COLUMNS
# ---------------------------------------------------------------------------
print("\n--- select one column (as a DataFrame) ---")
print(df[['Name']])

print("\n--- select multiple columns ---")
print(df[['Name', 'Exam_Score']])


# ---------------------------------------------------------------------------
# 5 & 6. loc (label based) vs iloc (integer-position based)
# ---------------------------------------------------------------------------
print("\n--- loc: rows where Name == 'Neha' ---")
print(df.loc[df.Name == 'Neha'])

print("\n--- loc: multiple conditions (use & for AND, | for OR, not 'and'/'or') ---")
print(df.loc[(df.Name == 'Neha') & (df.Exam_Score >= 90)])

print("\n--- loc: rows by index LABEL, 0 through 2 (inclusive) ---")
print(df.loc[0:2])

print("\n--- iloc: rows by integer POSITION, positions 0 and 1 ---")
print(df.iloc[0:2])

print("\n--- iloc with a step: start 0, stop before 4, every 2nd row ---")
print(df.iloc[0:4:2])
# Rule of thumb: loc -> labels, iloc -> positions.


# ---------------------------------------------------------------------------
# 7. FILTERING DATA
# ---------------------------------------------------------------------------
print("\n--- filter: Age >= 23 ---")
df_age_filter = df[df['Age'] >= 23]
print(df_age_filter)

print("\n--- filter: Age >= 23 AND Exam_Score >= 85 ---")
print(df[(df['Age'] >= 23) & (df['Exam_Score'] >= 85)])


# ---------------------------------------------------------------------------
# 8. where(): keeps values that pass the condition, replaces the rest
# ---------------------------------------------------------------------------
print("\n--- where(): rows failing the condition become NaN ---")
print(df.where(df['Age'] >= 23))

print("\n--- where() with a replacement value instead of NaN ---")
print(df.where(df['Age'] >= 23, other='Not Eligible'))


# ---------------------------------------------------------------------------
# 9. ADDING NEW COLUMNS AND ROWS
# ---------------------------------------------------------------------------
df['Track'] = ['AI', 'Cybersecurity', 'Data Science', 'AI']
print("\n--- after adding Track column ---")
print(df)

# Column built from another column -> this is a "vectorized operation":
# pandas applies the math to the WHOLE column at once, no manual for-loop needed.
df['Bonus_Score'] = df['Exam_Score'] * 0.10
print("\n--- after adding computed Bonus_Score column (10% of Exam_Score) ---")
print(df)

# Adding a new row: len(df) always points to the next free index.
df.loc[len(df)] = ['Ishaan', 23, 82, 'AI', 8.2]
print("\n--- after adding a new row for Ishaan ---")
print(df)


# ---------------------------------------------------------------------------
# 10. UPDATING VALUES
# ---------------------------------------------------------------------------
# Update by index position: row 0, column 'Exam_Score'.
df.loc[0, 'Exam_Score'] = 89
print("\n--- after updating row 0's Exam_Score to 89 ---")
print(df)

# Update by condition: find the row(s) where Name == 'Aarav', change Exam_Score there.
df.loc[df.Name == 'Aarav', 'Exam_Score'] = 93
print("\n--- after updating Aarav's Exam_Score to 93 by condition ---")
print(df)


# ---------------------------------------------------------------------------
# 11. DELETING ROWS AND COLUMNS
# ---------------------------------------------------------------------------
# Use a copy here so we can demo deletion without losing data the rest of the
# script still needs (Track/Bonus_Score come back into play in section 24).
df_delete_demo = df.copy()

# Delete a row by condition: first find its index, then drop that index.
df_delete_demo = df_delete_demo.drop(df_delete_demo[df_delete_demo.Name == 'Ishaan'].index)
print("\n--- after dropping Ishaan's row (by condition) ---")
print(df_delete_demo)

# Delete a row by its known index label. axis=0 -> rows, axis=1 -> columns.
df_delete_demo = df_delete_demo.drop(1, axis=0)
print("\n--- after dropping index 1 (by index label) ---")
print(df_delete_demo)

# Delete one column.
df_delete_demo = df_delete_demo.drop('Bonus_Score', axis=1)
print("\n--- after dropping the Bonus_Score column ---")
print(df_delete_demo)

# Delete multiple columns at once.
df_delete_demo = df_delete_demo.drop(['Track'], axis=1)
print("\n--- after also dropping the Track column ---")
print(df_delete_demo)


# ---------------------------------------------------------------------------
# 12. RENAMING A COLUMN (again, just the syntax reminder)
# ---------------------------------------------------------------------------
df.rename(columns={'Exam_Score': 'Score'}, inplace=True)
print("\n--- renamed Exam_Score back to Score ---")
print(df.columns.tolist())


# ---------------------------------------------------------------------------
# 13. SORTING DATA
# ---------------------------------------------------------------------------
print("\n--- sort_values ascending (default) ---")
print(df.sort_values('Score'))

print("\n--- sort_values descending ---")
print(df.sort_values('Score', ascending=False))


# ---------------------------------------------------------------------------
# 14-17. WORKING WITH DATES
# ---------------------------------------------------------------------------
df['Enrollment_Date'] = ['2025-02-10', '2025-02-24', '2025-04-12', '2025-05-03', '2025-03-18']
print("\n--- Enrollment_Date dtype BEFORE conversion ---")
print(df['Enrollment_Date'].dtype)  # 'object' -> pandas just sees plain text so far

df['Enrollment_Date'] = pd.to_datetime(df['Enrollment_Date'])
print("--- Enrollment_Date dtype AFTER pd.to_datetime() ---")
print(df['Enrollment_Date'].dtype)  # now a real datetime64 type

# If dates come in a specific written format, e.g. day-month-year, tell pandas
# explicitly so it doesn't guess wrong:
# pd.to_datetime(column, format='%d-%m-%Y')   # %d=day, %m=month, %Y=4-digit year

print("\n--- extracting parts of a date ---")
print("Year:\n", df['Enrollment_Date'].dt.year)
print("Month:\n", df['Enrollment_Date'].dt.month)
print("Day:\n", df['Enrollment_Date'].dt.day)
print("Day name:\n", df['Enrollment_Date'].dt.day_name())

df['Month'] = df['Enrollment_Date'].dt.month
print("\n--- new Month column extracted from Enrollment_Date ---")
print(df[['Name', 'Enrollment_Date', 'Month']])

print("\n--- adding 45 days to every enrollment date ---")
print(df['Enrollment_Date'] + pd.Timedelta(days=45))


# ---------------------------------------------------------------------------
# 18. HANDLING MISSING VALUES
# ---------------------------------------------------------------------------
# Simulate a missing value the way real data often has one.
df.loc[df.Name == 'Kabir', 'Score'] = np.nan
print("\n--- introduced a missing Score for Kabir ---")
print(df[['Name', 'Score']])

print("\n--- isnull(): True/False map of missing values ---")
print(df.isnull())

print("\n--- isnull().sum(): missing-value COUNT per column ---")
print(df.isnull().sum())

print("\n--- fillna(0): replace NaN with 0 ---")
print(df['Score'].fillna(0))

# Filling with 0 isn't always meaningful for ML - filling with the column's
# own mean is usually a safer default:
print("\n--- fillna(mean): replace NaN with the column average ---")
print(df['Score'].fillna(df['Score'].mean()))


# ---------------------------------------------------------------------------
# 19. value_counts(): how many times does each value appear?
# ---------------------------------------------------------------------------
print("\n--- value_counts() on Month ---")
print(df['Month'].value_counts())

print("\n--- value_counts() after filtering to Month == 2 ---")
print(df[df['Month'] == 2]['Month'].value_counts())


# ---------------------------------------------------------------------------
# 20. GROUPBY: split into groups, then aggregate each group
# ---------------------------------------------------------------------------
# Need real Score numbers for the demo, so fill the NaN we made above first.
df['Score'] = df['Score'].fillna(df['Score'].mean())

print("\n--- total Score per Month ---")
print(df.groupby('Month')['Score'].sum())

print("\n--- multiple aggregations at once: mean Score + count of students per Month ---")
print(df.groupby('Month').agg({'Score': 'mean', 'Name': 'count'}))


# ---------------------------------------------------------------------------
# 21. CONCAT: stack DataFrames together
# ---------------------------------------------------------------------------
df1 = pd.DataFrame({'ID': [11, 12, 13], 'Name': ['A', 'B', 'C']})
df2 = pd.DataFrame({'ID': [11, 12, 12, 15], 'Score': [84, 92, 78, 81]})

print("\n--- concat axis=0: stack rows (one DataFrame below the other) ---")
print(pd.concat([df1, df1], axis=0, ignore_index=True))

print("\n--- concat axis=1: stack columns (side by side) ---")
print(pd.concat([df1, df2], axis=1))


# ---------------------------------------------------------------------------
# 22. MERGE: SQL-style JOIN using a shared column
# ---------------------------------------------------------------------------
print("\n--- inner merge on 'ID': only IDs present in BOTH tables survive ---")
print(pd.merge(df1, df2, how='inner', on='ID'))

# If the join column has different names in each table, use left_on/right_on:
# pd.merge(df1, df2, how='inner', left_on='Student_ID', right_on='ID')


# ---------------------------------------------------------------------------
# 23. TWO EQUIVALENT WAYS TO FILTER: boolean indexing vs query()
# ---------------------------------------------------------------------------
print("\n--- Method 1: boolean indexing ---")
print(df[(df['Month'] == 2) & (df['Score'] > 80)])

print("\n--- Method 2: query() - often easier to read for complex conditions ---")
print(df.query("Month == 2 and Score > 80"))


# ---------------------------------------------------------------------------
# 24. MINI PROJECT: full ML-style workflow on this same dataset
# ---------------------------------------------------------------------------
# Raw dataset -> read_csv -> understand -> clean -> select features -> ready for ML
print("\n=== Mini workflow: preparing X (features) and y (target) ===")

workflow_df = df.copy()
print(workflow_df.head())
workflow_df.info()
print(workflow_df.describe())
print("Missing values per column:\n", workflow_df.isnull().sum())

# X -> the input features the model learns from.
# y -> the target/output the model tries to predict.
X = workflow_df[['Age', 'Month']]
y = workflow_df['Score']

print("\nFeatures (X):\n", X)
print("\nTarget (y):\n", y)
# From here X and y would be handed to a scikit-learn model to train on.
