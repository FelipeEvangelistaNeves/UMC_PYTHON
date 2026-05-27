# 5) Elaborar um programa para inverter o dicionário, trocando suas chaves e 
# valores, de forma que cada valor original se torne uma chave e cada chave 
# original se torne o valor correspondente. Exibir o novo dicionário.

from dados import dados
novodict={}
print(dados.items())
for chave, valor in dados.items():
    novodict[valor]=chave
print(novodict)