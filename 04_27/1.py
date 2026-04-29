array = []
for i in range(16):
  a = i+1
  valor = int(input(f"qual seu {a}º valor: "))
  # input("aperte enter para continuar")
  array.append(valor)

valor1 = int(input("digite a primeira posição: "))


while(valor1<1 or valor1>16 ):
  valor1 = int(input("digite a primeira posição: "))
valor2 = int(input("digite a segunda posição: "))
while(valor2<1 or valor2>16 ):
  valor2 = int(input("digite a segunda posição: "))
print(f"a soma dos valores das posições {valor1} e {valor2}")
valor1=valor1-1
valor2=valor2-1
soma = array[valor1] + array[valor2]
print(f" é: {soma}")