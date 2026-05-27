
import xerusbago
# Exercício 11: Escreva um programa que solicite ao usuário que digite um texto e, em seguida, 
# imprima as quatro primeiras letras desse texto. 
# Se o texto tiver menos de quatro letras, imprima o texto completo.
texto = str(input("digite um texto: "))
xerusbago.quatro_letras(texto)
input("aperte enter para continuar...")
# 2) Elaborar um programa que leia um nome e imprima o nome somente se a primeira letra do nome for “a” ou
# “e” (maiúscula ou minúscula).
xerusbago.letra_a_e(texto)
input("\n aperte enter para continuar...")
# 3) Elaborar um programa que receba uma palavra ou texto e a imprima de trás-para-frente.
xerusbago.texto_ao_contrario(texto)
input("\n aperte enter para continuar...")
# 4) Elaborar um programa que receba uma string e imprima a string sem suas vogais.
xerusbago.str_semvogal(texto)
input("\n aperte enter para continuar...")
# 5) Elaborar um programa que receba uma palavra e calcule quantas vogais (a, e, i, o, u) possui essa palavra. Depois
# o usuário deve digitar um caractere (vogal ou consoante) e o programa deve substituir todas as vogais da palavra dada por esse caractere.
caractere = str(input("\n digite um caractere para substituir as vogais: "))
xerusbago.vogal_substituida(texto, caractere)
input("\n aperte enter para continuar...")
# 6) Elaborar um programa em que troque todas as ocorrências de uma letra
# L1 pela letra L2 em uma string. A string e as letras L1 e L2 devem ser fornecidas pelo usuário.

#7) Elaborar um programa que o usuário deve preencher uma lista com os modelos de cinco carros. O usuário
# também deve preencher outra lista com o consumo desses carros, isto é, quantos quilômetros cada um deles
# faz com um litro de combustível. Calcule e mostre:  
carros = []
for x in range(1,6):
  carro= str(input(f"digite um nome do {x}º carro"))
  carros.append(carro)
consumo = []
for x in range(1,6):
  kml = int(input(f"digite quantos kml o {x}º carro faz"))
  consumo.append(kml)
xerusbago.gasolina(carros,consumo,1000)