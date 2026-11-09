from scipy.stats import chi2_contingency
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Función que calcula el coeficiente de cramer
def v_cramer_corregido(col1, col2):
  tabla_cont = pd.crosstab(col1, col2)
  estadistico_chi2 = chi2_contingency(tabla_cont)[0]
  n = tabla_cont.sum().sum()
  estadistico_phi2 = estadistico_chi2 / n
  renglon, columnas = tabla_cont.shape
  phi2corr = max(0, estadistico_phi2 - ((columnas-1)*(renglon-1))/(n-1))
  renglon_corr = renglon - ((renglon-1)**2)/(n-1)
  columnas_corr = columnas - ((columnas-1)**2)/(n-1)
  return np.sqrt(phi2corr / min((columnas_corr-1), (renglon_corr-1)))

#Función que calcula el coeficiente de correlación entre las variables numéricas
def correlacion_numericas(df):
  """
  Seleccionamos las variables numéricas y luego calculamos la correlación entre
  las variables númericas más la variable objetivo churn
  """
  variables_numericas = df.select_dtypes(include=['number'])
  variables_numericas['Churn'] = df['Churn'].replace({'no': 0, 'yes': 1})
  df_corr = variables_numericas.corr()
  return df_corr

def graficos_correlacion(df):
  "Función que grafíca la matriz de correlación"
  mascara_numericas = np.triu(np.ones_like(df, dtype=bool))
  fig, ax = plt.subplots(figsize=(12,10))
  sns.heatmap(df, annot=True, cmap='coolwarm', fmt=".2f", mask=mascara_numericas, ax=ax)
  return fig

