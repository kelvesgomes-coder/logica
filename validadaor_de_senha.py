ESPECIAIS = "!@#$%^&*()-_=+[]{}|;:',.<>?/`~\"\\"
 
def validar_senha(senha):
    tem_maiuscula = False
    tem_minuscula = False
    tem_especial  = False
    tem_numero    = False
 
    for caractere in senha:
        if caractere.isupper():
            tem_maiuscula = True
        elif caractere.islower():
            tem_minuscula = True
        elif caractere.isdigit():
            tem_numero = True
        elif caractere in ESPECIAIS:
            tem_especial = True
 
    requisitos_ausentes = []
 
    if len(senha) < 8:
        requisitos_ausentes.append("Mínimo de 8 caracteres")
    if not tem_maiuscula:
        requisitos_ausentes.append("Pelo menos uma letra maiúscula")
    if not tem_minuscula:
        requisitos_ausentes.append("Pelo menos uma letra minúscula")
    if not tem_especial:
        requisitos_ausentes.append("Pelo menos um caractere especial")
    if not tem_numero:
        requisitos_ausentes.append("Pelo menos um número")
 
    if not requisitos_ausentes:
        print("Senha aceita")
    else:
        print("Senha recusada. Não atende os requisitos: ")
        for requisito in requisitos_ausentes:
            print(f"  - {requisito}")
 
 
senha = input("Digite uma senha: ")
validar_senha(senha)