# 2) Elaborar uma função que receba dois números inteiros positivos por parâmetro e retorne a soma dos N
# números inteiros existentes entre eles (não considerar os dois números).
def interos(n1,n2):
  if n1 > n2:
    for i in range(n2+1,n1):
      print(n2+1)
      n2 = n2 + 1
  elif n2 > n1:
    for i in range(n1+1,n2):
      print(n1+1)
      n1 = n1 + 1
interos(7,5)