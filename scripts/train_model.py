import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib

# Carregar dados combinados
dados_combinados = pd.read_csv('data/dados_combinados.csv', sep=';')

# Verificar se a coluna 'churn' está presente
if 'churn' not in dados_combinados.columns:
    raise ValueError("A coluna 'churn' não está presente nos dados combinados.")

# Selecionar colunas usadas durante o treinamento (incluindo 'cliente_id' para alinhar)
colunas_modelo = ['cliente_id', 'idade', 'qtd_meses_assinatura', 'logins_mensais', 'horas_uso_mensais', 'tickets_suporte_mensais', 'feedback_positivo_mensal', 'feedback_negativo_mensal']
X = dados_combinados[colunas_modelo]
y = dados_combinados['churn']

# Dividir os dados em conjuntos de treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(X.drop(columns=['cliente_id']), y, test_size=0.2, random_state=42)

# Treinar modelo
modelo = RandomForestClassifier(n_estimators=100, random_state=42)
modelo.fit(X_train, y_train)

# Fazer previsões no conjunto de teste
y_pred = modelo.predict(X_test)

# Avaliar o modelo
accuracy = accuracy_score(y_test, y_pred)
print(f"Acurácia: {accuracy}")
print(classification_report(y_test, y_pred))

# Salvar modelo treinado
joblib.dump(modelo, 'models/modelo_churn.pkl')

print("Modelo treinado e salvo.")
