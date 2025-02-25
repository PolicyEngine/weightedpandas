## WeightedPandas

WeightedPandas extends pandas Series and DataFrame classes to support weighted operations. It provides drop-in replacements for pandas objects that automatically handle weights in statistical operations.

```{figure} ./logo.png
:alt: WeightedPandas Logo
:width: 300px
:align: center
```

### Features

- Weighted versions of common statistical operations:
  - `sum()`, `mean()`, `var()`, `std()`
  - `median()`, `quantile()`
  - `corr()`, `cov()`
- Preserves weights through arithmetic operations
- Familiar pandas interface
- Supports both Series and DataFrame objects

### Quick Example

```python
import pandas as pd
import numpy as np
from weightedpandas import WeightedSeries, WeightedDataFrame

# Create a weighted series
data = [1, 2, 3, 4, 5]
weights = [5, 4, 3, 2, 1]
ws = WeightedSeries(data, weights=weights)

# Calculate weighted statistics
print(f"Weighted mean: {ws.mean()}")
print(f"Weighted standard deviation: {ws.std()}")

# Weights are preserved through operations
ws2 = ws * 2 + 1
print(ws2.weights)  # Same as original weights
```

```{toctree}
:hidden:
:maxdepth: 2
installation
usage
api
examples
```