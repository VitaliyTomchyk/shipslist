lint:
	poetry run flake8 ships_list

build:
	poetry build
	

publish:
	poetry publish --dry-run -u ' ' -p ' '

package-install:
	python3 -m pip install --user dist/*.whl

package-reinstall:
	python3 -m pip install --force-reinstall --user dist/*.whl 

update:
	make build
	make publish
	make package-reinstall	

push:
	make lint
	git add .
	git commit -m '$M'
	git push