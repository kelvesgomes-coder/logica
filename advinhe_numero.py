import random

numero_secreto = random.randint(1, 100)
tentativas = 0
chute = 0

while chute != numero_secreto:
    chute = int(input("Adivinhe o número (1-100): "))
    tentativas += 1
    if chute < numero_secreto:
        print("Maior")
    elif chute > numero_secreto:
        print("Menor")

print(f"Acertou em {tentativas} tentativas")