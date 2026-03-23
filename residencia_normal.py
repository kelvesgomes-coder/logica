consumo = float(input("digite o consumo de água em m3: "))
if consumo <= 10:
    valor = 22.38
elif consumo <= 20:
    valor = consumo * 3.50
elif consumo <= 50:
    valor = consumo * 8.75
else:
    valor = consumo * 9.64
print(f"valor da conta: R$ {valor:.2f}")