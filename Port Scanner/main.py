import socket

def TCP_connect_port(ip, port):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(1)
    value = client.connect((ip, port))
    client.close()
    return value

def TCP_port_scanner(ip, ports):
    open_ports = []
    closed_ports = []
    blocked_ports = []
    for port in ports:
        try:
            state = TCP_connect_port(ip,port)
            if state == None:
                open_ports.append(port)

        except ConnectionRefusedError:
            closed_ports.append(port)
        except (TimeoutError, socket.timeout):
            blocked_ports.append(port)
    return [open_ports,closed_ports,blocked_ports]

def UDP_connect_port(ip, port):
    MAX_COUNT = 2
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client.settimeout(1)
    count = 0
    while count <= MAX_COUNT:
        count+=1
        client.sendto(b"PING", (ip, port))
        data, _ = client.recvfrom(1024)
        if data.decode('utf-8').strip() == "PONG":
            client.close()
            return 1
    return 0

def UDP_port_scanner(ip, ports): #assuming there is a response mechanism on the server
    open_ports = []
    notopen_ports = []
    for port in ports:
        if UDP_connect_port(ip, port) == 1:
            open_ports.append(port)
        else:
            notopen_ports.append(port)
        
    
TCP_port_scanner('127.0.0.1', [9000,1])



