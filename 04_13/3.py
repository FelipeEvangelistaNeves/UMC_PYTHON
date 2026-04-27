for i in range(30):
  nota1 = float(input("Digite a primeira nota do aluno: "))
  nota2 = float(input("Digite a segunda nota do aluno: "))
  media = (nota1 + nota2) / 2
  if media >= 5:
    print("Aluno aprovado com média:", media)
  elif media >= 3:
    print("Exame")
    exame = float(input("Digite a nota do exame: "))
    media_final = (media + exame) / 2
    if media_final >= 5:
      print("Aluno aprovado no exame com média final:", media_final)
    else:
      print("Aluno reprovado no exame com média final:", media_final)
  else:
    print("Aluno reprovado com média:", media)