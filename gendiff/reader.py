"""Get format of file."""
from os.path import splitext


def get_format(filepath: str) -> str:
    _, extension = splitext(filepath)
    if extension in ('.yaml', '.yml'):
        return 'yaml'
    elif extension == '.json':
        return 'json'
    raise TypeError(
        'Проверьте расширение файлов.\nТолько расширения файлов '
        'yaml,yml или json поддерживаются.'
    )


def read_data(filepath: str):
    with open(filepath) as read_file:
        return read_file.read()
