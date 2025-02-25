# Installation

## Requirements

WeightedPandas requires:

- Python 3.8+
- pandas 1.4.0+
- numpy 1.20.0+

## Installing with pip

The simplest way to install WeightedPandas is using pip:

```bash
pip install weightedpandas
```

## Installing from source

To install WeightedPandas from source:

```bash
git clone https://github.com/policyengine/weightedpandas.git
cd weightedpandas
pip install -e .
```

## Verifying installation

To verify that WeightedPandas is installed correctly, run:

```python
import weightedpandas

print(weightedpandas.__version__)
```