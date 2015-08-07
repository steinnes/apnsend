all: setup

venv:
	virtualenv venv

setup: venv
	venv/bin/python setup.py develop
