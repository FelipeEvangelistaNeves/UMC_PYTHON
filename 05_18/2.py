# 2) Elaborar um programa para exibir todos os pares chave-valor no seguinte 
# formato "chave=valor".

dados ={
    "nome": "João",
    "idade": 30,
    "cidade": "São Paulo"
}
for chave, valor in dados.items():
    print(f"{chave}={valor}")
