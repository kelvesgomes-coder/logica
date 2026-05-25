meta = 10000
vendas = [
    ['joão', 15000], ['julia', 27000],
    ['marcos', 9900],  ['maria', 3750],
    ['ana', 10300],   ['daniel', 7870],
]

print("vendedores que bateram a meta:")
for vendedor, valor in vendas:
    if valor >= meta:
        print(f"  {vendedor}: R$ {valor:,.2f}")
