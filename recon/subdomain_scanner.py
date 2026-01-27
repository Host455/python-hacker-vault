import requests
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
███████╗██╗   ██╗██████╗ ██████╗  ██████╗ 
██╔════╝██║   ██║██╔══██╗██╔══██╗██╔═══██╗
███████╗██║   ██║██████╔╝██████╔╝██║   ██║
╚════██║██║   ██║██╔══██╗██╔══██╗██║   ██║
███████║╚██████╔╝██████╔╝██████╔╝╚██████╔╝
╚══════╝ ╚═════╝ ╚═════╝  ╚═════╝  ╚═════╝

     J I L S   R O Y   —   C Y B E R   T O O L S
{RESET}""")

print(f"{CYAN}🔥 Tool #007 — Subdomain Scanner 🔥{RESET}\n")

domain = input(f"{YELLOW}Enter domain (e.g. example.com): {RESET}")

subdomains = [
    "www", "admin", "api", "dev", "test", "mail",
    "staging", "beta", "portal", "dashboard",
    "vpn", "blog", "shop", "support"
]

print(f"\n{BLUE}[+] Initializing subdomain scan...{RESET}")
start_time = time.time()

found = []

headers = {
    "User-Agent": "CyberRecon/1.0"
}

for sub in subdomains:
    host = f"{sub}.{domain}"

    try:
        ip = socket.gethostbyname(host)
        url = f"http://{host}"

        t1 = time.time()
        r = requests.get(url, timeout=5, headers=headers)
        t2 = time.time()

        status = r.status_code
        response_time = round(t2 - t1, 2)

        print(f"{GREEN}[FOUND] {host} → {ip} | {status} | {response_time}s{RESET}")
        found.append((host, ip, status, response_time))

    except socket.gaierror:
        print(f"{CYAN}[MISS] {host} (DNS not found){RESET}")

    except requests.exceptions.RequestException:
        print(f"{YELLOW}[WARN] {host} (No HTTP response){RESET}")

elapsed = round(time.time() - start_time, 2)

print(f"\n{MAGENTA}----------------------------------{RESET}")
print(f"{GREEN}[+] Scan complete{RESET}")
print(f"{CYAN}[+] Time taken: {elapsed}s{RESET}")
print(f"{CYAN}[+] Subdomains found: {len(found)}{RESET}")

if found:
    print(f"\n{GREEN}[+] Live subdomains:{RESET}")
    for item in found:
        print(f"{CYAN}{item[0]} → {item[1]} | {item[2]} | {item[3]}s{RESET}")

print(f"\n{MAGENTA}😈 Subdomain recon complete. Stay stealthy.{RESET}")
