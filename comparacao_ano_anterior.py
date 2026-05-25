produtos   = ['iphone','galaxy','tablet','tv','torradeira',
              'kindle','geladeira','forno','notebook positivo',
              'notebook hp','notebook asus','mouse logitech',
              'webcam','caixa de som jbl','microfone','câmera']
vendas2019 = [558147,712350,573823,405252,718654,531580,973139,892292,
              422760,154753,887061,438508,237467,489705,328311,591120]
vendas2020 = [951642,244295,26964,787604,867660,78830,710331,646016,
              694913,539704,324831,667179,295633,725316,644622,994303]

print("Produtos com crescimento em 2020:")
for i, produto in enumerate(produtos):
    v19 = vendas2019[i]
    v20 = vendas2020[i]
    if v20 > v19:
        crescimento = (v20 / v19 - 1) * 100
        print(f"  {produto}: {v19} → {v20}  (+{crescimento:.1f}%)")