from scanner.port_scanner import scan_ports

def main():
    print("=== InfraScan: Port Scanner ===")
    target = input("Enter target IP or domain: ")

    open_ports = scan_ports(target)

    if open_ports: 
        print(f"\n[+] Open ports on {target}: {open_ports}")
    else:
       print(f"\n[-] Nopen ports found on {target}")

if __name__ == "__main__":
    main()
