# Databricks notebook source
# MAGIC %md
# MAGIC ### 21. Crie um programa em Python que receba uma string como entrada e imprima a string sem as vogais.

# COMMAND ----------

# String Entrada
entrada = "Hello World"

# Substitui as vogais por asteriscos (*)
saida = ''
for i in entrada:
    if i in 'aeiou':
        saida += ''
    else:
        saida += i

# Impressão do resultado
print(saida)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 22. Crie um programa em Python que imprima a soma dos n primeiros números primos, onde n é um número fornecido pelo usuário.

# COMMAND ----------

n = int(input("Digite um número: "))

#variaveis
soma = 0
contagem = 0
numero = 2

#loop e condição
while contagem < n:
    primo = True
    for i in range(2, numero):
        if numero % i == 0:
            primo = False
            break
    if primo:
        soma += numero
        contagem += 1
    numero += 1

print(soma)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 23. Crie um programa em Python que receba uma lista de números e imprima a soma dos números pares e a soma dos números ímpares presentes na lista.

# COMMAND ----------

numeros = [2, 5, 9, 12, 18, 23, 27, 30, 35, 40]


soma_pares = 0
soma_impares = 0

for numero in numeros:
    if numero % 2 == 0:
        soma_pares += numero  # Soma Par
    else:
        soma_impares += numero  # Soma Impar

print("Soma dos números pares: ", soma_pares)
print("Soma dos números ímpares: ", soma_impares)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 24. Crie um programa em Python que receba uma lista de strings e retorne uma lista com todas as strings que começam e terminam com a mesma letra.

# COMMAND ----------

palavras = ["amor", "futebol", "verdade", "banana", "arara", "casa", "sol"]
palavras_selecionadas = []

for palavra in palavras:
    if len(palavra) > 1 and palavra[0] == palavra[-1]:
        palavras_selecionadas.append(palavra)

print("Palavras selecionadas: ", palavras_selecionadas)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 25. Crie um programa em Python que leia um número do usuário e verifique se ele é um número perfeito. Um número perfeito é aquele que é igual à soma de seus divisores próprios (ou seja, a soma de seus fatores inteiros positivos, excluindo ele próprio).

# COMMAND ----------

numero = int(input("Digite um número: "))

#Lista para armazenamento de numeros e Variavel
divisores = []
soma_divisores = 0

#Loop e condição
for i in range(1, numero):
    if numero % i == 0:
        divisores.append(i)
        soma_divisores += i

if soma_divisores == numero:
    print(numero, "é um número perfeito.")
else:
    print(numero, "não é um número perfeito.")

# COMMAND ----------

# MAGIC %md
# MAGIC ### 26. Crie um programa em Python que calcule a série de Fibonacci para um determinado número de termos fornecido pelo usuário. A série de Fibonacci é uma sequência em que cada número é a soma dos dois números anteriores: 0, 1, 1, 2, 3, 5, 8, 13, ...

# COMMAND ----------

termos = int(input("Digite o número de termos desejados: "))
fibonacci = [0, 1]
i = 2

#loop
while i < termos:
    proximo = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(proximo)
    i += 1

print(fibonacci)