import socket
from typing import List, Dict

def scan_ports(target: str, ports: List[int], grab_banner: bool = False) -> Dict:
    results = {
        "target": target,
        "open_ports": []
    }

    if not ports:
        ports = list(range(i, 1025))  #Default scan range if none provided

    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((target, port))


            if result == 0:
                port_info = {"port": port}


                if grab_banner:
                    try:
                        sock.send(b"HEAD / HTTP/1.1\r\n\r\n")
                        banner = sock.recv(1024).decode(errors="ignore").strip()
                        port_info["banner"] = banner
                    except:
                        port_info["banner"] = "Banner grab failed"


                results["open_ports"].append(port_info)

            sock.close()

        except Exception as e:
            print(f"[-] Error scanning port {port}: {e}")

    return results

