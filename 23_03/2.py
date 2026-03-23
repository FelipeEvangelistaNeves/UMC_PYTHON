salario = float(input("Digite o salário do funcionário: "))
cargo = input("Digite o cargo do funcionário (Gerente, Engenheiro ou Técnico): ")
if cargo == "Gerente":
    novosalario = salario * 1.10
elif cargo == "Engenheiro":
    novosalario = salario * 1.20
elif cargo == "Técnico":
    novosalario = salario * 1.30
else:
    novosalario = salario*1.4

print("antigo salario do funcionario é:", salario)
input("Pressione Enter para continuar...")
print("novo salario do funcionario é ", novosalario)
input("Pressione Enter para continuar...")
print("a diferença dos salarios é:", novosalario - salario)