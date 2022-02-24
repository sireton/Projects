import socket 
import threading

from queue import Queue


# For target variable, input target IP
target = "10.0.0.1"
queue = Queue()
open_ports =[]


# Portscan funtion 
def portscan(port):
        
    try:
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.connect((target, port))
        return True
    except:
        return False


def fill_queue(port_list):
    for port in port_list: 
        queue.put(port)

def worker(): 
    while not queue.empty():
        port = queue.get()
        if portscan(port):
            print("Port {} is OPEN!".format(port))
            open_ports.append(port)
            
# Desired port range
port_list = range(1,1024)
fill_queue(port_list)

thread_list =[]

for t in range(10):
    thread = threading.Thread(target=worker)
    thread_list.append(thread)


for thread in thread_list:
    thread.start()

for thread in thread_list:
    thread.join()

print("Open ports are: ", open_ports)

#print(portscan(98))