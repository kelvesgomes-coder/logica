print("-" * 20)
print("calculo do IRRF")
print("-" * 20)
resposta = True
while True:
    try:
        sal_bruto = float(input("digite seu salário bruto: "))
        if 2428.81 < sal_bruto <= 2826.65:
            irrf = 0.075
        elif 2826.81 < sal_bruto <= 3751.05:
            irrf = 0.15
        elif 3751.05 < sal_bruto <= 4664.68:
            irrf = 0.255
        else:
            irrf = 0.275
            print(f"{sal_bruto} com {irrf}% = R$ {sal_bruto - (sal_bruto * irrf):.2f}")
    except ValueError:
        print("valor do salário inválido")
        resposta = input("Deseja realizar outro cálculoi (S/N): ")
    if resposta == 'S' or resposta == 's':
       resposta = True
    else:
        resposta = False
