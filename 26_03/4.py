preco_antigo = float(input("Digite o preço antigo: "))

if preco_antigo <= 50:
  aumento = preco_antigo * 0.05
elif preco_antigo <= 100:
  aumento = preco_antigo * 0.10
else:
  aumento = preco_antigo * 0.15

preco_novo = preco_antigo + aumento

print(f"Preço novo: {preco_novo}")

if preco_novo <= 80:
  print("Barato")
elif preco_novo <= 120:
  print("Normal")
elif preco_novo <= 200:
  print("Caro")
else:
  print("Muito caro")