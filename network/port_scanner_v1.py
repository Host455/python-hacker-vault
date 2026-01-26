import socket
import time
from datetime import datetime

# ANSI Colors
GREEN = "\033[92m"
RED = "\033[91m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RESET = "\033[0m"

print(f"{CYAN}🔥 Tool #002 v2 — Colorful Port Scanner 🔥{RESET}")

target = input("Enter target IP or domain: ")

try:
    target_ip = socket.gethostbyname(target)
except:
    print(f"{RED}[-] Invalid target{RESET}")
    exit()

start_port = 1
end_port = 1024

print(f"\n{YELLOW}[+] Scanning started at: {datetime.now()}{RESET}")
print(f"{YELLOW}[+] Target: {target_ip}{RESET}")
print(f"{YELLOW}[+] Port Range: {start_port}-{end_port}{RESET}")
print("-" * 50)

open_ports = []
scanned = 0
start_time = time.time()
last_stats_time = start_time

try:
    for port in range(start_port, end_port + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.3)
        result = s.connect_ex((target_ip, port))
        s.close()

        scanned += 1

        if result == 0:
            open_ports.append(port)
            print(f"{GREEN}[OPEN] Port {port}{RESET}")

        # Show live stats every 2 seconds
        current_time = time.time()
        if current_time - last_stats_time >= 2:
            elapsed = int(current_time - start_time)
            print(f"{CYAN}\n[STATS] Scanned: {scanned} | Open: {len(open_ports)} | Time: {elapsed}s{RESET}")
            print("-" * 50)
            last_stats_time = current_time

except KeyboardInterrupt:
    print(f"\n{RED}[!] Scan stopped by user{RESET}")

print("-" * 50)
print(f"{YELLOW}[+] Scan finished at: {datetime.now()}{RESET}")
print(f"{GREEN}[+] Total open ports: {len(open_ports)}{RESET}")

if open_ports:
    print(f"{GREEN}[+] Open ports list: {open_ports}{RESET}")

print(f"{CYAN}😈 Done.{RESET}")
