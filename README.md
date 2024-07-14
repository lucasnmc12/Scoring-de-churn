# Scoring de Churn para SaaS

Este projeto visa prever a probabilidade de churn (cancelamento) de clientes de uma empresa de SaaS utilizando um modelo de aprendizado de máquina treinado.


## Pré-requisitos

- Python 3.8 ou superior
- Virtualenv

## Bibliotecas Necessárias

- pandas
- numpy
- scikit-learn
- joblib
- faker

## Instalação

1. Clone o repositório:

    ```sh
    git clone https://github.com/seu-usuario/scoring-de-churn.git
    cd scoring-de-churn
    ```

2. Crie e ative um ambiente virtual:

    ```sh
    python -m venv env
    source env/bin/activate  # Linux/Mac
    .\env\Scripts\activate  # Windows
    ```

3. Instale as dependências:

    ```sh
    pip install -r requirements.txt
    ```

## Uso

### 1. Gerar Dados Fictícios

Para gerar dados fictícios de clientes e uso, execute o script `generate_data.py`:


### 2. Pré-processar os Dados

Execute o script `preprocessos.py` para limpar e combinar os dados:


### 3. Treinar o Modelo

Para treinar o modelo de churn, execute o script `train_model.py`. Este script irá treinar o modelo e salvar o modelo treinado em `models/modelo_churn.pkl`.

### 4. Prever Churn para Novos Clientes

Para prever o churn de novos clientes, coloque os dados dos novos clientes em um arquivo CSV chamado `data/dados_novos_clientes.csv` (sem a coluna `churn`). Em seguida, execute o script `predict_churn.py`:



## Estrutura dos Arquivos de Dados

### dados_clientes.csv

Contém informações sobre os clientes, incluindo:

- `cliente_id`: Identificador único do cliente
- `data_registro`: Data de registro do cliente
- `idade`: Idade do cliente
- `genero`: Gênero do cliente
- `localizacao`: Localização do cliente
- `plano`: Plano de assinatura do cliente
- `metodo_pagamento`: Método de pagamento utilizado pelo cliente
- `qtd_meses_assinatura`: Quantidade de meses de assinatura
- `historico_pedidos`: Número de pedidos feitos pelo cliente

### dados_uso.csv

Contém informações sobre o uso do serviço pelos clientes, incluindo:

- `cliente_id`: Identificador único do cliente
- `logins_mensais`: Número de logins mensais
- `horas_uso_mensais`: Número de horas de uso mensais
- `tickets_suporte_mensais`: Número de tickets de suporte mensais
- `feedback_positivo_mensal`: Número de feedbacks positivos mensais
- `feedback_negativo_mensal`: Número de feedbacks negativos mensais


