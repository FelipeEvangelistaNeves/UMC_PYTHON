# 1. Elaborar um programa que o usuário deve digitar 10 números inteiros
#  (esses números devem ser armazenados em uma lista) e ao final o 
# programa deve mostrar quantos números são pares e quantos são ímpares.

numeros = []
for i in range(1,11):
    numero = int(input(f"Digite o {i}º número inteiro: "))
    numeros.append(numero)
pares = 0
impares = 0
for numero in numeros:
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
print(f"Quantidade de números pares: {pares}")
print(f"Quantidade de números ímpares: {impares}")
