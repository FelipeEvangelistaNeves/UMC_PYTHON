# 1) Elaborar um programa que leia um nome e imprima as 4 primeiras letras do nome.
def quatro_letras(texto):
  if len(texto) < 4:
    print (texto)
  else:
    for t in range(4):
      print (texto[t])

#-----------------------------------------------------------------------------------------------------#


# 2) Elaborar um programa que leia um nome e imprima o nome somente se a primeira letra do nome for “a” ou
# “e” (maiúscula ou minúscula).
def letra_a_e(texto):
  texto = texto.lower()
  if texto[0] == "a" or texto[0] == "e":
    print (texto, end="")
  else:
    print ("a primeira letra do nome não é a ou e")

#-----------------------------------------------------------------------------------------------------#


# 3) Elaborar um programa que receba uma palavra ou texto e a imprima de trás-para-frente.

def texto_ao_contrario(texto):
  texto_contrario = ""
  for t in range(len(texto)-1, -1, -1):
    texto_contrario += texto[t]
  print (texto_contrario)
#-----------------------------------------------------------------------------------------------------#

# 4) Elaborar um programa que receba do usuário uma string. O programa deve imprimir a string sem suas vogais.

def str_semvogal(texto):
  texto = texto.lower()
  for t in range(len(texto)):
    if texto[t] != "a" and texto[t] != "e" and texto[t] != "i" and texto[t] != "o" and texto[t] != "u":
      print (texto[t], end="")
#-----------------------------------------------------------------------------------------------------#

# 5) Elaborar um programa que receba uma palavra e calcule quantas vogais (a, e, i, o, u) possui essa palavra. Depois
# o usuário deve digitar um caractere (vogal ou consoante) e o programa deve substituir todas as vogais da
# palavra dada por esse caractere.
def vogal_substituida(texto, caractere):
    qnt_vog=0
    texto=texto.lower()
    for t in range(len(texto)):
      if texto[t]=="a":
        qnt_vog = qnt_vog + 1
      if texto[t]=="e":
        qnt_vog = qnt_vog + 1
      if texto[t]=="i":
        qnt_vog = qnt_vog + 1
      if texto[t]=="o":
        qnt_vog = qnt_vog + 1
      if texto[t]=="u":
        qnt_vog = qnt_vog + 1
    
    caractere = caractere.lower()
    texto_substituido = ""
    for t in range(len(texto)):
      if texto[t] == "a":
        texto_substituido += caractere
      else:
        texto_substituido += texto[t]

#-----------------------------------------------------------------------------------------------------#

# 6) Elaborar um programa em que troque todas as ocorrências de uma letra L1 pela letra L2 em uma string. A
# string e as letras L1 e L2 devem ser fornecidas pelo usuário.


#-----------------------------------------------------------------------------------------------------#

# 7) Elaborar um programa que o usuário deve preencher uma lista com os modelos de cinco carros. O usuário
# também deve preencher outra lista com o consumo desses carros, isto é, quantos quilômetros cada um deles
# faz com um litro de combustível. Calcule e mostre:
# (a) O modelo de carro mais econômico;
# (b) Quantos litros de combustível cada um dos carros cadastrados consome para percorrer uma distância
# de 1.000 quilômetros.

def gasolina(carros,consumo,distancia):
  consumo_1000 = []
  for c in range(len(consumo)):
    consumo_1000.append(distancia/consumo[c])
  print (f"O modelo de carro mais econômico é o {carros[consumo.index(max(consumo))]}")
  for c in range(len(consumo)):
    print (f"O {carros[c]} consome {consumo_1000[c]} litros para percorrer {distancia} km")
#-----------------------------------------------------------------------------------------------------#

# 8) Elaborar um programa que recebe do usuário uma string S, um caractere C, e uma posição X e devolve o índice
# da primeira posição da string onde foi encontrado o caractere C.A procura deve começar a partir da posição X.
