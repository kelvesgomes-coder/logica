celsius = []
 
print("=== Cadastro de Temperaturas ===")
print("Digite 'sair' para encerrar.\n")
 
while True:
    entrada = input("Digite a temperatura em Celsius: ")
    if entrada.lower() == "sair":
        break
    try:
        temp = float(entrada)
        celsius.append(temp)
    except ValueError:
        print("Valor inválido. Digite um número ou 'sair'.")
 
if celsius:
    fahrenheit = [(c * 9 / 5) + 32 for c in celsius]
 
    media_celsius = sum(celsius) / len(celsius)
    media_fahrenheit = sum(fahrenheit) / len(fahrenheit)
 
    print("\n=== Temperaturas Convertidas ===")
    print(f"{'Celsius':>10} | {'Fahrenheit':>10}")
    print("-" * 25)
    for c, f in zip(celsius, fahrenheit):
        print(f"{c:>9.1f}° | {f:>9.1f}°")
 
    print(f"\nMédia Celsius:    {media_celsius:.2f}°C")
    print(f"Média Fahrenheit: {media_fahrenheit:.2f}°F")
else:
    print("Nenhuma temperatura cadastrada.")
