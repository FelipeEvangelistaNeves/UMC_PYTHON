#Tupla é uma sequência de elementos ordenados dentro de um parenteses

a = (18,"abril",9.5)
x,y =(12,17)
print(x)
print(y)

#dict associam chave-valor.................... objeto com outro nome?
#chaves unicas imutaveis ..................... objeto com outro nome?
dict()


aaa = {
  "nome": "kleber",
  "nome2": "felipe"
}
nome = int(input("qual nome 1 ou 2"))

if nome == 1 or nome == 2:
  if nome == 1:
    print(aaa["nome"])
  else:
    print(aaa["nome2"])
else:
  print("valor invalido")

aaa.items()
#items serve para acessar os itens do dicionário, ou seja, as chaves e os valores. 
# Ele retorna uma lista de tuplas, onde cada tupla contém uma chave e seu valor correspondente. 
# Por exemplo, se tivermos um dicionário chamado "meu_dicionário" 
# com os seguintes pares chave-valor: {"chave1": "valor1", "chave2": "valor2"}, 
# ao usar o método items() em "meu_dicionário", 
# obteremos a seguinte saída: dict_items([('chave1', 'valor1'), ('chave2', 'valor2')]).
aaa.pop()
# O método pop() é usado para remover um item específico de um dicionário,
# com base na chave fornecida. Ele retorna o valor associado à chave removida.
# Por exemplo, se tivermos um dicionário chamado "meu_dicionário"
# com os seguintes pares chave-valor: {"chave1": "valor1", "chave2": "valor2"},
# ao usar o método pop("chave1") em "meu_dicionário",
# o item com a chave "chave1" será removido do dicionário e o valor "valor1" será retornado.
aaa.update()
# O método update() é usado para atualizar um dicionário com os pares chave-valor de outro dicionário ou de um 
# iterável de pares chave-valor.
# Ele adiciona os pares chave-valor do dicionário fornecido ao dicionário original, 
# substituindo os valores existentes para as chaves que já estão presentes.
# Por exemplo, se tivermos um dicionário chamado "meu_dicionário"
aaa.values()
# O método values() é usado para obter uma visão dos valores presentes em um dicionário.
# Ele retorna uma visão dos valores do dicionário, que pode ser convertida em uma lista ou iterada diretamente.
# Por exemplo, se tivermos um dicionário chamado "meu_dicionário"
# com os seguintes pares chave-valor: {"chave1": "valor1", "chave2": "valor2"},
# ao usar o método values() em "meu_dicionário", obteremos a seguinte saída: dict_values(['valor1', 'valor2']).
aaa.clear()
# O método clear() é usado para remover todos os itens de um dicionário, deixando-o vazio.
# Por exemplo, se tivermos um dicionário chamado "meu_dicionário"
# com os seguintes pares chave-valor: {"chave1": "valor1", "chave2": "valor2"},
# ao usar o método clear() em "meu_dicionário", o dicionário será esvaziado e a seguinte saída será obtida: {}.

aaa.keys()
# O método keys() é usado para obter uma visão das chaves presentes em um dicionário.
# Ele retorna uma visão das chaves do dicionário, que pode ser convertida em
# uma lista ou iterada diretamente.
# Por exemplo, se tivermos um dicionário chamado "meu_dicionário"
# com os seguintes pares chave-valor: {"chave1": "valor1", "
# chave2": "valor2"},
# ao usar o método keys() em "meu_dicionário", obteremos a seguinte saída: dict_keys(['chave1', 'chave2']).
aaa.copy()
# O método copy() é usado para criar uma cópia rasa de um dicionário.
# Ele retorna um novo dicionário que contém os mesmos pares chave-valor do dicionário original.
# Por exemplo, se tivermos um dicionário chamado "meu_dicionário"
# com os seguintes pares chave-valor: {"chave1": "valor1", "chave2": "valor2"},
# ao usar o método copy() em "meu_dicionário",
# obteremos um novo dicionário com os mesmos pares chave-valor: {"chave1": "valor1", "chave2": "valor2"}.

aaa.get()
# O método get() é usado para acessar o valor associado a uma chave específica em um dicionário.
# Ele retorna o valor correspondente à chave fornecida, ou um valor padrão se a chave não estiver presente no dicionário.
# Por exemplo, se tivermos um dicionário chamado "meu_dicionário"
# com os seguintes pares chave-valor: {"chave1": "valor1", "chave2": "valor2"},
# ao usar o método get("chave1") em "meu_dicionário",
# obteremos o valor "valor1".
