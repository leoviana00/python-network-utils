# Importando módulos

import threading
import socket
import time
from queue import Queue

# Scanner de porta usando soquete
def scan():
    """
    Varrer portas abertas em um host
    """
    socket.setdefaulttimeout(0.25)
    print_lock = threading.Lock()

    target = input('Digite o host a ser verificado: ')
    t_IP = socket.gethostbyname(target)
    print ('Iniciando a varredura no host: ', t_IP)

    def portscan(port):
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      try:
          con = s.connect((t_IP, port))
          with print_lock:
            print(port, 'está aberta')
          con.close()
      except:
          pass

    def threader():
      while True:
          worker = q.get()
          portscan(worker)
          q.task_done()
      
    q = Queue()
    startTime = time.time()
      
    for x in range(100):
      t = threading.Thread(target = threader)
      t.daemon = True
      t.start()
      
    for worker in range(1, 500):
      q.put(worker)
      
    q.join()
    print('Tempo gasto:', time.time() - startTime) 