idade = int(input("qual sua idade? "))
if idade >= 18:
    print("você é adulto")
elif idade >=14:
    print("juvenil B")
elif idade >=11:
    print("juvenil A")
elif idade >=8:
    print("infantil B")
elif idade <=5:
    print("infantil A")
else:
    print("idade invalida")