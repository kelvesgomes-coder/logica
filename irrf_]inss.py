salario = float(input("Digite o salário (R$): "))
 
if salario <= 1320.00:
    inss = salario * 0.075
elif salario <= 2571.29:
    inss = salario * 0.09
elif salario <= 3856.94:
    inss = salario * 0.12
else:
    inss = salario * 0.14
 
base_irrf = salario - inss
 
if base_irrf <= 2112.00:
    irrf = 0
elif base_irrf <= 2826.65:
    irrf = base_irrf * 0.075 - 158.40
elif base_irrf <= 3751.05:
    irrf = base_irrf * 0.15 - 370.40
elif base_irrf <= 4664.68:
    irrf = base_irrf * 0.225 - 651.73
else:
    irrf = base_irrf * 0.275 - 884.96
 
print(f"\nSalário bruto : R$ {salario:.2f}")
print(f"Desconto INSS : R$ {inss:.2f}")
print(f"Desconto IRRF : R$ {irrf:.2f}")
print(f"Salário líquido: R$ {salario - inss - irrf:.2f}")
 