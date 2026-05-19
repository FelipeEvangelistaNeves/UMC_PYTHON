matriz = []
for i in range(3):
  linha=[]
  for j in range(5):
    linha.append(int(input(f"digite um valor[{i}][{j}]:")))
  matriz.append(linha)
for linha in range(3):
  for coluna in range(5):
    if matriz[linha][coluna]%2==0:
      print(f"posicao {linha} {coluna} = {matriz[linha][coluna]}")