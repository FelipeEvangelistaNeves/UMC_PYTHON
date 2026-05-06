
# 1) Elaborar uma função que receba três notas de um aluno como parâmetros e uma letra. Se a letra for A,
# a função deverá calcular a média aritmética das notas do aluno; se for P, devera calcular a média
# ponderada, com pesos 5, 3 e 2.

def media(n1, n2, n3, letra):
  letra = letra.upper()
  if letra=="A":
    
    print((n1+n2+n3)/3)
  elif letra=="P":
    print((5*n1)+(3*n2)+(2*n3))
  else:
    print("Letra inválida")
n1 = float(input("Digite a primeira nota do aluno: "))
n2 = float(input("Digite a segunda nota do aluno: "))
n3 = float(input("Digite a terceira nota do aluno: "))
letra = input("Digite a letra para o tipo de média (A para aritmética, P para ponderada): ")

media(n1, n2, n3, letra)