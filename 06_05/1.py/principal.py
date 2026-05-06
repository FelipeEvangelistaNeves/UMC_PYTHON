import calculo
exerc = int(input("Digite o número do exercício que deseja testar: "))
if exerc == 1:
    num = int(input("Digite um número para calcular o dobro: "))
    print(calculo.dobro(num))
elif exerc == 2:
    num = int(input("Digite um número para verificar se é positivo ou negativo: "))
    print(calculo.positvnega(num))
elif exerc == 3:
    a = int(input("Digite o valor de a: "))
    b = int(input("Digite o valor de b: "))
    c = int(input("Digite o valor de c: "))
    calculo.calculodebaska(a, b, c)
elif exerc == 4:
    temp = int(input("Digite a temperatura em Celsius para converter para Fahrenheit: "))
    calculo.celsius_p_fahrenheit(temp)
elif exerc == 5:
    temp = int(input("Digite a temperatura em Celsius para converter para Kelvin: "))
    calculo.celsius_p_kelvin(temp)
elif exerc == 6:
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    print("Selecione a operação desejada:")
    print("a) Soma")
    print("b) Subtrair")
    print("c) Multiplicar")
    print("d) Dividir")
    print("e) Raiz quadrada do primeiro número.")
    opcao = input("Digite a letra correspondente à operação: ").lower()
    calculo.operacoes(num1, num2, opcao)
elif exerc == 7:
    num = int(input("Digite um número para verificar se é primo: "))
    print(calculo.primo(num))
elif exerc == 8:
    number = int(input("digite um  valor para descobrir os primos até ele: "))
    calculo.primos_ate_n(number)