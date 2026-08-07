from socket import SOCK_STREAM
import socket
import threading


def server():
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #it will only listen.
    #allows multiple connections
    servidor.bind(('127.0.0.1', 9000))
    servidor.listen(1) #waits for a client to connect
    connection, address = servidor.accept() #accepts the client connection
    #connection is used to communicate, can have multiple.
    recv_message = connection.recv(1048)
    print(recv_message.decode('utf-8'))
    servidor.close()
    connection.close()

def client():
    client = socket.socket(socket.AF_INET, SOCK_STREAM)
    client.connect(('127.0.0.1', 9000))
    client.send('Hey'.encode('utf-8'))
    client.close()


t1 = threading.Thread(target=server)
t2 = threading.Thread(target=client)

t1.start()
t2.start()

t1.join()
t2.join()
