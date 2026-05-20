# 2. Elaborar um programa que o usuário deve digitar 8 números reais
#  (esses números devem ser armazenados em uma lista) 
# e depois o programa deve mostrar: todos os números digitados, 
# o maior número, o menor número e a diferença entre o maior e o menor valor.
numeros_reais = []
for i in range(1, 9):
    numero = float(input(f"Digite o {i}º número real: "))
    numeros_reais.append(numero)
print(f"Números digitados: {numeros_reais}")
maior_numero = max(numeros_reais)
menor_numero = min(numeros_reais)
diferenca = maior_numero - menor_numero
print(f"Maior número: {maior_numero}")
print(f"Menor número: {menor_numero}")
print(f"Diferença entre o maior e o menor: {diferenca}")
