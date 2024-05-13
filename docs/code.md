# Início

## Funcionalidades

Essa template foi inicialmente baseado no [template de ciência de dados do cookiecutter](https://drivendata.github.io/cookiecutter-data-science/), a template tem as seguintes características:

- Utilização do arquivo `pyproject.toml` como centralizador de dependências;
- Configuração para criação de aplicação `streamlit`;
- Utilização de [jupyter notebooks](https://jupyter.org/) para arquivos de análise;
- Documentação com o [mkdocs](https://www.mkdocs.org/) ([material design](https://squidfunk.github.io/mkdocs-material/) theme)

## Instruções

### Requisitos

- git
- Python 3.10.*
- Poetry `1.1.13` ou superior

É aconselhável o uso do `pyenv` para o gerenciamento de versões do Python.

### Execução

Navegar até a pasta local, usando o comando :

```
cd equipe1-2024.1
```

Instalar as dependências do projeto utilizando o comando:

```
poetry install
```

Ativar o ambiente virtual criado pelo Poetry utilizando o comando:

```
poetry shell
```