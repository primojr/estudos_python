##
## Aplicar randon forest 

import pandas as pd
import matplotlib as pl
import seaborn as sns

df = pd.read_csv("date/WA_Fn-UseC_-Telco-Customer-Churn.csv")

df.head()

# Y
df['Churn'].value_counts()

df['Churn'].value_counts(normalize = True)*100

df.MonthlyCharges.hist()


ax = sns.boxplot(x = 'MonthlyCharges', y = 'Churn', data = df, orient = 'h')
ax.figure.set_size_inches(12, 4)
ax.set_title('Renda', fontsize = 18)
ax.set_xlabel('R$', fontsize = 14)
ax



