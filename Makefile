# Nome do ambiente virtual
VENV = venv

# Nome do pacote de requisitos
REQUIREMENTS = requirements.txt

# Definir os comandos a serem usados
PYTHON = $(VENV)/bin/python
PIP = $(VENV)/bin/pip
PYTEST = $(VENV)/bin/pytest

# Define o comando init que cria o ambiente virtual e instala as dependências
init:
	@echo "Criando ambiente virtual..."
	python3 -m venv $(VENV)
	@echo "Instalando dependências..."
	$(PIP) install -r $(REQUIREMENTS)
	@echo "Ambiente inicializado."

# Define o comando test que roda os testes com pytest na pasta 'test'
test:
	@echo "Rodando testes..."
	$(PYTEST) tests

# Limpeza dos arquivos compilados e ambiente virtual
clean:
	@echo "Limpando arquivos compilados..."
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -exec rm -r {} +
	@echo "Limpando arquivos temporarios de teste"
	rm -rf misc/
	@echo "Removendo ambiente virtual..."
	rm -rf $(VENV)
	@echo "Limpeza completa."

.PHONY: init test clean
