# 5. Elaborar um programa que o usuário deve digitar 15 números inteiros 
# (esses números devem ser armazenados em uma lista).
#  Depois o programa deve mostrar: quantas vezes o número 10 apareceu e em quais posições o número 10 foi encontrado.
numeros_inteiros = []
for i in range(1, 16):
    numero = int(input(f"Digite o {i}º número inteiro: "))
    numeros_inteiros.append(numero)
quantidade_10 = 0
posicoes_10 = []
for i in range(len(numeros_inteiros)):
    if numeros_inteiros[i] == 10:
        quantidade_10 += 1
        posicoes_10.append(i)
print(f"O número 10 apareceu {quantidade_10} vezes.")
print(f"O número 10 foi encontrado na {posicoes_10} posição(s).")
