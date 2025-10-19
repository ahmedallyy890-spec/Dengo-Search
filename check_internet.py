import socket
def is_connected():
    hosts = [
        ("1.1.1.1", 80),
        ("8.8.8.8", 53),
        ("208.67.222.222", 53),
        ("9.9.9.9", 53),
        ("129.6.15.28", 123),
        ("162.159.200.1", 123)
    ]
    for host, port in hosts:
        try:
            socket.create_connection((host, port), timeout=0.5)
            return True
        except(OSError, socket.gaierror):
            continue
    
    return False