# 5)Elaborar um programa que considere duas listas: uma com nomes de usuários e outra com suas
# respectivas senhas. Desenvolva um programa que solicite ao usuário login e senha. O programa deve
# permitir no máximo 3 tentativas. Informe se o acesso foi concedido ou se a conta foi bloqueada após as
# tentativas.

usuarios = ["alice", "bob", "charlie"]
senhas = ["123456", "abcdef", "xyz123"]
login = input("Digite seu login: ")
senha = input("Digite sua senha: ")
tentativas = 0
while tentativas < 3:
  if login in usuarios:
    index = usuarios.index(login)
    if senha == senhas[index]:
      print("Acesso concedido")
      break
    else:
      print("Senha incorreta")  
      senha = input("Digite sua senha: ")
  else:
    print("Login não encontrado")
    login = input("Digite seu login: ")
    senha = input("Digite sua senha: ")
  tentativas += 1
else:
  print("Conta bloqueada após 3 tentativas")
