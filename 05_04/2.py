matriz = []
soma = 0
media = 0
for i in range(3):
  linha=[]
  for j in range(3):
    valor=(int(input(f"digite um valor[{i}][{j}]:")))
    linha.append(valor)
    soma = soma+valor
    media = media+1
  matriz.append(linha)
print(soma/media)
for i in range(3):
  for j in range(3):
    if matriz[i][j]>soma/media:
      print(matriz[i][j])