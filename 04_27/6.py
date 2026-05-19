# 6) Elaborar um programa que dada uma lista com pontuações de jogadores, crie um programa que remova
# valores duplicados, ordene as pontuações em ordem decrescente, classifique os três primeiros colocados
# como “elite”, classifique os demais como “amadores”. Exiba o resultado.
pontuacoes = []
qnt_jogadores = int(input("quantos jogadores tem? "))
for i in range(qnt_jogadores):
  pontuacao = int(input("digite a pontuação do jogador: "))
  pontuacoes.append(pontuacao)
pontuacoes = list(set(pontuacoes))
pontuacoes.sort(reverse=True)
elite = pontuacoes[:3]
amadores = pontuacoes[3:]
print("elite: ", elite)
print("amadores: ", amadores)