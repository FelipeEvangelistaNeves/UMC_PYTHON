N = []
var = int(input("Digite um número inteiro: "))
while var !=1:
  if var % 2 == 0:
    N.append(var)
  if var <= 0:
    print("Número inválido. Digite um número inteiro positivo.")
  var = int(input("Digite um número inteiro: "))
print("Números pares digitados:", N)