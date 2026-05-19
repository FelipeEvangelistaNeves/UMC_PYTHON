n1=float(input("digite um numero: "))
n2=float(input("digite outro numero: "))
calc = input("qual operação deseja realizar? +, -, *, / ")
if(calc == "+"):
  print(n1+n2)
elif(calc == "-"):
    print(n1-n2)
elif(calc == "*"):
    print(n1*n2)
elif(calc == "/"):
    if(n2 == 0):
        print("impossivel dividir por zero")
    else:
        print(n1/n2)
else:
    print("operacao invalida")
      