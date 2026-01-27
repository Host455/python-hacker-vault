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

# Big Cyberpunk Name Banner
print(f"""{MAGENTA}
 ██████╗██╗   ██╗██████╗ ███████╗██████╗ 
██╔════╝╚██╗ ██╔╝██╔══██╗██╔════╝██╔══██╗
██║      ╚████╔╝ ██████╔╝█████╗  ██████╔╝
██║       ╚██╔╝  ██╔══██╗██╔══╝  ██╔══██╗
╚██████╗   ██║   ██████╔╝███████╗██║  ██║
 ╚═════╝   ╚═╝   ╚═════╝ ╚══════╝╚═╝  ╚═╝

      J I L S   R O Y   —   C Y B E R   T O O L S
{RESET}""")

print(f"{CYAN}🔥 Tool #003 v2 — Cyberpunk Banner Grabber 🔥{RESET}\n")

target = input(f"{YELLOW}Enter target IP or domain: {RESET}")
port = input(f"{YELLOW}Enter target port: {RESET}")

try:
    port = int(port)
except:
    print(f"{RED}[-] Invalid port number{RESET}")
    exit()

try:
    target_ip = socket.gethostbyname(target)
except:
    print(f"{RED}[-] Invalid target{RESET}")
    exit()

print(f"\n{BLUE}[+] Initializing cyber-connection...{RESET}")
time.sleep(0.5)
print(f"{BLUE}[+] Connecting to {target_ip}:{port}...{RESET}")

try:
    s = socket.socket()
    s.settimeout(3)
    s.connect((target_ip, port))

    print(f"{GREEN}[+] Connection established{RESET}")

    # Try receiving banner
    try:
        banner = s.recv(1024).decode(errors="ignore").strip()
        if banner:
            print(f"{GREEN}[+] Banner received:{RESET}")
            print(f"{CYAN}{banner}{RESET}")
        else:
            print(f"{YELLOW}[!] No banner received (service silent){RESET}")
    except:
        print(f"{RED}[-] Failed to receive banner{RESET}")

    s.close()

except Exception as e:
    print(f"{RED}[-] Connection failed:{RESET}", e)

print(f"\n{MAGENTA}😈 Cyber scan complete. Stay anonymous.{RESET}")
