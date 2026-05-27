# 2) Crie uma biblioteca chamada geometria.py contendo funções para realizar os seguintes cálculos 
# geométricos:
# a) Uma função que calcule e retorne a área de um quadrado. Onde: A (área) e l (lado do quadrado)
# b) Uma função que calcule e retorne a área de um retângulo. Onde: A (área), b (base) e h (altura)
# c) Uma função que calcule e exiba a área de um círculo. Onde: A (área), r (raio do círculo) e π (constante pi)
# d) Uma função que calcule e retorne o perímetro (circunferência) de um círculo. Onde: C (comprimento da 
# circunferência), r (raio do círculo) e π (constante Pi). 
# e) Uma função que calcule e exiba o volume de um cilindro. Onde: V (volume), r (raio da base) e h (altura).
#
import geometria
lado = int(input("digite o lado do quadrado"))
print("Área do quadrado:", geometria.area_quadrado(lado))
#------------------------------------------------------------------------------------------------------#
lado_base = int(input("digite a base do retângulo"))
altura = int(input("digite a altura do retângulo"))
print("Área do retângulo:", geometria.area_retangulo(lado_base, altura))
#------------------------------------------------------------------------------------------------------#
raio = int(input("digite o raio do círculo"))
print("Área do círculo:", geometria.area_circulo(raio))
print("Perímetro do círculo:", geometria.perimetro_circulo(raio))
#------------------------------------------------------------------------------------------------------#
altura_cilindro = int(input("digite a altura do cilindro"))
print("Volume do cilindro:", geometria.volume_cilindro(raio, altura_cilindro))
