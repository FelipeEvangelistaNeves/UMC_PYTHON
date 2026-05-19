idade = int(input("Digite a idade: "))
tempotrabalho = int(input("Digite o tempo de trabalho: "))
if(idade >= 65 or tempotrabalho >= 30 or (idade >= 60 and tempotrabalho >= 25)):
    print("Pode se aposentar")
else:
    print("Ainda não pode se aposentar")
