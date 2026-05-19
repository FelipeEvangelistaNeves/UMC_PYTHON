# 8) Elaborar um programa que o usuário deva preencher uma lista com 20 números inteiros. Após preencher
# a lista o programa deve verificar para cada número, se ele é primo ou não. O programa deve armazenar
# apenas os números primos em uma nova lista. Exiba a lista de primos e a quantidade encontrada.

lista = []
quantosvalores = int(input("quantos valores você quer inserir? "))
while len(lista)<quantosvalores:
  valor = int(input("digite um valor"))
  lista.append(valor)

primos = []
for numero in lista:
  if numero >1:
    primo = True
    for i in range(2,numero):
      if numero % i == 0:
        primo = False
    if primo:
      primos.append(numero)
print("números primos: ", primos)
print("quantidade de números primos: ", len(primos))