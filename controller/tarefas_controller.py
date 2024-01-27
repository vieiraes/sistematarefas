from model.tarefas_model import TarefasModel
import view.tarefas_view as view

# Instanciar o modelo
modelo = TarefasModel()

def adicionar_tarefa():
    tarefa = view.nova_tarefa()
    modelo.adicionar_tarefa(tarefa)

def mostrar_tarefas():
    tarefas = modelo.get_tarefas()
    view.mostrar_tarefas(tarefas)
