# Estudo da função apply
#  Aplicação apply dentro de dataframes
# 
# !pip install seaborn

import pandas as pd
import numpy as np
import seaborn as sns

# Carregar base de exemplo
titanic = sns.load_dataset("titanic")

print(titanic.info())

# Criar funções

# 1
def desc_missing(vetor):
  """
  Criar um resumo de dos missing
  Contar o numero de missing de um vetor
  """
  null_vec = pd.isnull(vetor)       # Criar boleano de valores faltantes
  null_count = np.sum(null_vec)     # Somar a quantidade de missing
  n_vetor = vetor.size              # Tamando total do vetor 
  perc_missing = null_count/n_vetor # Calculcar o percentual de valores faltantes
  
  return ['d': null_count, 'ss': perc_missing]


titanic.apply(desc_missing)

# 2
def prop_faltantes(vetor):
  """
  Calcular o percentual de valores faltantes de um vector
  """
  

