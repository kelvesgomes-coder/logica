lista_compras = []
 
 
def exibir_menu():
    print("\n=== Lista de Compras ===")
    print("1 - Adicionar à lista")
    print("2 - Pesquisar item")
    print("3 - Remover item")
    print("4 - Alterar item")
    print("5 - Listar produtos")
    print("6 - Sair")
 
 
def adicionar():
    print("\nDigite os produtos (ou 'sair' para voltar ao menu):")
    while True:
        produto = input("Produto: ").strip().lower()
        if produto == "sair":
            break
        if produto:
            lista_compras.append(produto)
            print(f"'{produto}' adicionado com sucesso!")
 
 
def pesquisar():
    produto = input("\nDigite o produto a pesquisar: ").strip().lower()
    if produto in lista_compras:
        print(f"Produto encontrado: {produto}")
    else:
        print("Produto não encontrado.")
 
 
def remover():
    produto = input("\nDigite o produto a remover: ").strip().lower()
    if produto in lista_compras:
        lista_compras.remove(produto)
        print("Produto encontrado e removido com sucesso!")
    else:
        print("Produto não encontrado.")
 
 
def alterar():
    produto = input("\nDigite o produto a alterar: ").strip().lower()
    if produto in lista_compras:
        novo = input("Digite o novo nome do produto: ").strip().lower()
        indice = lista_compras.index(produto)
        lista_compras[indice] = novo
        print("Produto alterado com sucesso!")
    else:
        print("Produto não encontrado.")
 
 
def listar():
    if not lista_compras:
        print("\nLista vazia.")
    else:
        print("\n=== Produtos Cadastrados ===")
        for i, produto in enumerate(lista_compras, start=1):
            print(f"{i}. {produto}")
 
 
while True:
    exibir_menu()
    opcao = input("\nEscolha uma opção: ").strip()
 
    if opcao == "1":
        adicionar()
    elif opcao == "2":
        pesquisar()
    elif opcao == "3":
        remover()
    elif opcao == "4":
        alterar()
    elif opcao == "5":
        listar()
    elif opcao == "6":
        print("\nPrograma encerrado com sucesso!")
        break
    else:
        print("Opção inválida. Tente novamente.")
