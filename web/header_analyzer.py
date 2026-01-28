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

# Banner
print(f"""{MAGENTA}
██╗  ██╗███████╗ █████╗ ██████╗ ███████╗██████╗ 
██║  ██║██╔════╝██╔══██╗██╔══██╗██╔════╝██╔══██╗
███████║█████╗  ███████║██║  ██║█████╗  ██████╔╝
██╔══██║██╔══╝  ██╔══██║██║  ██║██╔══╝  ██╔══██╗
██║  ██║███████╗██║  ██║██████╔╝███████╗██║  ██║
╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝

     J I L S   R O Y   —   C Y B E R   T O O L S
{RESET}""")

print(f"{CYAN}🔥 Tool #010 — HTTP Header Security Analyzer 🔥{RESET}\n")

url = input(f"{YELLOW}Enter website URL (e.g. https://example.com): {RESET}")

if not url.startswith("http"):
    url = "https://" + url

print(f"\n{BLUE}[+] Connecting to target...{RESET}")

try:
    start = time.time()
    r = requests.get(url, timeout=8)
    end = time.time()

    print(f"{GREEN}[+] Connection successful{RESET}")
    print(f"{CYAN}[STATUS] {r.status_code} OK{RESET}")
    print(f"{CYAN}[RESPONSE TIME] {round(end-start,2)}s{RESET}")

    headers = r.headers

    print(f"\n{MAGENTA}--- Security Header Report ---{RESET}")

    security_headers = {
        "Content-Security-Policy": "Protects against XSS",
        "Strict-Transport-Security": "Forces HTTPS",
        "X-Frame-Options": "Prevents clickjacking",
        "X-Content-Type-Options": "Stops MIME sniffing",
        "Referrer-Policy": "Controls referrer leaks",
        "Permissions-Policy": "Restricts browser features"
    }

    for h, meaning in security_headers.items():
        if h in headers:
            print(f"{GREEN}[✔ PRESENT]{RESET} {h}")
        else:
            print(f"{RED}[✘ MISSING]{RESET} {h}  {YELLOW}→ {meaning}{RESET}")

    print(f"\n{MAGENTA}----------------------------------{RESET}")
    print(f"{CYAN}😈 Header analysis complete. Stay secure.{RESET}")

except requests.exceptions.RequestException:
    print(f"{RED}[-] Could not connect to target.{RESET}")
