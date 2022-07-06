lint:
	poetry run flake8 ships_list

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

package-reinstall:
	python3 -m pip install --user dist/*.whl	

push:
	make lint
	git add .
	git commit -m '$M'
	git push