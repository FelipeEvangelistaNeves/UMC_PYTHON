#  3) Elaborar um programa que contém uma lista com 20 elementos. 
# Essa lista deve ser preenchida pelo usuário, porém não deve conter valores repetidos e valores abaixo de 40. 
# Exibir no final a lista com os 20 elementos. 

lista = []
while len(lista) < 20:
    numero = int(input("Digite um número inteiro (maior ou igual a 40): "))
    if numero < 40:
        print("Número inválido. Digite um número maior ou igual a 40.")
    elif numero in lista:
        print("Número já existe na lista. Digite um número diferente.")
    else:
        lista.append(numero)
print("Lista final:", lista)
