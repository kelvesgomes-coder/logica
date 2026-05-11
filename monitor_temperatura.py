def monitor_temperatura():
    LIMITE = 80
 
    while True:
        entrada = input("Temperatura atual (°C) ou 'sair': ").strip().lower()
 
        if entrada == "sair":
            print("Sistema encerrado.")
            break
 
        try:
            temperatura = float(entrada)
        except ValueError:
            print("Entrada inválida. Digite um número ou 'sair'.")
            continue
 
        if temperatura > LIMITE:
            print(f"ALERTA! Temperatura crítica: {temperatura}°C")
            print("Resfriamento ativado!")
        elif temperatura >= LIMITE * 0.9:
            print(f"Atenção: temperatura elevada: {temperatura}°C")
        else:
            print(f"Temperatura normal: {temperatura}°C")
 
 
monitor_temperatura()
 
 