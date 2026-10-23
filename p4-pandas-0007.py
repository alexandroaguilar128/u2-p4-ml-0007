import pandas as pd
import numpy as np
# Alexandro Aguilar NC 0007
n_filas = 5
n_columnas = 5
tag_columna = tuple('ABCDE') # etiquetas para las columnas
print(tag_columna)
matriz = np.random.randint(1, 6, size=(n_filas, n_columnas))
print("Genera matriz de 5 filas por 5 columnas")
print("con numeros aleatorios comprendidos entre 1 y 10")
print(matriz)
# La variable df es DataFrame
df = pd.DataFrame(matriz, columns= tag_columna)
print("--- La tabla o dataframe --- NC 0007")
print(df)
print("--- Alexandro Aguilar --- NC 0007")