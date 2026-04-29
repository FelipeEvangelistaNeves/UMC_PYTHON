lista_A= []
for i in range(10):  
  lista_A.append(int(input("Digite um número inteiro: ")))
print("lista A: ", lista_A)


lista_B = []
for num in lista_A:
  if num % 2 == 0:
    lista_B.append(num**2)
  else:
    lista_B.append(num**3)
lista_B_cresc=sorted(lista_B)
print("lista B: ", lista_B)
print("lista B: ", lista_B_cresc)