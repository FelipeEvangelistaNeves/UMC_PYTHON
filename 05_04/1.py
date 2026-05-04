matriz = []
for i in range(4):
  linha=[]
  for j in range(4):
    linha.append(int(input(f"digite um valor[{i}][{j}]:")))
  matriz.append(linha)
for i in range(4):
  for j in range(4):
    print(matriz[i][j])
