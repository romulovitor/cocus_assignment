.ONESHELL:
PYTHON := ${PWD}/venv/bin/python3
PIP := ${PWD}/venv/bin/pip3

venv:
	@echo "Inicializa uma venv local."
	virtualenv venv -p python

install: venv
	@echo "Instala as dependências numa venv local."
	${PIP} install -r requirements.txt
