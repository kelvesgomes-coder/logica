print("1 - À vista (em espécie)  - 10%")
print("2 - Cartão de débito      -  5%")
print("3 - Cartão de crédito     -  3%")
print("4 - PIX                   -  7.5%")
preco = float(input("Digite o preço total da venda (R$): "))
codigo = int(input("Forma de pagamento: ")) 
if codigo == 1:
    desconto = preco * 0.10
elif codigo == 2:
    desconto = preco * 0.05
elif codigo == 3:
    desconto = preco * 0.03
elif codigo == 4:
    desconto = preco * 0.075
else:
    print("Opção inválida!")
    exit()
print(f"Desconto: R$ {desconto:.2f}")
print(f"Valor final: R$ {preco - desconto:.2f}")