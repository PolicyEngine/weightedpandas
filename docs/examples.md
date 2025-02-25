# Examples

This page contains various examples demonstrating how to use WeightedPandas for different applications.

## Basic Usage

The following example demonstrates the basic usage of WeightedSeries and WeightedDataFrame:

```python
import pandas as pd
import numpy as np
from weightedpandas import WeightedSeries, WeightedDataFrame

# Create a weighted series
data = [1, 2, 3, 4, 5]
weights = [5, 4, 3, 2, 1]
ws = WeightedSeries(data, weights=weights)

# Calculate basic weighted statistics
print(f"Weighted sum: {ws.sum()}")
print(f"Weighted mean: {ws.mean()}")
print(f"Weighted median: {ws.median()}")
print(f"Weighted standard deviation: {ws.std()}")

# Create a weighted dataframe
df_data = {
    'A': [1, 2, 3, 4, 5],
    'B': [5, 4, 3, 2, 1]
}
wdf = WeightedDataFrame(df_data, weights=weights)

# Calculate statistics for each column
print("Weighted column means:")
print(wdf.mean())

# Calculate weighted correlation between columns
print("Weighted correlation:")
print(wdf.corr())
```

## Survey Data Analysis

Weighted statistics are commonly used in survey data analysis, where each respondent may represent a different number of people in the population:

```python
from weightedpandas import WeightedDataFrame

# Sample survey data
survey_data = {
    'age': [25, 35, 45, 55, 65],
    'income': [30000, 45000, 55000, 65000, 75000],
    'satisfaction': [3, 4, 5, 4, 3]
}

# Survey weights (e.g., based on demographic representation)
survey_weights = [2.5, 1.5, 1.0, 0.8, 0.5]

# Create weighted dataframe
survey_df = WeightedDataFrame(survey_data, weights=survey_weights)

# Calculate weighted statistics
print("Weighted average age:", survey_df['age'].mean())
print("Weighted average income:", survey_df['income'].mean())
print("Weighted average satisfaction:", survey_df['satisfaction'].mean())

# Calculate weighted correlation between income and satisfaction
income_satisfaction_corr = survey_df[['income', 'satisfaction']].corr().iloc[0, 1]
print(f"Weighted correlation between income and satisfaction: {income_satisfaction_corr:.3f}")
```

## Time Series Analysis with Exponential Weighting

In time series analysis, more recent data points are often given higher weights:

```python
import pandas as pd
import numpy as np
from weightedpandas import WeightedSeries

# Create a time series
dates = pd.date_range('2023-01-01', periods=10)
values = [10, 12, 9, 14, 15, 18, 20, 19, 22, 25]
time_series = pd.Series(values, index=dates)

# Create exponential weights (more recent = higher weight)
# Formula: weight = alpha * (1-alpha)^i where i is the distance from the end
alpha = 0.3
weights = [alpha * (1-alpha)**(len(values)-i-1) for i in range(len(values))]

# Create weighted series
weighted_ts = WeightedSeries(time_series.values, index=time_series.index, weights=weights)

# Calculate weighted statistics
print(f"Regular mean: {time_series.mean():.2f}")
print(f"Exponentially weighted mean: {weighted_ts.mean():.2f}")
print(f"Regular std: {time_series.std():.2f}")
print(f"Exponentially weighted std: {weighted_ts.std():.2f}")
```

## Handling Missing Data

WeightedPandas can handle missing data in weighted calculations:

```python
import pandas as pd
import numpy as np
from weightedpandas import WeightedSeries

# Create a series with missing values
data = [1, 2, np.nan, 4, 5]
weights = [5, 4, 3, 2, 1]

ws = WeightedSeries(data, weights=weights)

# Calculate statistics with and without NA values
print(f"Weighted mean (skip NA): {ws.mean()}")
print(f"Weighted mean (include NA): {ws.mean(skipna=False)}")

# Calculate sum with minimum count
print(f"Weighted sum (min_count=0): {ws.sum(min_count=0)}")
print(f"Weighted sum (min_count=5): {ws.sum(min_count=5)}")  # Returns NaN as there are only 4 non-NA values
```

## Advanced Example: Portfolio Analysis

This example demonstrates using WeightedPandas for financial portfolio analysis:

```python
import pandas as pd
import numpy as np
from weightedpandas import WeightedDataFrame

# Sample stock returns data
stock_returns = {
    'Stock A': [0.05, -0.02, 0.03, 0.01, 0.04],
    'Stock B': [0.02, 0.01, -0.01, 0.03, 0.02],
    'Stock C': [-0.01, 0.04, 0.05, -0.02, 0.03],
    'Stock D': [0.03, 0.02, 0.01, 0.04, -0.01]
}

# Portfolio weights (must sum to 1)
portfolio_weights = [0.3, 0.3, 0.2, 0.2]  # 30% each in A and B, 20% each in C and D

# Create returns dataframe
returns_df = pd.DataFrame(stock_returns)

# Calculate portfolio statistics
weighted_returns = WeightedDataFrame(returns_df, weights=portfolio_weights)

# Calculate weighted mean returns (expected return for each stock)
expected_returns = weighted_returns.mean(axis=0)
print("Expected returns for each stock:")
print(expected_returns)

# Calculate overall portfolio expected return
portfolio_return = (expected_returns * portfolio_weights).sum()
print(f"Overall portfolio expected return: {portfolio_return:.4f}")

# Calculate weighted covariance and correlation matrices
cov_matrix = weighted_returns.cov()
corr_matrix = weighted_returns.corr()

print("\nCovariance Matrix:")
print(cov_matrix)

print("\nCorrelation Matrix:")
print(corr_matrix)

# Calculate portfolio variance (risk)
portfolio_variance = 0
for i in range(len(portfolio_weights)):
    for j in range(len(portfolio_weights)):
        portfolio_variance += portfolio_weights[i] * portfolio_weights[j] * cov_matrix.iloc[i, j]

portfolio_risk = np.sqrt(portfolio_variance)
print(f"\nPortfolio risk (standard deviation): {portfolio_risk:.4f}")
```