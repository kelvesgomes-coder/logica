nota = float(input("digite sua nota: (0-10)"))
prescenca = input("presença maior ou igual que 75% (sim/não)")
if nota >= 7 and presenca == "sim":
    print("aprovado")
elif nota < 5 and presenca == "não":
    print("reprovado")
else:
    print("recuperação")