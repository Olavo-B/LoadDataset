import setuptools
import os

# Ler o conteúdo do README.md para a descrição longa
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Construir o caminho para o arquivo requirements.txt
lib_folder = os.path.dirname(os.path.realpath(__file__))
requirement_path = os.path.join(lib_folder, 'requirements.txt')

# Ler as dependências do requirements.txt, se existir
install_requires = []
if os.path.isfile(requirement_path):
    with open(requirement_path) as f:
        install_requires = f.read().splitlines()

# Configurar a instalação do pacote
setuptools.setup(
    name="LoadDataset",
    version="0.1.3",
    author="Olavo Barros",
    author_email="olavo.barros.silva@gmail.com",
    description="Biblioteca para importar datasets convencionais automaticamente",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Olavo-B/LoadDataset.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=install_requires,
)
