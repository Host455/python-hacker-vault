import requests
from urllib.parse import urljoin

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
██████╗  ██████╗ ██████╗  ██████╗ ████████╗███████╗
██╔══██╗██╔═══██╗██╔══██╗██╔═══██╗╚══██╔══╝██╔════╝
██████╔╝██║   ██║██████╔╝██║   ██║   ██║   ███████╗
██╔═══╝ ██║   ██║██╔══██╗██║   ██║   ██║   ╚════██║
██║     ╚██████╔╝██║  ██║╚██████╔╝   ██║   ███████║
╚═╝      ╚═════╝ ╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚══════╝

     J I L S   R O Y   —   C Y B E R   T O O L S
{RESET}""")

print(f"{CYAN}🔥 Tool #011 — Robots.txt + Sitemap Finder 🔥{RESET}\n")

target = input(f"{YELLOW}Enter website URL (e.g. https://example.com): {RESET}")

if not target.startswith("http"):
    target = "https://" + target

robots_url = urljoin(target, "/robots.txt")
sitemap_url = urljoin(target, "/sitemap.xml")

# -------------------------------
# Fetch Robots.txt
# -------------------------------
print(f"\n{BLUE}[+] Checking robots.txt...{RESET}")

try:
    r = requests.get(robots_url, timeout=6)

    if r.status_code == 200:
        print(f"{GREEN}[FOUND] robots.txt available!{RESET}")
        print(f"{CYAN}URL → {robots_url}{RESET}\n")

        lines = r.text.splitlines()

        print(f"{MAGENTA}--- Disallowed Paths ---{RESET}")

        for line in lines:
            if line.lower().startswith("disallow"):
                print(f"{YELLOW}{line}{RESET}")

    else:
        print(f"{RED}[-] robots.txt not found (Status: {r.status_code}){RESET}")

except requests.exceptions.RequestException:
    print(f"{RED}[-] Error fetching robots.txt{RESET}")

# -------------------------------
# Fetch Sitemap.xml
# -------------------------------
print(f"\n{BLUE}[+] Checking sitemap.xml...{RESET}")

try:
    r = requests.get(sitemap_url, timeout=6)

    if r.status_code == 200:
        print(f"{GREEN}[FOUND] sitemap.xml available!{RESET}")
        print(f"{CYAN}URL → {sitemap_url}{RESET}\n")

        # Show first few URLs
        urls = []
        for line in r.text.splitlines():
            if "<loc>" in line:
                clean = line.strip().replace("<loc>", "").replace("</loc>", "")
                urls.append(clean)

        print(f"{MAGENTA}--- Sitemap URLs (Top 10) ---{RESET}")
        for u in urls[:10]:
            print(f"{CYAN}{u}{RESET}")

        print(f"\n{CYAN}[+] Total URLs found: {len(urls)}{RESET}")

    else:
        print(f"{RED}[-] sitemap.xml not found (Status: {r.status_code}){RESET}")

except requests.exceptions.RequestException:
    print(f"{RED}[-] Error fetching sitemap.xml{RESET}")

print(f"\n{MAGENTA}😈 Recon complete. Hidden paths discovered.{RESET}")
