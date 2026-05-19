qnt_estoque = []
produtos = []
qnt_produtos = int(input("quantos produtos tem na loja? "))
for i in range(qnt_produtos):
  nome = input("digite o nome do produto: ")
  valor = int(input(f"quantos desse produto tem no estoque? "))
  qnt_estoque.append(valor)
  produtos.append(nome)
print("produtos: ", produtos)
print("quantidade em estoque: ", qnt_estoque)
nivel = []
for x in qnt_estoque:
  if x <5 :
    nivel.append("critico")
  elif x >=5 and x <10:
    nivel.append("baixo")
  else:
    nivel.append("normal")
print("nível de estoque: ", nivel)
