# 4) Elaborar um programa para renomear uma chave existente do dicionário, 
# preservando seu valor associado e mantendo o restante do dicionário inalterado. 
# Exibir o novo dicionário.

from dados import dados
qual_chave = input("Digite qual chave deseja renomear")
nova_chave=input("qual nome voce deseja dar a nova chave")
dados[nova_chave]=dados.pop(qual_chave)
print(dados[nova_chave])
print(dados)