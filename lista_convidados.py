convidados = []
 
print("=== Cadastro de Convidados ===")
for i in range(1, 6):
    nome = input(f"Digite o nome do convidado {i}: ")
    convidados.append(nome)
 
print("\n=== Lista de Convidados ===")
for convidado in convidados:
    print(f"- {convidado}")
 
print(f"\nTotal de convidados: {len(convidados)}")
