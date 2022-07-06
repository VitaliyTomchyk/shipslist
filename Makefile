lint:
	poetry run flake8 ships_list

push:
	make lint
	git add .
	git commit -m '$M'
	git push