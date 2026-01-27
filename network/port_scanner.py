import socket
import time

# ANSI Colors
GREEN = "\033[92m"
RED = "\033[91m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
MAGENTA = "\033[95m"
BLUE = "\033[94m"
RESET = "\033[0m"

# Cyberpunk Banner
print(f"""{MAGENTA}
██████╗  ██████╗ ██████╗ ████████╗
██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝
██████╔╝██║   ██║██████╔╝   ██║   
██╔═══╝ ██║   ██║██╔══██╗   ██║   
██║     ╚██████╔╝██║  ██║   ██║   
╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝   

     J I L S   R O Y   —   C Y B E R   T O O L S
{RESET}""")

print(f"{CYAN}🔥 Tool #008 — Fast Port Scanner 🔥{RESET}\n")

target = input(f"{YELLOW}Enter target IP or domain: {RESET}")

ports = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    3306: "MySQL",
    8080: "HTTP-ALT"
}

print(f"\n{BLUE}[+] Initializing port scan...{RESET}")
start_time = time.time()

open_ports = []

for port, service in ports.items():
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        result = sock.connect_ex((target, port))

        if result == 0:
            elapsed = round(time.time() - start_time, 2)
            print(f"{GREEN}[OPEN] {port}/tcp ({service}){RESET}")
            open_ports.append((port, service))

        sock.close()

    except socket.gaierror:
        print(f"{RED}[-] Hostname could not be resolved{RESET}")
        break

    except socket.error:
        print(f"{RED}[-] Could not connect to server{RESET}")
        break

elapsed_total = round(time.time() - start_time, 2)

print(f"\n{MAGENTA}----------------------------------{RESET}")
print(f"{GREEN}[+] Scan complete{RESET}")
print(f"{CYAN}[+] Time taken: {elapsed_total}s{RESET}")
print(f"{CYAN}[+] Open ports found: {len(open_ports)}{RESET}")

if open_ports:
    print(f"\n{GREEN}[+] Open services:{RESET}")
    for port, service in open_ports:
        print(f"{CYAN}{port}/tcp → {service}{RESET}")

print(f"\n{MAGENTA}😈 Port scan complete. Stay stealthy.{RESET}")
