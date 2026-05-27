# 2) Elaborar um programa para exibir todos os pares chave-valor no seguinte 
# formato "chave=valor".

from dados import dados
for chave, valor in dados.items():
    print(f"{chave}={valor}")
