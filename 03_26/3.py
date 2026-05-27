altura = float(input("Digite a altura (em metros): "))
peso = float(input("Digite o peso (em kg): "))
if altura <= 0 or peso <= 0:
    print("Erro: Altura e peso devem ser maiores que zero.")
elif altura < 1.20:
    if peso <= 60:
        print("A")
    elif  peso<60 and peso <= 90:
        print("D")
    else:
        print("G")
elif altura <= 1.70:
    if peso <= 60:
        print("B")
    elif peso <= 90:
        print("E")
    else:
        print("H")
else:
    if peso <= 60:
        print("C")
    elif peso <= 90:
        print("F")
    else:
        print("I")