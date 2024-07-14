import pandas as pd
import random

# Carregar dados
dados_clientes = pd.read_csv('data/dados_clientes.csv', sep=';')
dados_uso = pd.read_csv('data/dados_uso.csv', sep=';')

# Limpeza de dados
dados_clientes.dropna(inplace=True)
dados_uso.fillna(0, inplace=True)

# Remover duplicatas
dados_clientes.drop_duplicates(inplace=True)

# Transformar tipo de dados
dados_clientes['data_registro'] = pd.to_datetime(dados_clientes['data_registro'], format='%Y-%m-%d')

# Engenharia de Recursos
dados_uso_aggregado = dados_uso.groupby('cliente_id').sum().reset_index()

# Mesclar os dados dos clientes com os dados agregados de uso
dados_combinados = pd.merge(dados_clientes, dados_uso_aggregado, on='cliente_id', how='left')
dados_combinados.fillna(0, inplace=True)  # Preencher valores nulos com 0

# Adicionar coluna 'churn' (dados simulados)
#random.seed(42)
#dados_combinados['churn'] = [random.choice([0, 1]) for _ in range(len(dados_combinados))]

# Salvar dados limpos e combinados
dados_clientes.to_csv('data/dados_clientes_limpos.csv', sep=';', index=False)
dados_uso.to_csv('data/dados_uso_limpos.csv', sep=';', index=False)
dados_combinados.to_csv('data/dados_combinados.csv', sep=';', index=False)

print("Engenharia de recursos concluída e dados salvos.")
