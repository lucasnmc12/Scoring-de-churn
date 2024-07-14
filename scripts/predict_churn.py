import pandas as pd
import joblib
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report

# Carregar dados combinados
dados_combinados = pd.read_csv('data/dados_combinados.csv', sep=';')

# Carregar modelo treinado
modelo = joblib.load('models/modelo_churn.pkl')

# Selecionar colunas usadas durante o treinamento (incluindo 'cliente_id' para alinhar)
colunas_modelo = [
    'cliente_id', 'idade', 'qtd_meses_assinatura', 'logins_mensais',
    'horas_uso_mensais', 'tickets_suporte_mensais', 'feedback_positivo_mensal',
    'feedback_negativo_mensal'
]

# Verificar se todas as colunas necessárias estão presentes nos dados combinados
for col in colunas_modelo:
    if col not in dados_combinados.columns:
        raise ValueError(f"A coluna necessária '{col}' não está presente nos dados combinados.")

# Fazer previsões (removendo 'cliente_id' antes de passar os dados ao modelo)
X_input = dados_combinados[colunas_modelo].drop(columns=['cliente_id'])
dados_combinados['churn_pred'] = modelo.predict(X_input)

# Salvar previsões em um novo arquivo CSV
dados_combinados.to_csv('data/dados_combinados_com_previsoes.csv', sep=';', index=False)
print("Previsões concluídas e salvas.")

# Avaliar a probabilidade de acerto (se a coluna 'churn' verdadeira estiver presente)
if 'churn' in dados_combinados.columns:
    y_true = dados_combinados['churn']
    y_pred = dados_combinados['churn_pred']

    # Calcular as métricas
    accuracy = accuracy_score(y_true, y_pred)
    precision = precision_score(y_true, y_pred)
    recall = recall_score(y_true, y_pred)
    f1 = f1_score(y_true, y_pred)
    report = classification_report(y_true, y_pred, output_dict=True)

    # Adicionar métricas ao DataFrame
    metrics_df = pd.DataFrame(report).transpose()
    metrics_df['accuracy'] = accuracy
    metrics_df.loc['accuracy', 'f1-score'] = accuracy
    metrics_df.loc['accuracy', 'precision'] = '-'
    metrics_df.loc['accuracy', 'recall'] = '-'
    metrics_df['support'] = metrics_df['support'].astype(int)

    # Salvar métricas em um novo arquivo CSV
    metrics_df.to_csv('data/metrics.csv', sep=';', index=True)

    # Exibir as métricas
    print(f"Acurácia: {accuracy}")
    print(f"Precisão: {precision}")
    print(f"Recall: {recall}")
    print(f"F1-Score: {f1}")
    print("\nRelatório de Classificação:\n", metrics_df)
else:
    # Informar que a coluna 'churn' não está presente e que as métricas não foram calculadas
    print("A coluna 'churn' não está presente nos dados combinados. As métricas de desempenho não foram calculadas.")
