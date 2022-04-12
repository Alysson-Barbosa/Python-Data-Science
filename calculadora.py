# *** CALCULADORA PYTHON *** #

print("--- PYTHON CALCULATOR ---")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
escolha = int(input("Selecione o número da operação desejada (1/2/3/4): "))


if escolha == 1:
	soma = 0
	n1 = int(input("Escolha o primeiro numero: "))
	n2 = int(input("Escolha o segundo numero: "))
	soma = n1 + n2
	print(n1, " + ", n2, " = ", soma)

elif escolha == 2:
	  sub = 0
	  n1 = int(input("Escolha o primeiro número: "))
	  n2 = int(input("Escolha o segundo número: "))
	  sub = n1 - n2
	  print(n1, " - ", n2, " = ", sub)

elif escolha == 3:
	mult = 0
	n1 = int(input("Escolha o primeiro número: "))
	n2 = int(input("Escolha o segundo número: "))
	mult = n1*n2
	print(n1, " x ", n2, " = ", mult)

elif escolha == 4:
	div = 0
	n1 = int(input("Escolha o primeiro número: "))
	n2 = int(input("Escolha o segundo número: "))
	div = n1 / n2
	print(n1, " / ", n2, " = ", div)
else:
	print("Opção inválida!")


