import socket
from datetime import datetime

# Colors
GREEN = "\033[92m"
RED = "\033[91m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
MAGENTA = "\033[95m"
RESET = "\033[0m"

# Banner
print(f"""{MAGENTA}
██████╗  ██████╗ ██████╗ ████████╗
██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝
██████╔╝██║   ██║██████╔╝   ██║   
██╔═══╝ ██║   ██║██╔══██╗   ██║   
██║     ╚██████╔╝██║  ██║   ██║   
╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝   

     J I L S   R O Y — CYBER TOOLS
{RESET}""")

print(f"{CYAN}🔥 Tool #013 — Localhost Port Scanner 🔥{RESET}")
print(f"{YELLOW}Target: 127.0.0.1 (Your Own Machine Only){RESET}\n")

# Input
start_port = int(input("Enter start port (e.g. 20): "))
end_port = int(input("Enter end port (e.g. 100): "))

target = "127.0.0.1"

print(f"\n{CYAN}[+] Scanning localhost ports {start_port} → {end_port}...{RESET}")
print(f"{CYAN}[+] Started at: {datetime.now()}{RESET}\n")

open_ports = []

# Scan loop
for port in range(start_port, end_port + 1):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.3)

    result = sock.connect_ex((target, port))

    if result == 0:
        print(f"{GREEN}[OPEN] Port {port}{RESET}")
        open_ports.append(port)

    sock.close()

print(f"\n{MAGENTA}----------------------------------{RESET}")
print(f"{CYAN}[+] Scan complete.{RESET}")
print(f"{CYAN}[+] Open ports found: {len(open_ports)}{RESET}")

if open_ports:
    print(f"{GREEN}[+] Open Port List:{RESET}")
    for p in open_ports:
        print(f"   → Port {p}")
else:
    print(f"{RED}[-] No open ports detected on localhost.{RESET}")

print(f"\n{MAGENTA}😈 Local scan complete. Stay ethical.{RESET}")
