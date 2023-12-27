import json
import yaml


def parse(data, extension: str) -> str:
    if extension == 'json':
        return json.loads(data)
    if extension == 'yaml':
        return yaml.safe_load(data)
    raise ValueError(
        """f'The file extension (.{extension}) is not supported.\n
        Make sure that the selected files have
        the extension: json, yaml or yml.'"""
    )
