letra = input("Digite uma letra: ").strip()
if len(letra)!=1 or not letra.isalpha():
  print ("erro entrada invalida! Digite uma letra somente")
else:
  if letra.lower() in "aeiou":
    print("vogal")
  else:
    print("consoante")