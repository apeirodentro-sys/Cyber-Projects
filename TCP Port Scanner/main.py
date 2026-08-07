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

TCP_port_scanner('127.0.0.1', [9000,1])



