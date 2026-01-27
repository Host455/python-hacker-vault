import requests
import time

# ANSI Colors
GREEN = "\033[92m"
RED = "\033[91m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
MAGENTA = "\033[95m"
BLUE = "\033[94m"
RESET = "\033[0m"

# Cyberpunk ASCII Banner
print(f"""{MAGENTA}
██╗  ██╗████████╗████████╗██████╗ 
██║  ██║╚══██╔══╝╚══██╔══╝██╔══██╗
███████║   ██║      ██║   ██████╔╝
██╔══██║   ██║      ██║   ██╔═══╝ 
██║  ██║   ██║      ██║   ██║     
╚═╝  ╚═╝   ╚═╝      ╚═╝   ╚═╝     

   J I L S   R O Y   —   C Y B E R   T O O L S
{RESET}""")

print(f"{CYAN}🔥 Tool #004 — HTTP Status Checker 🔥{RESET}\n")

url = input(f"{YELLOW}Enter target URL (e.g. https://example.com): {RESET}")

if not url.startswith("http"):
    url = "http://" + url

print(f"\n{BLUE}[+] Initializing web probe...{RESET}")
start_time = time.time()

try:
    response = requests.get(url, timeout=10)
    end_time = time.time()

    status = response.status_code
    server = response.headers.get("Server", "Unknown")
    elapsed = round(end_time - start_time, 2)

    print(f"{GREEN}[+] Connection successful{RESET}")
    print(f"{CYAN}----------------------------------{RESET}")

    if status == 200:
        print(f"{GREEN}[STATUS] {status} OK{RESET}")
    elif status in [301, 302]:
        print(f"{YELLOW}[STATUS] {status} Redirect{RESET}")
    elif status in [401, 403]:
        print(f"{RED}[STATUS] {status} Forbidden / Unauthorized{RESET}")
    elif status == 404:
        print(f"{RED}[STATUS] {status} Not Found{RESET}")
    else:
        print(f"{YELLOW}[STATUS] {status}{RESET}")

    print(f"{CYAN}[SERVER] {server}{RESET}")
    print(f"{CYAN}[RESPONSE TIME] {elapsed}s{RESET}")

except requests.exceptions.RequestException as e:
    print(f"{RED}[-] Request failed:{RESET}", e)

print(f"\n{MAGENTA}😈 Web recon complete. Stay stealthy.{RESET}")
