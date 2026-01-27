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
██████╗  █████╗ ███╗   ██╗███╗   ██╗███████╗██████╗ 
██╔══██╗██╔══██╗████╗  ██║████╗  ██║██╔════╝██╔══██╗
██████╔╝███████║██╔██╗ ██║██╔██╗ ██║█████╗  ██████╔╝
██╔═══╝ ██╔══██║██║╚██╗██║██║╚██╗██║██╔══╝  ██╔══██╗
██║     ██║  ██║██║ ╚████║██║ ╚████║███████╗██║  ██║
╚═╝     ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝

     J I L S   R O Y   —   C Y B E R   T O O L S
{RESET}""")

print(f"{CYAN}🔥 Tool #009 — Banner Grabber 🔥{RESET}\n")

target = input(f"{YELLOW}Enter target IP or domain: {RESET}")
port = int(input(f"{YELLOW}Enter port (e.g. 22, 21, 80): {RESET}"))

print(f"\n{BLUE}[+] Connecting to service...{RESET}")

try:
    sock = socket.socket()
    sock.settimeout(5)
    sock.connect((target, port))

    try:
        banner = sock.recv(4096).decode(errors="ignore").strip()
    except:
        banner = ""

    if banner:
        print(f"{GREEN}[BANNER] {banner}{RESET}")
    else:
        print(f"{YELLOW}[!] No banner received (service may require handshake){RESET}")

    sock.close()

except socket.gaierror:
    print(f"{RED}[-] Hostname could not be resolved{RESET}")

except socket.timeout:
    print(f"{RED}[-] Connection timed out{RESET}")

except ConnectionRefusedError:
    print(f"{RED}[-] Connection refused (port closed or filtered){RESET}")

except Exception as e:
    print(f"{RED}[-] Error: {e}{RESET}")

print(f"\n{MAGENTA}😈 Banner grab complete. Stay stealthy.{RESET}")
