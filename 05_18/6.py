# 6) Elaborar um programa que solicite ao usuário para digitar uma chave e 
# verifique se essa chave existe no dicionário. Se a chave existir, exiba o 
# valor correspondente; caso contrário, mostre uma mensagem informando que a 
# chave não foi encontrada.

from dados import dados
chave = input("digite o valor de uma chave: ")
print(dados.get(chave, "chave não encontrada"))