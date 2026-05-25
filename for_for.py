numeros = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

soma_total = 0

for lista in numeros:
    for numero in lista:
        print(numero)
        soma_total += numero

print(f"\nsoma total: {soma_total}")