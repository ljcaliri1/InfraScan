import socket


def scan_ports(target, ports=None):
    if ports is None:

        # Common ports list - Feel free to expand!
        ports = [21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 445, 8080]
    
    print(f"[+] Scanning {target}...")
    open_ports = []

    for port in ports:
        try:
           with socket.socket(socket.AF_INET, scoket.SOCK_STREAM) as sock:
              sock.settimeout(1)
              result = sock.connect_ex((target, port))
               print(f"[+] Port {port} is open")
               open_ports.append(port)
    except Exception as e:
        print(f"[-] Error scanning port {port}: {e}")

return open_ports


