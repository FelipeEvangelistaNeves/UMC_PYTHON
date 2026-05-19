lista_A = []
for i in range(10):
    num = int(input("Digite um número inteiro: "))
    lista_A.append(num)
soma = lista_A[3] + lista_A[4] + lista_A[6] + lista_A[9]
print("A soma dos elementos nas posições 3, 4, 6 e 9 é:", soma)
lista_A[8] = -9
for b in range(len(lista_A)):
    print(lista_A[b], end=" - ")
  