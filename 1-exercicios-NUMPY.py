# Databricks notebook source
# MAGIC %md
# MAGIC ### 1. Criar um array com 10 números inteiros aleatórios entre 1 e 50 e calcular a média e o desvio padrão

# COMMAND ----------

import numpy as np

# Array de 10 numeros inteiros aleatórios
array_random = np.random.randint(1, 51, 10)

# Calculo média
media = np.mean(array_random)

# Calculo desvio padrao
desvio_padrao = np.std(array_random)

print("Array: ", array_random)
print("")
print("Média: ", media)
print("")
print("Desvio Padrão: ", desvio_padrao)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 2. Criar um array de 10 números aleatórios e calcular a raiz quadrada de todos os valores menores ou iguais a 0,5

# COMMAND ----------

import numpy as np

# Array 10 numeros aleatorios
array_random = np.random.rand(10)

# valores menores ou iguais a 0,5
array_filtrado = array_random[array_random <= 0.5]

# Calcular a raiz quadrada dos valores filtrados
array_raiz_quadrada = np.sqrt(array_filtrado)


print("Array: ", array_random)
print("")
print("Valores menores ou iguais a 0,5: ", array_filtrado)
print("")
print("Raiz quadrada: ", array_raiz_quadrada)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 3. Criar uma matriz 3D de tamanho 3x3x3 com valores aleatórios e exibir o valor máximo de cada linha de cada matriz 2D dentro dessa matriz 3D

# COMMAND ----------

import numpy as np

# Criar uma matriz 3D
matriz_3d = np.random.rand(3, 3, 3)

# Calcular o valor máximo de cada linha de cada matriz 2D
valores_maximos = np.max(matriz_3d, axis=1)


print("Matriz 3d: ", matriz_3d)
print("")
print("Valores máximos de cada matriz 2d: ", valores_maximos)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 4. Criar uma matriz de tamanho 5x5 com valores aleatórios e subtrair a média de cada linha dessa matriz

# COMMAND ----------

import numpy as np

# Criar Matrioz
matriz = np.random.rand(5, 5)

# Calcular a média de cada linha
media_linhas = np.mean(matriz, axis=1)

# Subtrair a média de cada linha
matriz_subtraida = matriz - media_linhas[:, np.newaxis]

print("Matriz original: ",matriz )
print("")
print("Matriz média: ",media_linhas )
print("")
print("matriz_subtraida: ", matriz_subtraida )


# COMMAND ----------

# MAGIC %md
# MAGIC ### 5. Criar uma matriz de tamanho 4x4 com valores aleatórios e calcular a média e o desvio padrão das diagonais da matriz

# COMMAND ----------

import numpy as np

# matriz 4x4
matriz = np.random.rand(4, 4)

# Extrair as diagonais da matriz
diagonal_principal = np.diag(matriz)
diagonal_secundaria = np.diag(np.fliplr(matriz))

# Média e o desvio padrão das diagonais
media_diagonal_principal = np.mean(diagonal_principal)
desvio_padrao_diagonal_principal = np.std(diagonal_principal)

media_diagonal_secundaria = np.mean(diagonal_secundaria)
desvio_padrao_diagonal_secundaria = np.std(diagonal_secundaria)


print("Matriz original: ", matriz)
print("")
print("Média da diagonal principal:", media_diagonal_principal)
print("")
print("Desvio padrão da diagonal principal:", desvio_padrao_diagonal_principal)
print("")
print("Média da diagonal secundária:", media_diagonal_secundaria)
print("")
print("Desvio padrão da diagonal secundária:", desvio_padrao_diagonal_secundaria)

# COMMAND ----------

