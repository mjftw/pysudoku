# PySudoku

Simple sudoku solver using backtrack method.
It's pretty slow, but it works.

## Install

```shell
# Setup virtual env (optional)
python3 -m pip install virtualenv
python3 -m virtualenv venv
. venv/bin/activate

# Install
python3 -m pip install .
```

## Run as a service

You can run the tool in SaaS mode (Sudoku as a Service `;-)`) using [FastAPI](https://fastapi.tiangolo.com)

```shell
make server
```

You can view the API docs (and try out the endpoints) at http://127.0.0.1:8000/docs

## Run the tests

```shell
make test
```
