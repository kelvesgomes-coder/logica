valor = float(input("digite o valor da compra: "))
premium = input("é cliente premiumn (sim/não)")
if valor > 150 or premium == "sim":
    print("frete grátis...")
else:
    print("pagar frete")