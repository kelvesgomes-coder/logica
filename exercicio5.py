soma = 0
maior = 0
menor = 0
impares = 0
pares = 0
num_pares = 0
num_impares = 0
for i in range(1, 11):
    num = float(input(f"digite {i}º número: "))

    soma += num
    if i == 1:
        maior = num
        menor = num
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    if num % 2 == 0:
        pares += num
        num_pares += 1
    else:
        impares += num
        num_impares += 1
print(f"soma = {soma}")
print(f"média = {soma / 10}")
print(f"maior = {maior}")
print(f"menor = {menor}")
print(f"soma dos pares = {pares}")
print(f"soma dos ímpares = {impares}")
print(f"número de pares = {num_pares}")
print(f"número de ímpares = {num_impares}")