# Databricks notebook source
# MAGIC %md
# MAGIC ### 1. Some todos os números de 1 até 100

# COMMAND ----------

# Váriavel
soma = 0

# Loop para somar os números de 1 a 100
for i in range(1, 101):
    soma += i

soma

# COMMAND ----------

# MAGIC %md
# MAGIC ### 2. Some todos os números pares de 1 até 100

# COMMAND ----------

# Váriavel
soma = 0

# Loop para somar os números pares de 1 a 100
for i in range(2, 101, 2):
    soma += i

soma

# COMMAND ----------

# MAGIC %md
# MAGIC ### 3. Some todos os números ímpares de 1 até 100

# COMMAND ----------

# Váriavel
soma = 0

# Loop para somar os números pares de 1 a 100
for i in range(1, 101, 2):
    soma += i

soma

# COMMAND ----------

# MAGIC %md
# MAGIC ### 4. Dada a lista abaixo, some todos os elementos inteiros positivos

# COMMAND ----------

lista = [-2, 2, 'celular', 10, -99, False]
lista

# COMMAND ----------

# Váriavel
soma = 0

# Lista
numeros = [-2, 2, 'celular', 10, -99, False]

# Loop para somar os números inteiros positivos da lista
for i in numeros:
    if isinstance(i, int) and i > 0:  # Verificar se o elemento é um inteiro positivo
        soma += i
        
soma

# COMMAND ----------

# MAGIC %md
# MAGIC ### 5. Dada a String

# COMMAND ----------

string = 'pYthOn É A mELhoR LiNguaGEM De PRoGRaMaçãO'
string

# COMMAND ----------

# MAGIC %md
# MAGIC Formate-a com as primeiras letras maiúsculas:

# COMMAND ----------

string = 'pYthOn É A mELhoR LiNguaGEM De PRoGRaMaçãO'

#Formatação de primeira letra maiuscula
string_Primeira_Letra_M = string.title()

string_Primeira_Letra_M

# COMMAND ----------

# MAGIC %md
# MAGIC Com todas as letras minúsculas

# COMMAND ----------

string = 'pYthOn É A mELhoR LiNguaGEM De PRoGRaMaçãO'

#Formatação de tudo minuscula
string_Minuscula = string.lower()

string_Minuscula

# COMMAND ----------

# MAGIC %md
# MAGIC Com todas as letras maiúsculas

# COMMAND ----------

string = 'pYthOn É A mELhoR LiNguaGEM De PRoGRaMaçãO'

#Formatação de tudo maiuscula
string_Maiuscula = string.upper()

string_Maiuscula

# COMMAND ----------

