import threading
import time
import random


def processo(nome, tempo_execucao):
    print(f"[{nome}] - Iniciou execução.")
    for i in range(1, tempo_execucao + 1):
        print(f"[{nome}] - Executando ciclo {i}/{tempo_execucao}")
        time.sleep(random.uniform(0.5, 1.5))  
    print(f"[{nome}] - Finalizou execução.\n")


threads = []
quantidade_processos = 5

for i in range(1, quantidade_processos + 1):
    tempo_execucao = random.randint(3, 6) 
    t = threading.Thread(target=processo, args=(f"Processo-{i}", tempo_execucao))
    threads.append(t)


for t in threads:
    t.start()


for t in threads:
    t.join()

print("Todos os processos foram finalizados.")
