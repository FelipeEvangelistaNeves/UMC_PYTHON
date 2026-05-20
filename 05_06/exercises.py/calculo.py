import math

# Criar um programa que contenha as seguintes funções: 
# 1) Elaborar uma função (com retorno) que recebe como parâmetro um número inteiro e devolve o seu 
# dobro. 
def dobro(num):
    '''
    Função que recebe um número inteiro e retorna o seu dobro.'''
    return num * 2


#-----------------------------------------------------------------------------------------------------#

# 2) Elaborar uma função (com retorno) que verifica se um número é positivo ou negativo. Sendo que o valor 
# de retorno será 1 se positivo, -1 se negativo e 0 se for igual a 0. 
def positvnega(num):
    '''
    Função que verifica se um número é positivo ou negativo.
    Retorna 1 se positivo, -1 se negativo e 0 se for igual a 0.
    '''
    if num == 0:
        return 0
    elif num > 0:
        return 1
    else:
        return -1
    
#-----------------------------------------------------------------------------------------------------#


# 3) Elaborar um programa em que o usuário deve inserir três números inteiros (a, b, c). 
# Logo após, esses valores são passados como parâmetros para uma função (sem retorno) que calcula a fórmula de 
# Bhaskara e exibe o resultado. 

def calculodebaska(a, b, c):
  '''
  Função que calcula a fórmula de Bhaskara e exibe o resultado.'''
  delta = b**2 - 4*a*c
  if delta < 0:
    print("Não existem raízes reais.")
  else:
    x1 = (-b+(math.sqrt(delta)))/(2*a)
    x2 = (-b-(math.sqrt(delta)))/(2*a)
    print(f"X1: {x1} e X2: {x2}")
  
#-----------------------------------------------------------------------------------------------------#

# 4) Elaborar uma função (sem retorno) que ao receber um número deve converte em Fahrenheit e exibe o 
# resultado na tela. A fórmula de conversão é: F = (9*C+160) / 5. 

def celsius_p_fahrenheit(num):
   '''Função que recebe um número em Celsius e converte para Fahrenheit.'''
   num = (9*num+160) / 5
   print(f"{num}°F")
  
#-----------------------------------------------------------------------------------------------------#

# 5) Elaborar uma função (com retorno) que ao receber um número deve converte em Kelvin e exibe o 
# resultado na tela. A fórmula de conversão é: K=C+273.15. 

def celsius_p_kelvin(num):
   '''Função que recebe um número em Celsius e converte para Kelvin.'''
   num = num + 273.15
   print(f"{num} K")



#-----------------------------------------------------------------------------------------------------


# 6) Elaborar uma função (sem retorno) que recebe dois valores inteiros passados como parâmetro. 
# Logo em seguida a função deve exibir um menu com 4 opções 
# (cada opção levará para uma função com retorno diferente): 
# a) Soma 
# b) Subtrair 
# c) Multiplicar 
# d) Dividir 
# e) Raiz quadrada do primeiro número. 
# Quando o usuário selecionar a operação desejada, a função correspondente deve exibir o resultado na tela. 

def operacoes(num1, num2, opcao):
    '''Função que recebe dois valores inteiros e uma opção de operação, e exibe o resultado da operação escolhida.'''
    if opcao == 'a':
        print(f"Soma: {num1 + num2}")
    elif opcao == 'b':
        print(f"Subtração: {num1 - num2}")
    elif opcao == 'c':
        print(f"Multiplicação: {num1 * num2}")
    elif opcao == 'd':
        print(f"Divisão: {num1 / num2}")
    elif opcao == 'e':
        print(f"Raiz quadrada de {num1}: {math.sqrt(num1)}")
    else:
        print("Opção inválida")

    
   

#-----------------------------------------------------------------------------------------------------#



# 7) Elaborar uma função (com retorno) que determina se um número passado como parâmetro é primo. A 
# função quando chamada retorna 1 indicando que o número é primo e O caso contrário. 

def primo(num):
  '''Função que determina se um número é primo. Retorna 1 se for primo e 0 caso contrário.'''
  if num < 2:
     return 0
  for i in range(2, num):
     if num % i == 0:
        return 0
  return 1


#-----------------------------------------------------------------------------------------------------#


# 8) Elaborar uma função (sem retorno) que imprime todos os números primos de 2 a N 
# (essa função deve utilizar a função do exercício 7).
#  Sendo que N é um número inserido pelo usuário, que deve ser superior a 2 
# (solicitar um novo número caso o usuário digite um número menor ou igual a 2). 

def primos_ate_n(n):
  '''Função que imprime todos os números primos de 2 a N.'''
  if n <= 2:
    print("Digite um número maior que 2.")
    return
  for i in range(2, n + 1):
    if primo(i) == 1:
      print(i)
    
#-----------------------------------------------------------------------------------------------------




