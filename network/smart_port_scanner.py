import socket
from datetime import datetime

# Colors
GREEN = "\033[92m"
RED = "\033[91m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
MAGENTA = "\033[95m"
RESET = "\033[0m"

# Common Service Map
SERVICE_MAP = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP (Mail)",
    53: "DNS",
    80: "HTTP (Web Server)",
    110: "POP3",
    139: "NetBIOS",
    143: "IMAP",
    443: "HTTPS (Secure Web)",
    3306: "MySQL Database",
    8080: "HTTP-ALT (Web App)",
}

# Banner
print(f"""{MAGENTA}
███████╗ ██████╗ █████╗ ███╗   ██╗
██╔════╝██╔════╝██╔══██╗████╗  ██║
███████╗██║     ███████║██╔██╗ ██║
╚════██║██║     ██╔══██║██║╚██╗██║
███████║╚██████╗██║  ██║██║ ╚████║
╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝

     J I L S   R O Y — CYBER TOOLS
{RESET}""")

print(f"{CYAN}🔥 Tool #014 — Smart Local Port Scanner 🔥{RESET}")
print(f"{YELLOW}Target: 127.0.0.1 (Safe Localhost Only){RESET}\n")

# Default Scan Ports
default_ports = list(SERVICE_MAP.keys())

print(f"{CYAN}[+] Default ports to scan:{RESET}")
print(default_ports)

choice = input(f"\n{YELLOW}Scan only common ports? (y/n): {RESET}")

if choice.lower() == "y":
    ports_to_scan = default_ports
else:
    start = int(input("Enter start port: "))
    end = int(input("Enter end port: "))
    ports_to_scan = range(start, end + 1)

target = "127.0.0.1"

print(f"\n{CYAN}[+] Scan started at: {datetime.now()}{RESET}\n")

open_ports = []

# Scan Loop
for port in ports_to_scan:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.3)

    result = sock.connect_ex((target, port))

    if result == 0:
        service = SERVICE_MAP.get(port, "Unknown Service")
        print(f"{GREEN}[OPEN] Port {port} → {service}{RESET}")
        open_ports.append((port, service))

    sock.close()

# Report
print(f"\n{MAGENTA}----------------------------------{RESET}")
print(f"{CYAN}[+] Scan complete.{RESET}")
print(f"{CYAN}[+] Open ports found: {len(open_ports)}{RESET}")

if open_ports:
    print(f"\n{GREEN}[+] Live Services Running:{RESET}")
    for p, s in open_ports:
        print(f"   → Port {p} ({s})")
else:
    print(f"{RED}[-] No common ports open on localhost.{RESET}")

print(f"\n{MAGENTA}😈 Tool #014 Complete. Stay ethical.{RESET}")
