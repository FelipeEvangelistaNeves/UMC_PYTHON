# 3) Elaborar uma função fatorial que quando chamada retorna o fatorial de um número, sendo que esse número
# é passado como parâmetro para a função. Sabendo que o fatorial de um número é a multiplicação desse
# número por todos os seus antecessores maiores que zero.
def fatorial(n):
  resultado = 1
  for i in range(1, n + 1):
    resultado = resultado*i
  return resultado
n = int(input("Digite um número para calcular o fatorial: "))
print(f"O fatorial de {n} é: {fatorial(n)}")
