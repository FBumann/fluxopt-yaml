from pathlib import Path

from fluxopt_yaml import load_yaml


def test_load_yaml(tmp_path: Path) -> None:
    yaml_file = tmp_path / 'model.yaml'
    yaml_file.write_text('name: test\nvalue: 42\n')
    result = load_yaml(yaml_file)
    assert result == {'name': 'test', 'value': 42}
