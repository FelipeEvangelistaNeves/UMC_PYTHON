# 4. Elaborar um programa que o
#  usuário deve digitar 7 nomes de alunos 
# (esses nomes devem ser armazenados em uma lista) e 
# ao final o programa deve mostrar: todos os nomes, o primeiro nome digitado,
#  o último nome digitado e quantos nomes possuem mais de 5 letras.
nomes_alunos = []
for i in range(1, 8):
    nome = input(f"Digite o {i}º nome do aluno: ")
    nomes_alunos.append(nome)
print(f"Nomes digitados: {nomes_alunos}")
primeiro_nome = nomes_alunos[0]
ultimo_nome = nomes_alunos[6]
nome_5letras = 0
for i in range(len(nomes_alunos)):
    if len(nomes_alunos[i]) > 5:
        nome_5letras += 1
print(f"Primeiro nome digitado: {primeiro_nome}")
print(f"Último nome digitado: {ultimo_nome}")
print(f"Quantidade de nomes com mais de 5 letras: {nome_5letras}")
