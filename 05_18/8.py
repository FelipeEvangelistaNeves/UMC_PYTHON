# 8) Elaborar um programa que permite o usuário informar uma chave a ser removida. 
# Remova do dicionário o par referente a essa chave, caso ela exista. Se a chave 
# informada não estiver no dicionário, exiba uma mensagem de aviso. Mostre o 
# dicionário atualizado após a operação.

from dados import dados
chave_remover = input("Digite a chave que deseja remover: ")
if chave_remover in dados:
  dados.pop(chave_remover)
print(dados)