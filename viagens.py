distancia = float(input("Digite a distância que deseja percorrer (km): "))
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print(f"Valor da passagem: R$ {preco:.2f}")