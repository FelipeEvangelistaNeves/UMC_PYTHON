# 7) Elaborar um programa em que o usuário deva inserir várias temperaturas. Todas as temperaturas
# precisam ser armazenadas em uma lista. Caso o usuário insira um número menor que zero (0) o programa
# finaliza a inserção de números. Logo em seguida, o programa deve acessar a lista gerada e classificar cada
# temperatura inserida. Classifique cada temperatura como: “Frio” (<10°C), “Agradável” (entre 10°C e 30°C),
# “Quente” (>30°C). O programa deve ignorar valores fora de valor plausível (acima de 60°C). Exiba a
# quantidade de ocorrências em cada categoria.
temp = []
clas = []
valortemperatura = int(input("digite uma temperatura"))
if valortemperatura <0:
  print("Temperatura classificada como frio")
temp.append(valortemperatura)
while valortemperatura >=0:
  valortemperatura = int(input("digite uma temperatura"))
  temp.append(valortemperatura)
