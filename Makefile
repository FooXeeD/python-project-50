install:
	poetry install

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml tests/

build:
	poetry build

check: selfcheck test lint

selfcheck:
	poetry check

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

lint:
	poetry run flake8 gendiff

gendiff:
	poetry run gendiff

rp:
	pip install --user --force-reinstall dist/*.whl