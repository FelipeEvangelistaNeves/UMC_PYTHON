# 2) Elaborar um programa em que o usuário deva preencher uma lista com 30 números. Após o
# preenchimento o programa deve calcular a média dos números inseridos. Logo em seguida, o programa
# deve salvar em outra lista somente os números que são maiores que a média. Exibir no final a lista dos
# números maiores que a média.
lista = []
maioresmedia=[]
for x in range(3):
    valor = int(input("Digite um número inteiro: "))
    lista.append(valor)

media = sum(lista) / len(lista)
for valor in lista:
    if valor > media:
        maioresmedia.append(valor)

print("Lista dos números maiores que a média:", maioresmedia)