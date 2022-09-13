### 


## Usando tensoflow

##### Bibliotecas Auxiliares
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras

np.random.seed(13)

df = pd.read_csv("C:\R\Dir\lookalike_cliente_cartao\date\dfFAmostra.csv", delimiter=";")

df.head(2)


# # TensorFlow e tf.keras
# import tensorflow as tf
# from tensorflow import keras


# print(tf.__version__)

######## Ajuste da base ------- 
# Sys
df['system'] = df['system'].replace('android','1')
df['system'] = df['system'].replace('ios','0')
df['system'] = df['system'].astype(float)

# Classe cep
df['class_cep'].value_counts()
df['class_cep'] = df['class_cep'].replace('A.Ruim','0')
df['class_cep'] = df['class_cep'].replace('B.Neutro','1')
df['class_cep'] = df['class_cep'].replace('C.Medio','2')
df['class_cep'] = df['class_cep'].replace('D.Bom','3')
df['class_cep'] = df['class_cep'].replace('E.MuitoBom','4')
df['class_cep'] = df['class_cep'].astype(float)


# Binario resposta
df.loc[df['classe1'] == 'ComCartaoApp', 'Class'] = 1
df.loc[df['classe1'] != 'ComCartaoApp', 'Class'] = 0
df = df.drop('classe1',axis=1)
df.head()


# Remover na()
df = df.dropna()
df = df.reset_index()

# Tipos dos dados
df.dtypes


######### Separar treino e teste
#df = df.loc[:,df.columns[1:]]
X = df.loc[:, df.columns[2:14]]
y = df.loc[:,['Class']]

n_aleatorio = np.arange(df.shape[0])
np.random.shuffle(n_aleatorio)

X_train = X.loc[n_aleatorio[:3000],:]
X_test  = X.loc[n_aleatorio[3000:],:]

y_train = y.loc[n_aleatorio[:3000],:]
y_test  = y.loc[n_aleatorio[3000:],:]


tf.random.set_seed(42)


model = tf.keras.Sequential([
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(256, activation='relu'),
    tf.keras.layers.Dense(256, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

model.compile(
    loss=tf.keras.losses.binary_crossentropy,
    optimizer=tf.keras.optimizers.Adam(lr=0.01),
    metrics=[
        tf.keras.metrics.BinaryAccuracy(name='accuracy'),
        tf.keras.metrics.Precision(name='precision'),
        tf.keras.metrics.Recall(name='recall')
    ]
)

history = model.fit(X_train, y_train, epochs=100)
history = model.fit(X_test, y_test, epochs=100)


pd.DataFrame(history.history).plot(figsize = (8,5))
plt.grid(True)
plt.gca().set_ylim(0,1)
plt.show()
