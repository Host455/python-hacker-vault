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
██████╗ ██╗██████╗ ██████╗ 
██╔══██╗██║██╔══██╗██╔══██╗
██║  ██║██║██████╔╝██████╔╝
██║  ██║██║██╔═══╝ ██╔═══╝ 
██████╔╝██║██║     ██║     
╚═════╝ ╚═╝╚═╝     ╚═╝     

   J I L S   R O Y   —   C Y B E R   T O O L S
{RESET}""")

print(f"{CYAN}🔥 Tool #005 — Directory Bruteforcer 🔥{RESET}\n")

base_url = input(f"{YELLOW}Enter target URL (e.g. https://example.com): {RESET}")

if not base_url.startswith("http"):
    base_url = "http://" + base_url

# Small built-in wordlist
wordlist = [
    "admin", "login", "dashboard", "backup", "uploads",
    "config", "test", "old", "dev", "private",
    "server-status", ".git", ".env"
]

print(f"\n{BLUE}[+] Initializing directory scan...{RESET}")
start_time = time.time()

found = []

for word in wordlist:
    url = f"{base_url.rstrip('/')}/{word}"
    try:
        r = requests.get(url, timeout=5, allow_redirects=False)
        status = r.status_code

        if status == 200:
            print(f"{GREEN}[FOUND] {url} (200 OK){RESET}")
            found.append((url, status))

        elif status in [301, 302]:
            print(f"{YELLOW}[REDIRECT] {url} ({status}){RESET}")
            found.append((url, status))

        elif status == 403:
            print(f"{RED}[FORBIDDEN] {url} (403){RESET}")
            found.append((url, status))

        else:
            print(f"{CYAN}[MISS] {url} ({status}){RESET}")

    except requests.exceptions.RequestException:
        print(f"{RED}[-] Error connecting to {url}{RESET}")

elapsed = round(time.time() - start_time, 2)

print(f"\n{MAGENTA}----------------------------------{RESET}")
print(f"{GREEN}[+] Scan complete{RESET}")
print(f"{CYAN}[+] Time taken: {elapsed}s{RESET}")
print(f"{CYAN}[+] Paths found: {len(found)}{RESET}")

if found:
    print(f"\n{GREEN}[+] Interesting paths:{RESET}")
    for item in found:
        print(f"{CYAN}{item[0]} → {item[1]}{RESET}")

print(f"\n{MAGENTA}😈 Directory recon complete. Stay stealthy.{RESET}")
