idade = int(input("qual sua idade? "))
if idade <= 5:
    print("idade invalida")
elif idade < 11:
    print("infantil")
elif idade < 16:
    print("juvenil")
elif idade < 21:
    print("junior")
elif idade < 26:
    print("profissional")
else:
    print("invalido")
