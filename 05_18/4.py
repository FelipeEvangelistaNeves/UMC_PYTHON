# 4) Elaborar um programa para renomear uma chave existente do dicionário, 
# preservando seu valor associado e mantendo o restante do dicionário inalterado. 
# Exibir o novo dicionário.

dados ={
    "nome": "João",
    "idade": 30,
    "cidade": "São Paulo"
}
nova_chave = input("Digite a nova chave para renomear 'nome': ")
dados[nova_chave]=dados.pop