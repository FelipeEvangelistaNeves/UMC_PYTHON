# 7) Elaborar um programa que leia uma nova chave e um valor do usuário e os 
# adicione ao dicionário. Caso a chave já exista, atualize o valor existente 
# para o novo valor fornecido. No final, exiba o dicionário resultante.
from dados import dados
nova_chave=input("digite o valor da nova chave")
dados[nova_chave]="coco"
print(dados)