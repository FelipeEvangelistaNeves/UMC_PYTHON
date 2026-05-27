# 3. Elaborar um programa que o usuário deve digitar 12 
# números inteiros (esses números devem ser armazenados em uma lista)
#  e em seguida o programa deve mostrar: todos os números positivos (armazenados em outra lista), 
# todos os números negativos (armazenados em outra lista), a quantidade de zeros digitados.
numeros_inteiros = []
for i in range(1, 13):
    numero = int(input(f"Digite o {i}º número inteiro: "))
    numeros_inteiros.append(numero)
numeros_positivos = []
numeros_negativos = []
quantidade_zeros = 0
for numero in numeros_inteiros:
    if numero > 0:
        numeros_positivos.append(numero)
    elif numero < 0:
        numeros_negativos.append(numero)
    else:
        quantidade_zeros += 1
print(f"Números positivos: {numeros_positivos}")
print(f"Números negativos: {numeros_negativos}")
print(f"Quantidade de zeros: {quantidade_zeros}")
