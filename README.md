<div align="center">
  
  `D20 Dragons`
  
  <img src="https://github.com/atlantico-academy/equipe1-2024.1/assets/94808306/a4a86016-0f78-451a-869f-d8e267fe9e3d" width="300">
</div>
<hr>

# Análise de Churn de Clientes Bancários

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)![Plotly](https://img.shields.io/badge/Plotly-%233F4F75.svg?style=for-the-badge&logo=plotly&logoColor=white)![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)

![GitHub](https://img.shields.io/github/license/atlantico-academy/equipe1-2024.1.svg) [![PyPI](https://img.shields.io/pypi/v/atlantico-academy-equipe1-2024.1.svg)](http://pypi.org/project/atlantico-academy-equipe1-2024.1/) [![GitHub last commit](https://img.shields.io/github/last-commit/atlantico-academy/equipe1-2024.1.svg)](https://github.com/atlantico-academy/equipe1-2024.1/commit/developer)

## Contexto

Este projeto foca na análise de [churn de clientes de um banco, usando um dataset disponível no Kaggle](https://www.kaggle.com/datasets/saurabhbadole/bank-customer-churn-prediction-dataset). O objetivo é identificar padrões e fatores que influenciam os clientes a deixar o banco, utilizando técnicas de ciência de dados para processar e analisar os dados. A análise ajudará a entender melhor as necessidades dos clientes e a melhorar as estratégias de retenção.

## Justificativa

A justificativa para este projeto se baseia na importância de manter uma base de clientes sólida para a sustentabilidade financeira do banco. Reduzir o churn pode significar maior lucratividade e satisfação do cliente, crucial em um mercado competitivo.

## Graphical Abstract

[Graphical Abstract](https://whimsical.com/fluxograma-ciclico-crisp-dm-para-previsao-de-churn-de-clientes-VEJSdhqT3cxN7DKenK6toG)

## Desenvolvedores

[<img src="https://github.com/atlantico-academy/equipe1-2024.1/assets/94808306/e1af5396-1b27-46f2-9e67-bcc13049ce73"  width="150" height="150">](https://github.com/claralimasilva) | [<img src="https://github.com/atlantico-academy/equipe1-2024.1/assets/94808306/aa965a52-2d5f-4836-9ac9-ab117f913b31"  width="150" height="150">](https://github.com/matheusvazdata) |  [<img src="https://github.com/atlantico-academy/equipe1-2024.1/assets/94808306/1187a373-0dba-4430-b35b-00e2901b3bf6"  width="150" height="150">](https://github.com/matt-balda) | [<img src="https://github.com/atlantico-academy/equipe1-2024.1/assets/94808306/6023d7fa-71fa-4bf1-ab29-9b439d63e7e0"  width="150" height="150">](https://github.com/uSilas) 
--- | --- | --- | --- 
[Clara Lima Silva](https://github.com/claralimasilva) | [Francisco Matheus Vaz dos Santos](https://github.com/matheusvazdata) |  [Mateus Balda Mota](https://github.com/matt-balda) | [Silas Eufrásio da Silva](https://github.com/uSilas) 

### > [Execução](./docs/code.md)

### Organização de diretórios

```
├── data/              # Diretório contendo todos os arquivos de dados
│   ├── external/      # Arquivos de dados de fontes externas
│   ├── interim/       # Arquivos de dados intermediários
│   ├── processed/     # Arquivos de dados processados
│   └── raw/           # Arquivos de dados originais, imutáveis
├── docs/              # Documentação gerada através da biblioteca mkdocs
├── models/            # Modelos treinados e serializados, predições ou resumos de modelos
├── notebooks/         # Diretório contendo todos os notebooks utilizados nos passos
├── references/        # Dicionários de dados, manuais e todo o material exploratório
├── src/               # Código fonte utilizado nesse projeto
│   ├── data/          # Classes e funções utilizadas para download e processamento de dados
│   ├── deployment/    # Classes e funções utilizadas para implantação do modelo
│   └── model/         # Classes e funções utilizadas para modelagem
├── app.py             # Arquivo com o código da aplicação do streamlit
├── Procfile           # Arquivo de configuração do heroku
├── pyproject.toml     # Arquivo de dependências para reprodução do projeto
├── poetry.lock        # Arquivo com sub-dependências do projeto principal
├── README.md          # Informações gerais do projeto
└── tasks.py           # Arquivo com funções para criação de tarefas utilizadas pelo invoke
```
