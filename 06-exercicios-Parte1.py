# Databricks notebook source
# MAGIC %md
# MAGIC ### 1. Crie um programa em Python que receba uma string como entrada e imprima uma nova string com os caracteres na ordem inversa.

# COMMAND ----------

#String
entrada = "Hello World"

# Inversão da string
saida = entrada[::-1]

# String Invertida
print(saida)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 2. Crie um programa em Python que receba uma string como entrada e imprima outra string com todas as palavras em ordem inversa.

# COMMAND ----------

# String Entrada
entrada = "Hello World"

# Quebrando a string em palavras
palavras = entrada.split()

# String Invertida
palavras_inversas = palavras[::-1]

# Junta as palavras invertidas em uma nova string
saida = ' '.join(palavras_inversas)

# Impressão da string com as palavras invertidas
print(saida)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 3. Crie um programa em Python que receba uma string como entrada e imprima outra string com todas as vogais substituídas por asteriscos (*)

# COMMAND ----------

# String Entrada
entrada = "Hello World"

# Substitui as vogais por asteriscos (*)
saida = ''
for i in entrada:
    if i in 'aeiou':
        saida += '*'
    else:
        saida += i

# Impressão do resultado
print(saida)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 4. Crie um programa em Python que receba uma string como entrada e imprima outra string com todas as palavras que começam com letra maiúscula.

# COMMAND ----------

# String Entrada
entrada = "Hello world"

# Quebrando a string
palavras = entrada.split()

# Lista para colocar palavras que começam Maiusculas
palavras_m = []

# Identifica palavras que começam Maiusculas
for i in palavras:
    if i[0].isupper():
        palavras_m.append(i)

# Junta as palavras maiúsculas em uma nova string
saida = ' '.join(palavras_m)

# Impressão resultado
print(saida)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 5. Crie um programa em Python que receba uma string como entrada e verifique se ela é um palíndromo (ou seja, se pode ser lida da mesma forma da esquerda para a direita e da direita para a esquerda).

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
# MAGIC ### 6. Crie um programa em Python que receba uma string como entrada e verifique se ela é um anagrama de outra string. (ou seja, se elas possuem as mesmas letras em quantidades diferentes)

# COMMAND ----------

# String Entrada
texto1 = input("Digite a primeira string: ")
texto2 = input("Digite a segunda string: ")

# Remove os espaços em branco e transforma em minuscula
texto1 = texto1.replace(" ", "").lower()
texto2 = texto2.replace(" ", "").lower()

# Verifica se são anagramas
if sorted(texto1) == sorted(texto2):
    print("As strings são anagramas.")
else:
    print("As strings não são anagramas.")

# COMMAND ----------

# MAGIC %md
# MAGIC ### 7. Crie um programa em Python que receba uma string como entrada e imprima outra string que é formada pela primeira letra de cada palavra da string original.

# COMMAND ----------

# String Entrada
texto = input("Digite uma string: ")

# Separa as palavras
palavras = entrada.split()

# Obtém a primeira letra de cada palavra e concatena
primeiras_letras = ""
for i in palavras:
    if i:
        primeira_letra = i[0]
        primeiras_letras += primeira_letra

# Resultado
print(primeiras_letras)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 8. Crie um programa em Python que receba uma tupla de números inteiros como entrada e retorne uma nova tupla contendo apenas os números primos.

# COMMAND ----------

# Tupla de nms
numeros = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)

# Nova tupla para nms primos
numeros_primos = tuple()

# Loop
for n in numeros:
    # Verifica se o nm é maior que 1 (já que 1 não é primo)
    if n > 1:
        # Verifica se o nm é primo
        primo = True
        for i in range(2, n):
            if n % i == 0:
                primo = False
                break

        # Se o nm for primo, adiciona à nova tupla
        if primo:
            numeros_primos += (n,)

# Resultado
print(numeros_primos)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 9. Crie um programa em Python que receba duas tuplas de números inteiros como entrada e retorne uma nova tupla contendo apenas os elementos que aparecem em ambas as tuplas.

# COMMAND ----------

# Entrada
numeros1 = (1, 2, 3, 4, 5, 6)
numeros2= (4, 5, 6, 7, 8, 9)

# Cria uma nova tupla
numeros_iguais = tuple()

# Loop
for i in numeros1:
    # Verifica se o elemento está presente na segunda tupla
    if i in numeros2:
        # Se tiver o nm nas duas então acrescenta na nova tupla
        numeros_iguais += (i,)

# Resultado
print(numeros_iguais)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 10. Crie um programa em Python que receba uma tupla de strings como entrada e retorne uma nova tupla contendo apenas as strings que começam e terminam com a mesma letra.

# COMMAND ----------

# Entrada
tupla = ("arara", "casa", "mala", "ovo", "paralelepípedo", "pato")

# Nova tupla
strings_começam_igual = tuple()

# loop
for i in tupla:
    # Verifica se a palavra começa e termina com a mesma letra
    if i[0] == i[-1]:
        # Se atende ao requisito adiciona na novas tupla
        strings_começam_igual += (i,)

# Resultado
print(strings_começam_igual)

# COMMAND ----------

