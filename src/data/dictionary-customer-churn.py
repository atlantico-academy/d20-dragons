import pandas as pd
import os

dictionary = pd.DataFrame([
    {
        "variavel": "Surname",
        "descricao": "O sobrenome do cliente",
        "tipo":"qualitativa",
        "subtipo":"nominal"
    },{
        "variavel": "CreditScore",
        "descricao": "O score de crédito do cliente",
        "tipo":"quantitativa",
        "subtipo":"discreta"
    },{
        "variavel": "Geography",
        "descricao": "A localização geográfica do cliente (por exemplo, país ou região)",
        "tipo":"qualitativa",
        "subtipo":"nominal"
    },{
        "variavel": "Gender",
        "descricao": "O gênero do cliente",
        "tipo":"qualitativa",
        "subtipo":"nominal"
    },{
        "variavel": "Age",
        "descricao": "A idade do cliente",
        "tipo":"quantitativa",
        "subtipo":"discreta"
    },{
        "variavel": "Tenure",
        "descricao": "O número de anos que o cliente está no banco",
        "tipo":"quantitativa",
        "subtipo":"discreta"
    },{
        "variavel": "Balance",
        "descricao": "O saldo da conta do cliente",
        "tipo":"quantitativa",
        "subtipo":"continua"
    },{
        "variavel": "NumOfProducts",
        "descricao": "O número de produtos bancários que o cliente possui",
        "tipo":"quantitativa",
        "subtipo":"discreta"
    },{
        "variavel": "HasCrCard",
        "descricao": "Indica se o cliente possui cartão de crédito (binário: sim/não)",
        "tipo":"qualitativa",
        "subtipo":"nominal"
    },{
        "variavel": "IsActiveMember",
        "descricao": "Indica se o cliente é um membro ativo (binário: sim/não)",
        "tipo":"qualitativa",
        "subtipo":"nominal"
    },{
        "variavel": "EstimatedSalary",
        "descricao": "O salário estimado do cliente",
        "tipo":"quantitativa",
        "subtipo":"continua"
    },{
        "variavel": "Exited",
        "descricao": "Indica se o cliente saiu do banco (binário: sim/não)",
        "tipo":"qualitativa",
        "subtipo":"nominal"
    }
])

file_path = '../../data/external/dictionary.csv'

dictionary.to_csv(file_path, index=False)

if os.path.exists(file_path):
    print("O arquivo está no local especificado.")
else:
    print("O arquivo não está no local especificado.")