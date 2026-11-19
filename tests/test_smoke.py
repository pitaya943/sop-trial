"""Smoke test: the package imports and has a version (bootstrap check B5)."""

import trial


def test_package_imports_with_a_version():
    assert trial.__version__ == "0.1.0"
