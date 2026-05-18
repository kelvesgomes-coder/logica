tarefas = []
 
print("=== Cadastro de Tarefas ===")
print("Digite 'fim' para encerrar o cadastro.\n")
 
while True:
    tarefa = input("Digite uma tarefa: ")
    if tarefa.lower() == "fim":
        break
    tarefas.append(tarefa)
 
print("\n=== Suas Tarefas ===")
if tarefas:
    for i, tarefa in enumerate(tarefas, start=1):
        print(f"{i}. {tarefa}")
else:
    print("Nenhuma tarefa cadastrada.")
