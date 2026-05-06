# 5) Elaborar uma função que recebe 3 valores (A, B e C) do tipo float (parâmetros) e retornar para a função
# principal o resultado da seguinte soma: (A3+B5+C). Utilize a função do exercício 4.
def potencia(x, n):
  resultado =1
  for i in range(1, n+1):
    resultado = resultado * x
  return resultado
def soma(a:float, b:float, c:float):
  return potencia(a,3) + potencia(b,5) + c
val1 = float(input("Digite o valor de A: "))
val2 = float(input("Digite o valor de B: "))
val3 = float(input("Digite o valor de C: "))
print(soma(val1, val2, val3))