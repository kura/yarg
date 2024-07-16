.PHONY: clean coverage deps deps-docs deps-test docs flake8 install pypi rtd test tox uninstall

clean:
	find . -name "*.pyc" -delete

coverage: deps-test
	coverage run -m pytest

deps:
	pip install -r requirements.txt

deps-docs:
	pip install -r requirements-docs.txt

deps-test:
	pip install -r requirements-test.txt

docs: deps-docs
	sphinx-build -b html docs/source docs/build

flake8:
	pip install flake8
	flake8 yarg  --show-source

install:
	python setup.py install

pypi: rtd
	pip install -r requirements-pypi.txt
	python setup.py register
	python setup.py sdist bdist_wheel
	twine upload dist/*

rtd:
	curl -X POST https://readthedocs.org/build/yarg

test: deps deps-test
	pytest

tox: deps deps-test
	detox

uninstall:
	pip uninstall yarg
