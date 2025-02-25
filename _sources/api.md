## API Reference

This page documents the complete API for WeightedPandas.

### WeightedSeries

```{eval-rst}
.. py:class:: weightedpandas.WeightedSeries(data=None, index=None, dtype=None, name=None, copy=False, fastpath=False, weights=None)

   A Series-like object that supports weighted operations.

   :param data: Data to initialize series with
   :type data: array-like, Iterable, dict, or scalar value
   :param index: Index to use for resulting series
   :type index: array-like or Index (1d)
   :param dtype: Data type for the output series
   :type dtype: str, numpy.dtype, or ExtensionDtype, optional
   :param name: Name to use for the series
   :type name: str, optional
   :param copy: Copy input data
   :type copy: bool, default False
   :param fastpath: Internal parameter
   :type fastpath: bool, default False
   :param weights: Weights to use for weighted operations
   :type weights: array-like, optional
```

#### Properties

```{eval-rst}
.. py:attribute:: weightedpandas.WeightedSeries.weights

   The weights array used for weighted operations.
```

#### Statistical Methods

```{eval-rst}
.. py:method:: weightedpandas.WeightedSeries.sum(axis=None, skipna=True, level=None, numeric_only=None, min_count=0, **kwargs)

   Return the weighted sum of the values.
   
   :param axis: Not used, included for compatibility with pandas API
   :param skipna: Exclude NA/null values when computing the result
   :type skipna: bool, default True
   :param level: If the axis is a MultiIndex, count along a particular level
   :param numeric_only: Include only float, int, boolean columns
   :type numeric_only: bool, default None
   :param min_count: The required number of valid values to perform the operation
   :type min_count: int, default 0
   :return: Weighted sum
   :rtype: scalar or Series

.. py:method:: weightedpandas.WeightedSeries.mean(axis=None, skipna=True, level=None, numeric_only=None, **kwargs)

   Return the weighted mean of the values.
   
   :param axis: Not used, included for compatibility with pandas API
   :param skipna: Exclude NA/null values when computing the result
   :type skipna: bool, default True
   :param level: If the axis is a MultiIndex, count along a particular level
   :param numeric_only: Include only float, int, boolean columns
   :type numeric_only: bool, default None
   :return: Weighted mean
   :rtype: scalar

.. py:method:: weightedpandas.WeightedSeries.var(axis=None, skipna=True, level=None, ddof=1, numeric_only=None, **kwargs)

   Return the weighted variance of the values.
   
   :param axis: Not used, included for compatibility with pandas API
   :param skipna: Exclude NA/null values when computing the result
   :type skipna: bool, default True
   :param level: If the axis is a MultiIndex, count along a particular level
   :param ddof: Delta Degrees of Freedom
   :type ddof: int, default 1
   :param numeric_only: Include only float, int, boolean columns
   :type numeric_only: bool, default None
   :return: Weighted variance
   :rtype: scalar

.. py:method:: weightedpandas.WeightedSeries.std(axis=None, skipna=True, level=None, ddof=1, numeric_only=None, **kwargs)

   Return the weighted standard deviation of the values.
   
   :param axis: Not used, included for compatibility with pandas API
   :param skipna: Exclude NA/null values when computing the result
   :type skipna: bool, default True
   :param level: If the axis is a MultiIndex, count along a particular level
   :param ddof: Delta Degrees of Freedom
   :type ddof: int, default 1
   :param numeric_only: Include only float, int, boolean columns
   :type numeric_only: bool, default None
   :return: Weighted standard deviation
   :rtype: scalar

.. py:method:: weightedpandas.WeightedSeries.median(axis=None, skipna=True, level=None, numeric_only=None, **kwargs)

   Return the weighted median of the values.
   
   :param axis: Not used, included for compatibility with pandas API
   :param skipna: Exclude NA/null values when computing the result
   :type skipna: bool, default True
   :param level: If the axis is a MultiIndex, count along a particular level
   :param numeric_only: Include only float, int, boolean columns
   :type numeric_only: bool, default None
   :return: Weighted median
   :rtype: scalar

.. py:method:: weightedpandas.WeightedSeries.quantile(q=0.5, axis=0, numeric_only=True, interpolation='linear', **kwargs)

   Return weighted quantiles of the Series.
   
   :param q: Quantile to compute, can be a scalar or array-like
   :type q: float or array-like, default 0.5
   :param axis: Not used, included for compatibility with pandas API
   :param numeric_only: Include only float, int, boolean columns
   :type numeric_only: bool, default True
   :param interpolation: Interpolation method to use when quantile lies between data points
   :type interpolation: str, default 'linear'
   :return: Weighted quantile(s)
   :rtype: scalar or Series
```

### WeightedDataFrame

```{eval-rst}
.. py:class:: weightedpandas.WeightedDataFrame(data=None, index=None, columns=None, dtype=None, copy=False, weights=None)

   A DataFrame-like object that supports weighted operations.

   :param data: Data to initialize DataFrame with
   :type data: ndarray, Iterable, dict, or DataFrame
   :param index: Index to use for resulting DataFrame
   :type index: Index or array-like
   :param columns: Column labels to use
   :type columns: Index or array-like
   :param dtype: Data type for the output
   :type dtype: dtype, default None
   :param copy: Copy data from inputs
   :type copy: bool, default False
   :param weights: Weights to use for weighted operations
   :type weights: array-like, optional
```

#### Properties

```{eval-rst}
.. py:attribute:: weightedpandas.WeightedDataFrame.weights

   The weights array used for weighted operations.
```

#### Statistical Methods

```{eval-rst}
.. py:method:: weightedpandas.WeightedDataFrame.sum(axis=0, skipna=True, level=None, numeric_only=None, min_count=0, **kwargs)

   Return the weighted sum of the values for the requested axis.
   
   :param axis: Axis to calculate along (0 for columns, 1 for rows)
   :type axis: {0 or 'index', 1 or 'columns'}, default 0
   :param skipna: Exclude NA/null values when computing the result
   :type skipna: bool, default True
   :param level: If the axis is a MultiIndex, count along a particular level
   :param numeric_only: Include only float, int, boolean columns
   :type numeric_only: bool, default None
   :param min_count: The required number of valid values to perform the operation
   :type min_count: int, default 0
   :return: Weighted sum along specified axis
   :rtype: Series or DataFrame

.. py:method:: weightedpandas.WeightedDataFrame.mean(axis=0, skipna=True, level=None, numeric_only=None, **kwargs)

   Return the weighted mean of the values for the requested axis.
   
   :param axis: Axis to calculate along (0 for columns, 1 for rows)
   :type axis: {0 or 'index', 1 or 'columns'}, default 0
   :param skipna: Exclude NA/null values when computing the result
   :type skipna: bool, default True
   :param level: If the axis is a MultiIndex, count along a particular level
   :param numeric_only: Include only float, int, boolean columns
   :type numeric_only: bool, default None
   :return: Weighted mean along specified axis
   :rtype: Series or DataFrame

.. py:method:: weightedpandas.WeightedDataFrame.var(axis=0, skipna=True, level=None, ddof=1, numeric_only=None, **kwargs)

   Return the weighted variance of the values for the requested axis.
   
   :param axis: Axis to calculate along (0 for columns, 1 for rows)
   :type axis: {0 or 'index', 1 or 'columns'}, default 0
   :param skipna: Exclude NA/null values when computing the result
   :type skipna: bool, default True
   :param level: If the axis is a MultiIndex, count along a particular level
   :param ddof: Delta Degrees of Freedom
   :type ddof: int, default 1
   :param numeric_only: Include only float, int, boolean columns
   :type numeric_only: bool, default None
   :return: Weighted variance along specified axis
   :rtype: Series or DataFrame

.. py:method:: weightedpandas.WeightedDataFrame.std(axis=0, skipna=True, level=None, ddof=1, numeric_only=None, **kwargs)

   Return the weighted standard deviation of the values for the requested axis.
   
   :param axis: Axis to calculate along (0 for columns, 1 for rows)
   :type axis: {0 or 'index', 1 or 'columns'}, default 0
   :param skipna: Exclude NA/null values when computing the result
   :type skipna: bool, default True
   :param level: If the axis is a MultiIndex, count along a particular level
   :param ddof: Delta Degrees of Freedom
   :type ddof: int, default 1
   :param numeric_only: Include only float, int, boolean columns
   :type numeric_only: bool, default None
   :return: Weighted standard deviation along specified axis
   :rtype: Series or DataFrame

.. py:method:: weightedpandas.WeightedDataFrame.corr(method='pearson', min_periods=1)

   Calculate the weighted correlation between columns.
   
   :param method: Method to use for correlation calculation
   :type method: {'pearson', 'kendall', 'spearman'}, default 'pearson'
   :param min_periods: Minimum number of observations required per pair of columns
   :type min_periods: int, default 1
   :return: Weighted correlation matrix
   :rtype: DataFrame

.. py:method:: weightedpandas.WeightedDataFrame.cov(min_periods=None, ddof=1)

   Calculate the weighted covariance between columns.
   
   :param min_periods: Minimum number of observations required per pair of columns
   :type min_periods: int, optional
   :param ddof: Delta Degrees of Freedom
   :type ddof: int, default 1
   :return: Weighted covariance matrix
   :rtype: DataFrame
```

### Helper Functions

```{eval-rst}
.. py:function:: weightedpandas.weighted_series(data=None, index=None, dtype=None, name=None, copy=False, weights=None)

   Helper function to create a WeightedSeries.
   
   :param data: Data to initialize series with
   :type data: array-like, Iterable, dict, or scalar value
   :param index: Index to use for resulting series
   :type index: array-like or Index (1d)
   :param dtype: Data type for the output series
   :type dtype: str, numpy.dtype, or ExtensionDtype, optional
   :param name: Name to use for the series
   :type name: str, optional
   :param copy: Copy input data
   :type copy: bool, default False
   :param weights: Weights to use for weighted operations
   :type weights: array-like, optional
   :return: A new WeightedSeries
   :rtype: weightedpandas.WeightedSeries

.. py:function:: weightedpandas.weighted_dataframe(data=None, index=None, columns=None, dtype=None, copy=False, weights=None)

   Helper function to create a WeightedDataFrame.
   
   :param data: Data to initialize DataFrame with
   :type data: ndarray, Iterable, dict, or DataFrame
   :param index: Index to use for resulting DataFrame
   :type index: Index or array-like
   :param columns: Column labels to use
   :type columns: Index or array-like
   :param dtype: Data type for the output
   :type dtype: dtype, default None
   :param copy: Copy data from inputs
   :type copy: bool, default False
   :param weights: Weights to use for weighted operations
   :type weights: array-like, optional
   :return: A new WeightedDataFrame
   :rtype: weightedpandas.WeightedDataFrame
```