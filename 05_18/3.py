# 3) Elaborar um programa para verificar se todos os valores em um dicionário 
# são distintos (ou seja, se não há duas chaves com o mesmo valor). 
# Exibir mensagem caso exista algum valor repetido ou não.
from dados import dados

valores = list(dados.values())

for k in valores:
  if valores.count(k)>1:
    print("valores repetidos")
    print(k)
  else:
    print("valores distintos")