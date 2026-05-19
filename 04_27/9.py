# 9) Elaborar um programa que contém uma lista com 15 elementos. Essa lista deve ser preenchida pelo
# usuário, porém não deve conter valores repetidos. Exibir no final a lista.

lista = []
while len(lista)<15:
  valor = int(input("digite um valor"))
  if valor not in lista:
    lista.append(valor)
  else:
    print("valor repetido, digite outro valor")
    
print(lista)