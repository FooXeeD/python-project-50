import json

import yaml


def parse(data, format_: str) -> str:
    if format_ == 'json':
        return json.loads(data)
    if format_ == 'yaml':
        return yaml.safe_load(data)
    raise ValueError(
        'Расширение файла (.{format_}) не поддерживается.\n'
        'Выбранные файлы должны иметь '
        'расширение: json, yaml or yml.'.format(format_=format_)
    )
