lint:
	poetry run flake8 ships_list

build:
	poetry build

publish:
	poetry publish --dry-run -u ' ' -p ' '

install:
	python3 -m pip install --user dist/*.whl

package-install:
	python3 -m pip install --force-reinstall --user dist/*.whl

update:
	make build
	make publish
	make install
	make package-install

pytest:
	poetry run pytest

run:
	poetry run ships_list -h

com:
	make lint
	make pytest
	git add .
	git commit -m '$m'

push:
	make pytest
	git add .
	git commit -m '$m'
	git push