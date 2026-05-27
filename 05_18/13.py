# 13) Elaborar um programa para mesclar dois dicionários de forma que, quando 
# ambos compartilharem a mesma chave, seus valores sejam somados em vez de um 
# sobrescrever o outro.

dic1 = {'a': 5, 'b': 10}
dic2 = {'b': 15, 'c': 20}
dic3 = dic1.copy()
for chave, valor in dic2.items():
    if chave in dic3:
        dic3[chave] += valor
    else:
        dic3[chave] = valor
print(dic3)