all: setup

venv:
	virtualenv venv

setup: venv
	venv/bin/python setup.py develop

clean:
	rm -rf venv
	find . -name \*.pyc -exec rm '{}' ';'
	rm -rf *.egg-info
