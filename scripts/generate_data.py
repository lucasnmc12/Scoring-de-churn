import pandas as pd
import numpy as np
from faker import Faker
import random
import os

# Inicializar Faker
fake = Faker('pt_BR')

# Número de registros que queremos gerar
num_records = 1000

# Função para gerar dados de clientes
def generate_client_data(num_records):
    client_data = {
        'cliente_id': np.arange(1, num_records + 1),
        'data_registro': [fake.date_between(start_date='-3y', end_date='today') for _ in range(num_records)],
        'idade': [random.randint(18, 70) for _ in range(num_records)],
        'genero': [random.choice(['M', 'F']) for _ in range(num_records)],
        'localizacao': [fake.city() for _ in range(num_records)],
        'plano': [random.choice(['Básico', 'Standard', 'Premium']) for _ in range(num_records)],
        'metodo_pagamento': [random.choice(['Cartão de Crédito', 'PayPal', 'Boleto']) for _ in range(num_records)],
        'qtd_meses_assinatura': [random.randint(1, 36) for _ in range(num_records)]
    }
    return pd.DataFrame(client_data)

# Função para gerar dados de uso
def generate_usage_data(client_ids):
    usage_data = {
        'cliente_id': client_ids,
        'logins_mensais': [random.randint(0, 50) for _ in range(len(client_ids))],
        'horas_uso_mensais': [random.randint(0, 200) for _ in range(len(client_ids))],
        'tickets_suporte_mensais': [random.randint(0, 10) for _ in range(len(client_ids))],
        'feedback_positivo_mensal': [random.randint(0, 10) for _ in range(len(client_ids))],
        'feedback_negativo_mensal': [random.randint(0, 5) for _ in range(len(client_ids))]
    }
    return pd.DataFrame(usage_data)

# Gerar dados de clientes
dados_clientes = generate_client_data(num_records)

# Usar os mesmos cliente_ids para dados de uso
client_ids = dados_clientes['cliente_id']
dados_uso = generate_usage_data(client_ids)

# Criar diretório 'data' se não existir
if not os.path.exists('data'):
    os.makedirs('data')

# Salvar dados em arquivos CSV com delimitador ponto e vírgula
dados_clientes.to_csv('data/dados_clientes.csv', sep=';', index=False)
dados_uso.to_csv('data/dados_uso.csv', sep=';', index=False)

print("Dados gerados e salvos.")
