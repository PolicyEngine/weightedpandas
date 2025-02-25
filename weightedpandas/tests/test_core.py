import unittest

import numpy as np
import pandas as pd

from weightedpandas import WeightedDataFrame, WeightedSeries


class TestWeightedSeries(unittest.TestCase):
    def setUp(self):
        self.data = [1, 2, 3, 4, 5]
        self.weights = [5, 4, 3, 2, 1]
        self.ws = WeightedSeries(self.data, weights=self.weights)

    def test_init(self):
        # Test initialization with weights
        ws = WeightedSeries(self.data, weights=self.weights)
        np.testing.assert_array_equal(ws.weights, self.weights)

        # Test initialization without weights
        ws = WeightedSeries(self.data)
        np.testing.assert_array_equal(ws.weights, np.ones(len(self.data)))

    def test_set_weights(self):
        new_weights = [10, 20, 30, 40, 50]
        ws2 = self.ws.set_weights(new_weights)
        np.testing.assert_array_equal(ws2.weights, new_weights)

        # Original weights should remain unchanged
        np.testing.assert_array_equal(self.ws.weights, self.weights)

    def test_sum(self):
        expected = sum(d * w for d, w in zip(self.data, self.weights))
        self.assertAlmostEqual(self.ws.sum(), expected)

    def test_mean(self):
        expected = sum(d * w for d, w in zip(self.data, self.weights)) / sum(
            self.weights
        )
        self.assertAlmostEqual(self.ws.mean(), expected)

    def test_var(self):
        wmean = self.ws.mean()
        expected = sum(
            ((d - wmean) ** 2) * w for d, w in zip(self.data, self.weights)
        ) / (sum(self.weights) - 1)
        self.assertAlmostEqual(self.ws.var(), expected)

    def test_std(self):
        self.assertAlmostEqual(self.ws.std(), np.sqrt(self.ws.var()))

    def test_median(self):
        # For this specific example, the weighted median should be 2
        self.assertEqual(self.ws.median(), 2)

    def test_quantile(self):
        # Test various quantiles
        self.assertEqual(self.ws.quantile(0), 1)
        self.assertEqual(self.ws.quantile(1), 5)

        # Specific to this example
        self.assertEqual(self.ws.quantile(0.5), 2)

    def test_operations(self):
        # Test that operations return WeightedSeries
        self.assertIsInstance(self.ws + 1, WeightedSeries)
        self.assertIsInstance(self.ws * 2, WeightedSeries)
        self.assertIsInstance(self.ws / 2, WeightedSeries)

        # Test that operations preserve weights
        ws2 = self.ws + 1
        np.testing.assert_array_equal(ws2.weights, self.weights)


class TestWeightedDataFrame(unittest.TestCase):
    def setUp(self):
        self.data = {"A": [1, 2, 3, 4, 5], "B": [5, 4, 3, 2, 1]}
        self.weights = [5, 4, 3, 2, 1]
        self.wdf = WeightedDataFrame(self.data, weights=self.weights)

    def test_init(self):
        # Test initialization with weights
        wdf = WeightedDataFrame(self.data, weights=self.weights)
        np.testing.assert_array_equal(wdf.weights, self.weights)

        # Test initialization without weights
        wdf = WeightedDataFrame(self.data)
        np.testing.assert_array_equal(wdf.weights, np.ones(len(self.data["A"])))

    def test_set_weights(self):
        new_weights = [10, 20, 30, 40, 50]
        wdf2 = self.wdf.set_weights(new_weights)
        np.testing.assert_array_equal(wdf2.weights, new_weights)

        # Original weights should remain unchanged
        np.testing.assert_array_equal(self.wdf.weights, self.weights)

    def test_sum(self):
        expected_a = sum(d * w for d, w in zip(self.data["A"], self.weights))
        expected_b = sum(d * w for d, w in zip(self.data["B"], self.weights))

        results = self.wdf.sum()
        self.assertAlmostEqual(results["A"], expected_a)
        self.assertAlmostEqual(results["B"], expected_b)

    def test_mean(self):
        expected_a = sum(d * w for d, w in zip(self.data["A"], self.weights)) / sum(
            self.weights
        )
        expected_b = sum(d * w for d, w in zip(self.data["B"], self.weights)) / sum(
            self.weights
        )

        results = self.wdf.mean()
        self.assertAlmostEqual(results["A"], expected_a)
        self.assertAlmostEqual(results["B"], expected_b)

    def test_var(self):
        results = self.wdf.var()

        # Calculate expected manually for verification
        wm_a = self.wdf["A"].mean()
        expected_a = sum(
            ((d - wm_a) ** 2) * w for d, w in zip(self.data["A"], self.weights)
        ) / (sum(self.weights) - 1)

        wm_b = self.wdf["B"].mean()
        expected_b = sum(
            ((d - wm_b) ** 2) * w for d, w in zip(self.data["B"], self.weights)
        ) / (sum(self.weights) - 1)

        self.assertAlmostEqual(results["A"], expected_a)
        self.assertAlmostEqual(results["B"], expected_b)

    def test_std(self):
        results = self.wdf.std()
        var_results = self.wdf.var()

        self.assertAlmostEqual(results["A"], np.sqrt(var_results["A"]))
        self.assertAlmostEqual(results["B"], np.sqrt(var_results["B"]))

    def test_getitem(self):
        # Test column access
        col_a = self.wdf["A"]
        self.assertIsInstance(col_a, WeightedSeries)
        np.testing.assert_array_equal(col_a.weights, self.weights)

        # Test multiple column access
        subset = self.wdf[["A", "B"]]
        self.assertIsInstance(subset, WeightedDataFrame)
        np.testing.assert_array_equal(subset.weights, self.weights)

    def test_corr(self):
        # Test correlation
        corr = self.wdf.corr()
        self.assertEqual(corr.shape, (2, 2))
        self.assertAlmostEqual(corr.loc["A", "A"], 1.0)
        self.assertAlmostEqual(corr.loc["B", "B"], 1.0)

        # In this specific example, A increases as B decreases, so correlation should be negative
        self.assertLess(corr.loc["A", "B"], 0)


if __name__ == "__main__":
    unittest.main()
