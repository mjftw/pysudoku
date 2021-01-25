VENV := ./venv/bin/activate


${VENV}:
	python3 -m pip install virtualenv
	python3 -m virtualenv venv

test: ${VENV}
	. venv/bin/activate
	python3 -m pip install .
	pytest

.PHONY: test