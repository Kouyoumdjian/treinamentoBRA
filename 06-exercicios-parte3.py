# Databricks notebook source
# MAGIC %md
# MAGIC ### 16. Crie um programa em Python que receba uma lista de dicionários como entrada, onde cada dicionário representa um aluno com nome e notas em diferentes disciplinas, e retorne o nome do aluno com a maior média ponderada, sendo que a média ponderada deve ser calculada utilizando as notas como pesos.

# COMMAND ----------



alunos = [
    {"nome": "João", "notas": {"Matemática": 8.5, "Português": 9.0, "História": 7.0}},
    {"nome": "Maria", "notas": {"Matemática": 9.5, "Português": 8.5, "História": 6.0}},
    {"nome": "Pedro", "notas": {"Matemática": 7.0, "Português": 6.5, "História": 9.0}},
    {"nome": "Ana", "notas": {"Matemática": 8.0, "Português": 7.5, "História": 8.0}}
]

#Variaveis
maior_media_ponderada = float(-1)
nome_aluno_maior_media_ponderada = ""

#loop
for aluno in alunos:
    nome = aluno["nome"]
    notas = aluno["notas"]
    # Calcula a média ponderada
    media_ponderada = (notas["Matemática"] * 2 + notas["Português"] * 3 + notas["História"] * 2) / 7
    if media_ponderada > maior_media_ponderada:
        maior_media_ponderada = media_ponderada
        nome_aluno_maior_media_ponderada = nome

print("Maior média ponderada é:", nome_aluno_maior_media_ponderada)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 17. Crie um programa em Python que receba três números como entrada e imprima "Maior" se o primeiro número for maior do que a soma dos outros dois, "Menor" se o primeiro número for menor do que a soma dos outros dois, ou "Igual" caso contrário.

# COMMAND ----------

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

# soma dos dois últimos números
soma = num2 + num3

# Condições
if num1 > soma:
    print("Maior")
elif num1 < soma:
    print("Menor")
else:
    print("Igual")

# COMMAND ----------

# MAGIC %md
# MAGIC ### 18. Crie um programa em Python que receba a idade e a altura de uma pessoa como entrada e classifique-a de acordo com as seguintes regras: se a idade for menor do que 18 anos e a altura for menor do que 1,60 m, imprimir "Adolescente Baixo"; se a idade for menor do que 18 anos e a altura for maior do que 1,60 m, imprimir "Adolescente Alto"; se a idade for maior ou igual a 18 anos e a altura for menor do que 1,60 m, imprimir "Adulto Baixo"; se a idade for maior ou igual a 18 anos e a altura for maior do que 1,60 m, imprimir "Adulto Alto".

# COMMAND ----------

idade = int(input("Digite a idade: "))
altura = float(input("Digite a altura: "))

# Condicoes
if idade < 18 and altura < 1.60:
    print("Adolescente Baixo")
elif idade < 18 and altura >= 1.60:
    print("Adolescente Alto")
elif idade >= 18 and altura < 1.60:
    print("Adulto Baixo")
else:
    print("Adulto Alto")

# COMMAND ----------

# MAGIC %md
# MAGIC ### 19. Crie um programa em Python que receba uma string como entrada e imprima "Palíndromo" se a string for um palíndromo (ou seja, se a string lida de trás para frente for igual à string original), ou "Não Palíndromo" caso contrário.

# COMMAND ----------

# String Entrada
texto = input("Digite uma string: ")

# Remove os espaços em branco e transformo em minuscula
texto = texto.replace(" ", "").lower()


# Verifica se é um palíndromo
if texto == texto[::-1]:
    print("A entrada é um palíndromo.")
else:
    print("A entrada não é um palíndromo.")
    
#Imprimindo o resultado só pra verificar
print(texto)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 20. Crie um programa em Python que receba uma lista de números inteiros como entrada e calcule a soma dos quadrados dos números ímpares da lista.

# COMMAND ----------

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]

#variavel
         
soma_quadrados_impares = 0


for num in lista:
    # Verifica se o número é ímpar
    if num % 2 != 0: 
         # Soma o quadrado do número ímpar à variável soma
        soma_quadrados_impares += num ** 2  


print(soma_quadrados_impares)