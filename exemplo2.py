# -*- coding: utf-8 -*-

from java.util import ArrayList, Collections, HashMap

def criar_lista_tarefas():
    tarefas = ArrayList()
    tarefas.add("Estudar Jython")
    tarefas.add("Preparar o jantar")
    tarefas.add("Corrigir bug no sistema")
    tarefas.add("Colocar o lixo pra fora")
    return tarefas

def marcar_concluidas(tarefas):
    status = HashMap()
    for i in range(tarefas.size()):
        tarefa = tarefas.get(i)
        status.put(tarefa, i % 2 == 0)
    return status

def exibir_tarefas(tarefas, status):
    for i in range(tarefas.size()):
        tarefa = tarefas.get(i)
        concluida = status.get(tarefa)
        marcador = "[x]" if concluida else "[]"
        print("%s %s" % (marcador, tarefa))
    

if __name__ == "__main__":
    tarefas = criar_lista_tarefas()

    print("=== Tarefas (ordem original) ===")
    exibir_tarefas(tarefas, marcar_concluidas(tarefas))

    Collections.sort(tarefas)

    print("\n=== Tarefas ordenadas (java.util.Collections.sort) ===")
    exibir_tarefas(tarefas, marcar_concluidas(tarefas))
    