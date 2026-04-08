#  Pandas Complete Learning Guide (With Examples)

##  Introduction to Pandas

Pandas is a powerful Python library used for handling structured data.
It is widely used in: - Data Analysis - Machine Learning preprocessing -
Data Cleaning

It mainly provides two data structures: - Series (1D) - DataFrame (2D)

------------------------------------------------------------------------

# 1. Series

## Definition

A Series is a one-dimensional labeled array capable of holding any data
type.

##  Example

``` python
import pandas as pd
s = pd.Series([1,2,3])
print(s)
```

##  Output

    0    1
    1    2
    2    3
    dtype: int64

 It contains: - Index (0,1,2) - Values (1,2,3)

------------------------------------------------------------------------

#  2. DataFrame

##  Definition

A DataFrame is a two-dimensional table with rows and columns.

##  Example

``` python
df = pd.DataFrame({
    'A':[1,2,3],
    'B':[4,5,6],
    'C':[7,8,9]
})
print(df)
```

##  Output

       A  B  C
    0  1  4  7
    1  2  5  8
    2  3  6  9

------------------------------------------------------------------------

#  3. Viewing Data

## head()

``` python
df.head()
```

 Shows first 5 rows

## tail()

``` python
df.tail()
```

 Shows last 5 rows

------------------------------------------------------------------------

#  4. Data Information

## info()

``` python
df.info()
```

 Gives: - Number of rows - Column names - Data types - Memory usage

------------------------------------------------------------------------

#  5. Statistical Summary

## describe()

``` python
df.describe()
```

 Output includes: - mean → average - std → spread of data - min/max →
smallest/largest - quartiles → distribution

------------------------------------------------------------------------

#  6. Column Access

``` python
df['A']
```

 Returns a Series

------------------------------------------------------------------------

#  7. Indexing

## loc (Label-based)

``` python
df.loc[1]
df.loc[1, 'A']
```

## iloc (Position-based)

``` python
df.iloc[1]
df.iloc[1, 0]
```

###  Difference

-   loc → uses index label
-   iloc → uses position

------------------------------------------------------------------------

#  8. Filtering

``` python
df[df['C'] > 7]
```

 Select rows where condition is true

------------------------------------------------------------------------

#  9. Column Operations

``` python
df['C'] = df['A'] + df['B']
```

 Creates a new column

------------------------------------------------------------------------

#  10. Dropping Columns

``` python
df = df.drop('C', axis=1)
```

 Removes column

------------------------------------------------------------------------

#  11. Sorting

``` python
df.sort_values('A')
```

 Sorts rows based on column A

------------------------------------------------------------------------

#  12. GroupBy

##  Definition

Group data based on a column and apply aggregation

##  Example

``` python
df2 = pd.DataFrame({
    "team":["A","B","C","D"],
    "Scores":[22,55,33,45]
})

df2.groupby("team").sum()
```

------------------------------------------------------------------------

#  13. Merging DataFrames

##  Example

``` python
lf = pd.DataFrame({"id":[1,2], "Val":[10,20]})
rt = pd.DataFrame({"id":[1,2], "Val2":[100,200]})

pd.merge(lf, rt, on="id")
```

Combines based on common column

------------------------------------------------------------------------

#  14. Apply Function

``` python
df3["A"].apply(lambda x: x*5)
```

 Applies function to each element

------------------------------------------------------------------------

#  15. String Operations

``` python
df3['char'].str.upper()
```

 Converts to uppercase

------------------------------------------------------------------------

#  16. Date Handling

``` python
dates = pd.date_range("2024-01-01", periods=3)
df = pd.DataFrame({'dates': dates})
```

## Extracting Components

``` python
df['dates'].dt.year
df['dates'].dt.month
df['dates'].dt.day
df['dates'].dt.day_name()
```

------------------------------------------------------------------------

#  17. Pivot Table

``` python
pd.pivot_table(df, values="C", index="A", columns="B")
```

 Reshapes data into summary table

------------------------------------------------------------------------

# 18. File Handling

## Save CSV

``` python
df.to_csv('test.csv', index=False)
```

## Read CSV

``` python
pd.read_csv('test.csv')
```

------------------------------------------------------------------------

# Final Summary

-   Series → single column
-   DataFrame → table
-   loc/iloc → data selection
-   groupby → aggregation
-   merge → join tables
-   apply → custom logic
-   dt → date extraction

------------------------------------------------------------------------

# Conclusion

This covers: ✔ Data creation\
✔ Data analysis\
✔ Data transformation\
✔ File handling

 This is a strong foundation for Data Science & ML
