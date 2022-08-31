##
## Conhecer os dados 
import pandas as pd


# Ler dataframe

df = pd.read_csv("date/WA_Fn-UseC_-Telco-Customer-Churn.csv")

#
## informaçoes macro
#
df.head()     # Visão geral
type(df)      # Saber qual a estrutura da base
df.shape      # Dimensão da base
df.columns    # Nome das colunas do DF
df.dtypes     # Estrutura das colunas
df.info()     # Visão detalhada da estrutura

#
## fitro de coluna 
#
df['gender']
df.gender.head() # Top 5 informações da coluna
df.gender.tail() # Ultimas 5 informações da coluna

df[['gender','Churn']] # Selecionar varias colunas

#
# ## Filto de linha
# ps. No python o indece começa em Zero

df.loc[0] # Dados da 1º linha do DF
df.loc[9] # Dados da 10º linha do DF
df.loc[[0,9,99]]

#
## Cominando selecao de linhas e colunas
#
df.loc[:9,['gender','Churn']] # Selecinar as top 10 linhas das colunas genero e churn
df.loc[9:,['gender','Churn']] # Selecinar a parti da 10 linhas das colunas genero e churn

colunas = df.columns[1:5]
linhas = [0,9,99]
df.loc[linhas, colunas]


# Count 
df['Churn'].value_counts() # Absoluto
df['Churn'].value_counts()/df['Churn'].value_counts().sum() # Proporção
