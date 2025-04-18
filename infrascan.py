import pyfiglet

def print_banner():
    banner = pyfiglet.figlet_format("InfraScan")
    print(banner)
    print("Red Halo - Infrastructure Scanner\n")




import argparse
from modules.port_scanner import scan_ports

def main():
    print_banner()
    parser = argparse.ArgumentParser(description="InfraScan - Red Halo's Infrastructure Scanner")
    parser .add_argument("--target", required=True, help="Target IP or domain")
    parser .add_argument("--ports", help="Comma-seperated ports (default: 1-1024 or top 1000)")
    parser .add_argument("--banner", action="store_true", help="Attempt to grab service banners")
    parser .add_argument("--output", help="Output file path (JSON format)")

    args = parser.parse_args()


    ports = []
    if args.ports:
        ports = [int(p.strip()) for p in args.ports.split(",")]



    print(f"[+] Starting scan on {args.target}")
    results = scan_ports(args.target, ports, args.banner)


    import json
    if args.output:
        with open(args.output, "w") as f:
            json.dump(results, f, indent=4)
        print(f"[+] Scan results saved to {args.output}")
    else:
        print("[+] Scan Results:")
        print(json.dumps(results, indent=4))


if __name__ == "__main__":
    main()
