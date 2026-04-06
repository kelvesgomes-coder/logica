print("1 - Opção 1")
print("2 - Opção 2")
print("3 - Opção 3")
print("4 - Sair")
try:
    opcao = int(input("Digite uma opção: "))
except ValueError:
    opcao = -1
if opcao == 1:
    print("Você selecionou a opção 1")
elif opcao == 2:
    print("Você selecionou a opção 2")
elif opcao == 3:
    print("Você selecionou a opção 3")
elif opcao == 4:
    print("Você selecionou sair")
else:
    print("Opção inválida")
print("Fim do programa")