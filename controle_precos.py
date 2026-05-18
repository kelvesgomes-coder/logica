precos = []
 
print("=== Cadastro de Preços ===")
for i in range(1, 6):
    preco = float(input(f"Digite o preço {i}: R$ "))
    precos.append(preco)
 
print("\n=== Resultado ===")
print(f"Preços cadastrados: {precos}")
print(f"Maior preço: R$ {max(precos):.2f}")
print(f"Menor preço: R$ {min(precos):.2f}")
