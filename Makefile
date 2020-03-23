ci-build: test-with-coverage type-check style-check coverage-report

test:
	python -m unittest discover src/tests

test-with-coverage:
	coverage run --rcfile=src/setup.cfg -m unittest discover src/tests

type-check:
	mypy --config-file src/setup.cfg src/

style-check:
	flake8 --config=src/setup.cfg src/

coverage-report:
	coverage report --rcfile=src/setup.cfg
