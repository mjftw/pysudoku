VENV := ./venv/bin/activate
APP ?= pysudoku.web.app:app

${VENV}:
	python3 -m pip install virtualenv
	python3 -m virtualenv venv

install: ${VENV}
	. venv/bin/activate
	python3 -m pip install .

test: install
	pytest

server: install
	uvicorn ${APP} --reload

.PHONY: test install