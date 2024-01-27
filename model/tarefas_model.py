from .bd_connection import bd_tarefas

class TarefasModel:
    def adicionar_tarefa(self, tarefa):
        bd_tarefas.append(tarefa)

    def get_tarefas(self):
        return bd_tarefas
