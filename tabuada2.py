numero= int(input("digite o número da tabuada: "))
i = 1
print("--- tabuada do número {numero} ---")
while i <= 10:
    print(f"{i} x {numero} = ({i * numero})")
    i += 1
    print("fim da tabuada!")