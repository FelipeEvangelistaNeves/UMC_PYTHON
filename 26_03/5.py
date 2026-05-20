codigo = int(input("Digite o código do item: "))
quantidade = int(input("Digite a quantidade: "))

if codigo == 100:
  preco = 3.50
elif codigo == 101:
  preco = 3.80
elif codigo == 102:
  preco = 4.50
elif codigo == 103:
  preco = 4.70
elif codigo == 104:
  preco = 5.30
elif codigo == 105:
  preco = 4.00
else:
  print("Código inválido")
  exit()

total = preco * quantidade
print(f"Total a pagar: R$ {total}")