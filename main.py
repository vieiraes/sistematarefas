import controller.tarefas_controller as controller

while True:
    print("\n1. Adicionar Tarefa\n2. Mostrar Tarefas\n3. Sair" )
    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        controller.adicionar_tarefa()
    elif escolha == "2":
        controller.mostrar_tarefas()
    elif escolha == "3":
        break #finaliza o programa
