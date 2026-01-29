import requests
import time

# Colors
GREEN = "\033[92m"
RED = "\033[91m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
MAGENTA = "\033[95m"
RESET = "\033[0m"

# Banner
print(f"""{MAGENTA}
███████╗██╗███╗   ██╗ ██████╗ ███████╗██████╗ 
██╔════╝██║████╗  ██║██╔════╝ ██╔════╝██╔══██╗
█████╗  ██║██╔██╗ ██║██║  ███╗█████╗  ██████╔╝
██╔══╝  ██║██║╚██╗██║██║   ██║██╔══╝  ██╔══██╗
██║     ██║██║ ╚████║╚██████╔╝███████╗██║  ██║
╚═╝     ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝

     J I L S   R O Y — CYBER TOOLS
{RESET}""")

print(f"{CYAN}🔥 Tool #015 — Web Server Fingerprinter 🔥{RESET}\n")

# Input
url = input(f"{YELLOW}Enter website URL (https://example.com): {RESET}")

if not url.startswith("http"):
    url = "https://" + url

print(f"\n{CYAN}[+] Sending request...{RESET}")

try:
    start = time.time()
    r = requests.get(url, timeout=6)
    end = time.time()

    response_time = round(end - start, 2)

    print(f"{GREEN}[+] Connection Successful!{RESET}")
    print(f"{CYAN}[STATUS] {r.status_code}{RESET}")
    print(f"{CYAN}[RESPONSE TIME] {response_time}s{RESET}")

    print(f"\n{MAGENTA}--- Fingerprint Report ---{RESET}")

    # Server Header
    server = r.headers.get("Server", "Unknown")
    print(f"{GREEN}[SERVER] {server}{RESET}")

    # Powered By Header
    powered = r.headers.get("X-Powered-By", "Not disclosed")
    print(f"{GREEN}[X-POWERED-BY] {powered}{RESET}")

    # Cloudflare Detection
    if "cloudflare" in server.lower() or "cf-ray" in r.headers:
        print(f"{YELLOW}[CLOUDFLARE] Protection Detected{RESET}")
    else:
        print(f"{CYAN}[CLOUDFLARE] Not Detected{RESET}")

    # Interesting Headers
    print(f"\n{MAGENTA}--- Interesting Headers ---{RESET}")

    interesting = [
        "Content-Type",
        "Strict-Transport-Security",
        "Content-Security-Policy",
        "Set-Cookie"
    ]

    for h in interesting:
        if h in r.headers:
            print(f"{GREEN}[{h}] {r.headers[h]}{RESET}")
        else:
            print(f"{RED}[MISSING] {h}{RESET}")

    print(f"\n{MAGENTA}😈 Fingerprinting Complete. Stay ethical.{RESET}")

except Exception as e:
    print(f"{RED}[-] Request Failed!{RESET}")
    print(f"{RED}Reason: {e}{RESET}")
