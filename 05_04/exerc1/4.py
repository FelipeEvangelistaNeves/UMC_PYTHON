# 4) Elaborar uma função (com retorno) que quando chamada calcula xn através de multiplicações. Tanto x
# (float) como n (int) são parâmetros da função. Não utilizar nenhuma função pronta de biblioteca.
def potencia(x, n):
  resultado =1
  for i in range(1, n+1):
    resultado = resultado * x
  return resultado
val1 = float(input("Digite a base: "))
val2 = int(input("Digite o expoente: "))
print(potencia(val1, val2))