import socket

def scan_ports_simple(host):
    open_ports = []
    for port in range(20, 1025):  # skanuje porty 20-1024
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.3)  # timeout 300ms
            result = sock.connect_ex((host, port))
            if result == 0:
                open_ports.append(f"{port}/tcp - open")
            sock.close()
        except Exception:
            pass
    return open_ports
