"""YAML loading and model construction for fluxopt."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml


def load_yaml(path: str | Path) -> dict[str, Any]:
    """Load a fluxopt model definition from a YAML file.

    Args:
        path: Path to the YAML file.

    Returns:
        Parsed YAML content as a dictionary.
    """
    path = Path(path)
    with path.open() as f:
        data: dict[str, Any] = yaml.safe_load(f)
    return data
