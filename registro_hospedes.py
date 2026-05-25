quantidade = int(input("quantas pessoas no quarto? (1-4): "))
quarto = []

for i in range(quantidade):
    print(f"\ncadastrando pessoa {i + 1}:")
    nome = input("nome: ")
    cpf  = input("CPF: ")
    quarto.append([nome, f"cpf:{cpf}"])

print("\nquarto = [")
for pessoa in quarto:
    print(f"    {pessoa},")
print("]")