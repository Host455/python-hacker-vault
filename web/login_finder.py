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

# Cyberpunk Banner
print(f"""{MAGENTA}
██╗      ██████╗  ██████╗ ██╗███╗   ██╗
██║     ██╔═══██╗██╔════╝ ██║████╗  ██║
██║     ██║   ██║██║  ███╗██║██╔██╗ ██║
██║     ██║   ██║██║   ██║██║██║╚██╗██║
███████╗╚██████╔╝╚██████╔╝██║██║ ╚████║
╚══════╝ ╚═════╝  ╚═════╝ ╚═╝╚═╝  ╚═══╝

     J I L S   R O Y   —   C Y B E R   T O O L S
{RESET}""")

print(f"{CYAN}🔥 Tool #006 — Login Page Detector 🔥{RESET}\n")

base_url = input(f"{YELLOW}Enter target URL (e.g. https://example.com): {RESET}")

if not base_url.startswith("http"):
    base_url = "http://" + base_url

login_paths = [
    "login", "admin", "wp-login.php", "signin",
    "account", "user/login", "panel", "dashboard"
]

print(f"\n{BLUE}[+] Initializing login page scan...{RESET}")
start_time = time.time()

found = []

headers = {
    "User-Agent": "CyberRecon/1.0"
}

for path in login_paths:
    url = f"{base_url.rstrip('/')}/{path}"
    try:
        r = requests.get(url, timeout=5, allow_redirects=False, headers=headers)
        status = r.status_code

        if status in [200, 301, 302, 401, 403]:
            print(f"{GREEN}[FOUND] {url} ({status}){RESET}")
            found.append((url, status))
        else:
            print(f"{CYAN}[MISS] {url} ({status}){RESET}")

    except requests.exceptions.RequestException:
        print(f"{RED}[-] Error connecting to {url}{RESET}")

elapsed = round(time.time() - start_time, 2)

print(f"\n{MAGENTA}----------------------------------{RESET}")
print(f"{GREEN}[+] Scan complete{RESET}")
print(f"{CYAN}[+] Time taken: {elapsed}s{RESET}")
print(f"{CYAN}[+] Login paths found: {len(found)}{RESET}")

# Fingerprinting headers
print(f"\n{BLUE}[+] Fingerprinting server...{RESET}")
try:
    r = requests.get(base_url, timeout=5, headers=headers)
    server = r.headers.get("Server", "Unknown")
    powered = r.headers.get("X-Powered-By", "Not disclosed")

    print(f"{GREEN}[SERVER] {server}{RESET}")
    print(f"{GREEN}[X-POWERED-BY] {powered}{RESET}")

    text = r.text.lower()

    if "wp-content" in text:
        print(f"{YELLOW}[CMS] WordPress detected{RESET}")
    elif "laravel" in text:
        print(f"{YELLOW}[CMS] Laravel detected{RESET}")
    elif "django" in text:
        print(f"{YELLOW}[CMS] Django detected{RESET}")
    elif "react" in text:
        print(f"{YELLOW}[FRONTEND] React detected{RESET}")
    elif "angular" in text:
        print(f"{YELLOW}[FRONTEND] Angular detected{RESET}")
    else:
        print(f"{CYAN}[CMS] Could not detect CMS{RESET}")

except requests.exceptions.RequestException:
    print(f"{RED}[-] Could not fingerprint server{RESET}")

print(f"\n{MAGENTA}😈 Login recon complete. Stay stealthy.{RESET}")
