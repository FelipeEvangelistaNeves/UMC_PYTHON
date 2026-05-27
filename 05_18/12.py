# 12) Elaborar um programa que tenha que ler do usuário 5 pares de informações 
# (nome e idade). Crie um dicionário esses dados fornecidos e, ao final, 
# imprima o dicionário.

dic ={}
for k in range(5):
  nome = input("digite o nome: ")
  idade = input("digite a idade: ")
  dic[k] = {nome,idade}
print(dic)