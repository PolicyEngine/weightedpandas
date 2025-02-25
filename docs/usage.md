# Usage Guide

## Creating Weighted Objects

WeightedPandas provides two main classes: `WeightedSeries` and `WeightedDataFrame`, which extend pandas' Series and DataFrame classes to support weighted operations.

### Creating a WeightedSeries

```python
from weightedpandas import WeightedSeries

# Create a weighted series with explicit weights
data = [1, 2, 3, 4, 5]
weights = [5, 4, 3, 2, 1]
ws = WeightedSeries(data, weights=weights)

# Create a weighted series with uniform weights
ws_uniform = WeightedSeries(data)  # All weights default to 1.0
```

### Creating a WeightedDataFrame

```python
from weightedpandas import WeightedDataFrame

# Create a weighted dataframe with explicit weights
df_data = {
    'A': [1, 2, 3, 4, 5],
    'B': [5, 4, 3, 2, 1]
}
weights = [5, 4, 3, 2, 1]
wdf = WeightedDataFrame(df_data, weights=weights)

# Create a weighted dataframe with uniform weights
wdf_uniform = WeightedDataFrame(df_data)  # All weights default to 1.0
```

### Helper Functions

For convenience, you can use the following helper functions:

```python
from weightedpandas import weighted_series, weighted_dataframe

# These are equivalent to the constructor calls
ws = weighted_series(data, weights=weights)
wdf = weighted_dataframe(df_data, weights=weights)
```

## Calculating Weighted Statistics

### Basic Statistics

```python
# Weighted sum
ws.sum()

# Weighted mean
ws.mean()

# Weighted variance and standard deviation
ws.var()
ws.std()
```

### Quantiles and Percentiles

```python
# Weighted median (equivalent to 50th percentile)
ws.median()

# Weighted quantiles
ws.quantile(0.25)  # 25th percentile
ws.quantile([0.25, 0.5, 0.75])  # Multiple quantiles
```

### Correlation and Covariance

```python
# Weighted correlation between columns
wdf.corr()

# Weighted covariance between columns
wdf.cov()
```

## Operations and Weight Preservation

An important feature of WeightedPandas is that weights are preserved through operations:

```python
# Create a weighted series
ws = WeightedSeries([1, 2, 3, 4, 5], weights=[5, 4, 3, 2, 1])

# Perform operations
ws2 = ws * 2 + 1

# Weights are preserved
print(ws2.weights)  # Same as original weights: [5, 4, 3, 2, 1]
```

## Working with Regular Pandas Objects

WeightedPandas objects can interoperate with regular pandas objects:

```python
import pandas as pd
from weightedpandas import WeightedSeries

# Regular pandas Series
s = pd.Series([1, 2, 3, 4, 5])

# WeightedSeries
ws = WeightedSeries([6, 7, 8, 9, 10], weights=[5, 4, 3, 2, 1])

# Operations between different types
result = ws + s  # Result is a WeightedSeries with preserved weights
```

## How Weights Are Applied

In weighted calculations:

- `sum()`: Each value is multiplied by its weight before summing
- `mean()`: The weighted sum divided by the sum of weights
- `var()` and `std()`: Each squared deviation is weighted
- `quantile()`: The quantile is determined from the weighted cumulative distribution