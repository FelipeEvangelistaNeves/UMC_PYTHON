# 4) Elaborar um programa que contém uma matriz 4x5.
#  O usuário deve preencher essa matriz com números reais. 
# Após isso, o programa deve calcular a média de cada linha e exibir qual linha possui a maior média.
matriz = []
for i in range(4):
  linha=[]
  for j in range(5):
    linha.append(int(input(f"digite um valor[{i}][{j}]:")))
  matriz.append(linha)
medias = []
for i in range(4):
  media = sum(matriz[i]) / len(matriz[i])
  medias.append(media)
print("Médias das linhas:", medias)
print("Linha com maior média:", medias.index(max(medias)) + 1)

