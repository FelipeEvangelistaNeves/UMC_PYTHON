#  5) Elaborar um programa que contenha a seguinte sequência: 
# (a) Ler uma string S1 (tamanho máximo de 20 caracteres,se passar solicitar outra) 
# (b) Imprimir o tamanho da string S1 
# (c) Comparar a string S1 com uma nova string S2 (tamanho máximo de 20 caracteres, se passar solicitar outra) fornecida pelo usuário e imprimir o resultado da comparação 
# (se é igual ou não e qual tem maior quantidade de caracteres)
# (d) Concatenar a string S1 com uma nova string S2 e imprimir na tela o resultado da concatenação; 
# (e) Imprimir a string S1 de forma reversa 
# (f) Contar quantas vezes um caractere específico aparece na string S1. Esse caractere desse ser solicitado para o usuário. 
# (g) Substituir a primeira ocorrência do caractere C1 da string S1 pelo caractere C2. 
# Os caracteres C1 e C2 serão inseridos pela usuário.
#(h) Verificar se uma string S2 é substring (trecho) de S1. A string S2 deve ser informada pelo usuário.
#(i) Retornar uma substring (trecho) da string S1. Para isso o usuário deve informar a partir de qual posição deve ser criada a 
# substring (trecho) e qual é o tamanho da substring (trecho).
# 
s1 = input("Digite a string S1 (máximo 20 caracteres): ")
while len(s1) > 20:
   print("string longa, digite novamente")
   s1 = input("Digite a string S1 (máximo 20 caracteres): ")
print(len(s1))
s2 = input("Digite a string S2 (máximo 20 caracteres): ")
while len(s2) > 20:
   print("string longa, digite novamente")
   s2 = input("Digite a string S2 (máximo 20 caracteres): ")
if len(s2)>len(s1):
   print("a maior string é a S2")
elif len(s1)>len(s2):
   print("a maior string é a S1")
else:
   print("as strings têm o mesmo tamanho")
print("concatenação:", s1 , s2)
string_reversa = s1[::-1]
print("string reversa:", string_reversa)
aparece_qt = input("digite uma letra para contar na string s1")
qtd_let = 0
for i in range(len(s1)):
   if s1[i] == aparece_qt:
      qtd_let += 1
print(f"a letra {aparece_qt} aparece {qtd_let} vezes na string s1")
c1 = input("digite o caractere C1 para substituir na string s1")
c2 = input("digite o caractere C2 para substituir na string s1")
texto_substituido = ""
for t in range(len(s1)):
  if s1[t] == c1:
    texto_substituido += c2
  else:
    texto_substituido += s1[t]
print(f"string s1 com o caractere C1 substituído pelo caractere C2: {texto_substituido}")
if s2 in s1:
   print("a string s2 é substring da string s1")
sub_s1 = int(input("digite a posição inicial para criar a substring da string s1"))
tamanho_sub = int(input("digite o tamanho da substring da string s1"))
texto_extraido = ""
for i in range(tamanho_sub):
    texto_extraido += s1[sub_s1 + i]
print(f"substring da string s1: {texto_extraido}")
