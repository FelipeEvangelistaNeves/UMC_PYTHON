distancia = float(input("Digite a distância percorrida (em km): "))
litros = float(input("Digite a quantidade de litros consumidos: "))
consumo = distancia / litros
if consumo < 8:
    print("Venda o carro!")
elif consumo >= 8 and consumo <= 14:
    print("Econômico!")
else:
    print("Super econômico!")
