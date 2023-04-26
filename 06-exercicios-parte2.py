# Databricks notebook source
# MAGIC %md
# MAGIC ### 11. Crie um programa em Python que receba uma lista de números inteiros como entrada e retorne uma nova lista contendo apenas os números que aparecem um número ímpar de vezes.

# COMMAND ----------


numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 9, 8, 7, 6, 5, 4, 3, 2, 1]

# Dicionario para ocorrencia de numeros
contador = {}
for num in numeros:
    if num in contador:
        contador[num] += 1
    else:
        contador[num] = 1

# Lista p/ armazenar
numeros_impares = []
for num, ocorrencias in contador.items():
   # Verifica se o número de ocorrências é ímpar
    if ocorrencias % 2 != 0: 
        numeros_impares.append(num)

# Resultado
print(numeros_impares)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 12. Crie um programa em Python que receba duas listas de números inteiros como entrada e retorne uma nova lista contendo apenas os elementos que aparecem em pelo menos uma das listas, mas não em ambas.

# COMMAND ----------

# Listas
lista1 = [1, 2, 3, 4, 5, 6, 7]
lista2 = [4, 5, 6, 7, 8, 9, 10]

# Variaveis para armazenar lista
nums1 = set(lista1)
nums2 = set(lista2)

# Elementos que aparecem em pelo menos uma das listas, e nao em ambas
resultado = list((nums1.symmetric_difference(nums2)))

print(resultado)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 13. Crie um programa em Python que receba duas listas de números inteiros como entrada e retorne uma nova lista contendo apenas os elementos que aparecem em ambas as listas, mas sem repetições.

# COMMAND ----------

lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]

# Cria um conjunto para armazenar os elementos únicos de cada lista
nums1  = set(lista1)
nums2 = set(lista2)

# Obtém a interseção entre os conjuntos
resultado = list(nums1.intersection(nums2))


print(resultado)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 14. Crie um programa em Python que receba uma lista de dicionários como entrada, onde cada dicionário representa um produto com nome e preço, e retorne o nome do produto mais caro.

# COMMAND ----------

produtos = [{"nome": "celular", "preco": 1500},
            {"nome": "notebook", "preco": 3500},
            {"nome": "tablet", "preco": 1200},
            {"nome": "fones de ouvido", "preco": 200},
            {"nome": "smartwatch", "preco": 800}]

# Definição variáveis
produto_caro = ""
preco_caro = 0

# Loop para percorrer a lista
for produto in produtos:
    nome = produto["nome"]
    preco = produto["preco"]
    
    # Compara os preços dos produtos de um em um, até ficar o mais caro
    if preco > preco_caro:
        produto_caro = nome
        preco_caro = preco

# Resultado
print("O produto mais caro é :", produto_caro)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 15. Crie um programa em Python que receba um dicionário como entrada, onde as chaves representam nomes de produtos e os valores representam as quantidades disponíveis em estoque, e retorne o nome do produto com estoque mais baixo.

# COMMAND ----------

estoque = {"celular": 50, "notebook": 20, "tablet": 100, "fones de ouvido": 5, "smartwatch": 15}

# Definição variáveis
produto_mais_baixo = ""
quantidade_mais_baixo = float('inf')

# loop
for produto, quantidade in estoque.items():
    
    # verifica e preenche sempre que a quantidade for mais baixa
    if quantidade < quantidade_mais_baixo:
        produto_mais_baixo = produto
        quantidade_mais_baixo = quantidade
        
print(produto_mais_baixo)