# fluxopt-yaml

Declarative YAML + CSV model definition for
[fluxopt](https://fbumann.github.io/fluxopt/) energy system models.

!!! warning "Early development"
    This package is experimental — the API may change between releases.

## Installation

```bash
pip install fluxopt-yaml
```

## Quick start

```python
from fluxopt_yaml import load_yaml

data = load_yaml('model.yaml')
```

Example YAML file:

```yaml
effects:
  - name: cost
    is_objective: true

ports:
  - name: grid
    imports:
      - carrier: electricity
        size: 200
        effects_per_flow_hour:
          cost: 0.04
```

## Links

- [fluxopt documentation](https://fbumann.github.io/fluxopt/)
- [Source code](https://github.com/FBumann/fluxopt-yaml)
