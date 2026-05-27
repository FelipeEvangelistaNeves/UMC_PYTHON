# 1) Crie uma biblioteca chamada financeiro.py contendo funções para realizar os seguintes cálculos 
# financeiros.
#   a) Uma função que calcule e retorna o montante final utilizando juros simples. Onde: M (montante final), C 
# (capital inicial), i (taxa de juros) e t (tempo).
#   b) Uma função que calcule e exiba o montante final utilizando juros compostos. Onde: M (montante final), C 
# (capital inicial), i (taxa de juros) e t (tempo).
#   c) Uma função que calcule e retorna o valor final de um produto após aplicar um desconto percentual. Onde:
# Vf (valor final), Vi (valor inicial) e d (percentual de desconto). 
#   d) Uma função que calcule e exiba o valor final após aplicar um aumento percentual. Onde: Vf (valor final), 
# Vi (valor inicial) e a (percentual de aumento). 
#   e) Uma função que calcule e retorne o valor de cada parcela de um financiamento simples. Onde: P (valor 
# da parcela), V (valor total financiado) e n (número de parcelas. 

import financeiro
capital = int(input("digite o capital inicial"))
taxa = int(input("digite a taxa de juros"))
tempo = int(input("digite o tempo"))
print("Montante com juros simples:", financeiro.juros_simples(taxa, capital, tempo))
print("Montante com juros compostos:", financeiro.juros_compostos(taxa, capital, tempo))

#------------------------------------------------------------------------------------------------------#
valor_inicial = int(input("digite o valor inicial do produto"))
desconto = int(input("digite o percentual de desconto"))
print("Valor final com desconto:", financeiro.desconto(valor_inicial, desconto))

#------------------------------------------------------------------------------------------------------#
aumento = int(input("digite o percentual de aumento"))
print("Valor final com aumento:", financeiro.aumento(valor_inicial, aumento))

#------------------------------------------------------------------------------------------------------#
valor_total = int(input("digite o valor total financiado"))
numero_parcelas = int(input("digite o número de parcelas"))
print("Valor de cada parcela:", financeiro.parcela(valor_total, numero_parcelas))
