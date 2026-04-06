print("******************************")
print("CÁLCULO DE GRANDEZAS ELÉTRICAS")
print("******************************")
print("1. Tensão (em Volt)")
print("2. Resistência (em Ohm)")
print("3. Corrente (em Ampére)")
print("4. Sair do programa")
print("******************************")
opcao = int(input("Qual grandeza deseja calcular? "))
if opcao == 1:
    r = float(input("Digite a Resistência (Ω): "))
    i = float(input("Digite a Corrente (A): "))
    print(f"Tensão: {r * i:.2f} V")
elif opcao == 2:
    u = float(input("Digite a Tensão (V): "))
    i = float(input("Digite a Corrente (A): "))
    print(f"Resistência: {u / i:.2f} Ω")
elif opcao == 3:
    u = float(input("Digite a Tensão (V): "))
    r = float(input("Digite a Resistência (Ω): "))
    print(f"Corrente: {u / r:.2f} A")
elif opcao == 4:
    print("Saindo do programa...")
else:
    print("Opção inválida!")