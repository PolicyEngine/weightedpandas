# Makefile for WeightedPandas

.PHONY: install install-dev test lint format format-check clean docs docs-serve build publish

# Default Python command
PYTHON := python3

# Installation
install:
	$(PYTHON) -m pip install .

install-dev:
	$(PYTHON) -m pip install -e ".[dev]"

# Testing
test:
	$(PYTHON) -m pytest weightedpandas/tests/ -v

# Code quality
lint:
	$(PYTHON) -m flake8 weightedpandas/
	$(PYTHON) -m mypy weightedpandas/

format:
	$(PYTHON) -m black weightedpandas/
	$(PYTHON) -m isort weightedpandas/

format-check:
	$(PYTHON) -m black --check weightedpandas/
	$(PYTHON) -m isort --check weightedpandas/

# Documentation
docs:
	cd docs && $(PYTHON) -m pip install -r requirements.txt
	rm -rf docs/_build/
	cd docs && $(PYTHON) -m jupyter book build .

docs-serve:
	cd docs/_build/html && $(PYTHON) -m http.server 8000

# Build and publish
build:
	$(PYTHON) -m pip install build
	$(PYTHON) -m build

publish:
	$(PYTHON) -m pip install twine
	$(PYTHON) -m twine upload dist/*

# Clean up
clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	rm -rf **/__pycache__/
	rm -rf **/.ipynb_checkpoints/
	rm -rf docs/_build/
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type f -name "*.pyd" -delete
	find . -type f -name ".DS_Store" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	find . -type d -name "*.egg" -exec rm -rf {} +

# Help
help:
	@echo "Available targets:"
	@echo "  install      - Install the package"
	@echo "  install-dev  - Install the package in development mode with dev dependencies"
	@echo "  test         - Run tests"
	@echo "  lint         - Run linting checks"
	@echo "  format       - Format code with black and isort"
	@echo "  format-check - Check code format without modifying files"
	@echo "  docs         - Build documentation"
	@echo "  docs-serve   - Serve documentation locally"
	@echo "  build        - Build distribution packages"
	@echo "  publish      - Publish package to PyPI"
	@echo "  clean        - Remove build artifacts"