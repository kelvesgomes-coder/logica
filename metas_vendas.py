venda     = [250,330,440,540,350,250,368,40,250,30,30]
vendedores = ['maria','fernando','joão','pedro','silvia','mario',
              'carlos','mateus','ana','chica','luiz']
meta = 50
i = 0

while i < len(vendedores):
    if venda[i] >= meta:
        print(vendedores[i])
    i += 1