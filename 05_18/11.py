# 11) Crie uma função que receba um dicionário e retorne a quantidade de pares 
# chave-valor presentes nele.

from dados import dados
def conta_elemento(dados:dict):
  return len(dados)
print(conta_elemento(dados))