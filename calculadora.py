print("1 - Adição")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
print("5 - Potência")
print("6 - Raiz quadrada")
print("7 - Número par")
print("8 - Número ímpar")
try:
    opcao = int(input("Escolha uma operação: "))
except ValueError:
    opcao = -1
if opcao in [1, 2, 3, 4, 5]:
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
    except ValueError:
        print("Valor inválido!")
        exit()
elif opcao in [6, 7, 8]:
    try:
        num1 = float(input("Digite o número: "))
    except ValueError:
        print("Valor inválido!")
        exit()
if opcao == 1:
    print(f"Resultado: {num1 + num2}")
elif opcao == 2:
    print(f"Resultado: {num1 - num2}")
elif opcao == 3:
    print(f"Resultado: {num1 * num2}")
elif opcao == 4:
    if num2 != 0:
        print(f"Resultado: {num1 / num2}")
    else:
        print("Erro: divisão por zero!")
elif opcao == 5:
    print(f"Resultado: {num1 ** num2}")
elif opcao == 6:
    print(f"Resultado: {num1 ** 0.5}")
elif opcao == 7:
    if num1 % 2 == 0:
        print(f"{int(num1)} é par")
    else:
        print(f"{int(num1)} não é par")
elif opcao == 8:
    if num1 % 2 != 0:
        print(f"{int(num1)} é ímpar")
    else:
        print(f"{int(num1)} não é ímpar")
else:
    print("Opção inválida")