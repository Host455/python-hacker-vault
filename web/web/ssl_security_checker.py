import ssl
import socket
from datetime import datetime

# Colors
GREEN = "\033[92m"
RED = "\033[91m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
MAGENTA = "\033[95m"
RESET = "\033[0m"

# Banner
print(f"""{MAGENTA}
███████╗███████╗██╗     ███████╗
██╔════╝██╔════╝██║     ██╔════╝
███████╗███████╗██║     █████╗  
╚════██║╚════██║██║     ██╔══╝  
███████║███████║███████╗███████╗
╚══════╝╚══════╝╚══════╝╚══════╝

     J I L S   R O Y   —   C Y B E R   T O O L S
{RESET}""")

print(f"{CYAN}🔥 Tool #012 — SSL/TLS Security Checker 🔥{RESET}\n")

# Input
domain = input(f"{YELLOW}Enter domain (example.com): {RESET}")

# Remove https:// if user enters it
domain = domain.replace("https://", "").replace("http://", "").strip()

print(f"\n{CYAN}[+] Connecting to SSL server...{RESET}")

try:
    # Create SSL context
    context = ssl.create_default_context()

    # Connect socket
    with socket.create_connection((domain, 443), timeout=5) as sock:
        with context.wrap_socket(sock, server_hostname=domain) as ssock:

            cert = ssock.getpeercert()
            tls_version = ssock.version()

            print(f"{GREEN}[+] SSL Connection Successful!{RESET}")
            print(f"{CYAN}[TLS VERSION] {tls_version}{RESET}")

            # Certificate Info
            subject = dict(x[0] for x in cert["subject"])
            issuer = dict(x[0] for x in cert["issuer"])

            issued_to = subject.get("commonName", "Unknown")
            issued_by = issuer.get("commonName", "Unknown")

            print(f"\n{MAGENTA}--- Certificate Info ---{RESET}")
            print(f"{GREEN}[ISSUED TO] {issued_to}{RESET}")
            print(f"{GREEN}[ISSUED BY] {issued_by}{RESET}")

            # Expiry Date
            expiry_date = cert["notAfter"]
            expiry_datetime = datetime.strptime(expiry_date, "%b %d %H:%M:%S %Y %Z")

            days_left = (expiry_datetime - datetime.utcnow()).days

            print(f"\n{MAGENTA}--- Expiry Report ---{RESET}")
            print(f"{CYAN}[EXPIRY DATE] {expiry_datetime}{RESET}")

            if days_left > 30:
                print(f"{GREEN}[SAFE] Certificate valid for {days_left} more days{RESET}")
            elif days_left > 0:
                print(f"{YELLOW}[WARNING] Certificate expires soon ({days_left} days left){RESET}")
            else:
                print(f"{RED}[DANGER] Certificate already expired!{RESET}")

            print(f"\n{MAGENTA}😈 SSL Recon Complete. Stay secure.{RESET}")

except Exception as e:
    print(f"{RED}[-] SSL Connection Failed!{RESET}")
    print(f"{RED}Reason: {e}{RESET}")
