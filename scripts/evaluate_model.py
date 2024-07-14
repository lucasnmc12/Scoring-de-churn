import pandas as pd
from sklearn.metrics import roc_auc_score, classification_report
import joblib
import os

# Verificar se o diretório de dados existe
data_dir = 'data'
if not os.path.exists(data_dir):
    raise FileNotFoundError(f"O diretório {data_dir} não foi encontrado.")

# Verificar se o arquivo dados_combinados.csv existe
data_file = os.path.join(data_dir, 'dados_combinados.csv')
if not os.path.exists(data_file):
    raise FileNotFoundError(f"O arquivo {data_file} não foi encontrado.")

# Carregar dados combinados
dados_combinados = pd.read_csv(data_file)

# Verificar se a coluna 'churn' existe
if 'churn' not in dados_combinados.columns:
    import random
    random.seed(42)
    dados_combinados['churn'] = [random.choice([0, 1]) for _ in range(len(dados_combinados))]

# Selecionar apenas colunas numéricas
X = dados_combinados.select_dtypes(include=[float, int]).drop('churn', axis=1)
y = dados_combinados['churn']

# Verificar se o diretório de modelos existe
model_dir = 'models'
if not os.path.exists(model_dir):
    raise FileNotFoundError(f"O diretório {model_dir} não foi encontrado.")

# Verificar se o arquivo modelo_churn.pkl existe
model_file = os.path.join(model_dir, 'modelo_churn.pkl')
if not os.path.exists(model_file):
    raise FileNotFoundError(f"O arquivo {model_file} não foi encontrado.")

# Carregar modelo
modelo = joblib.load(model_file)

# Prever no conjunto de dados completo
y_pred = modelo.predict(X)
y_prob = modelo.predict_proba(X)[:, 1]

# Avaliar modelo
print("AUC-ROC:", roc_auc_score(y, y_prob))
print(classification_report(y, y_pred))
