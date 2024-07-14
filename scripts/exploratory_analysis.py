import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar dados combinados
dados_combinados = pd.read_csv('data/dados_combinados.csv')

# Selecionar apenas colunas numéricas
dados_numericos = dados_combinados.select_dtypes(include=[float, int])

# Análise de correlação
corr = dados_numericos.corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Matriz de Correlação dos Dados Combinados')
plt.show()

# Estatísticas descritivas
print(dados_combinados.describe())
