num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))
 
maior = num1
if num2 > maior:
    maior = num2
if num3 > maior:
    maior = num3
 
menor = num1
if num2 < menor:
    menor = num2
if num3 < menor:
    menor = num3
 
soma = num1 + num2 + num3
media = soma / 3
 
print("**********")
print(f"maior = {maior}")
print(f"menor = {menor}")
print(f"soma = {soma}")
print(f"media = {media}")
 
 