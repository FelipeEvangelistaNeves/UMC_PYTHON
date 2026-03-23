Nome = input("qual o nome do hospede? ")
Tipo = input("qual o tipo do quarto? (simples, duplo ou triplo) ")
dias = int(input("quantos dias de hospedagem? "))
consumo = float(input("qual o valor do consumo? "))
if Tipo == "simples":
    valor = 100
elif Tipo == "duplo":
    valor = 150
elif Tipo == "triplo":
    valor = 200
else:
    print("tipo de quarto invalido")
    valor = 0
total = (valor * dias + consumo) * 1.1
print("O valor total da hospedagem para", Nome, "é: R$", total)

