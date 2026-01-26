import socket
import os
from datetime import datetime

print("🔥 Tool #001 — Target Info Recon 🔥")

target = input("Enter target IP or domain: ")

print("\n[+] Time:", datetime.now())
print("[+] Resolving hostname...")

try:
    ip = socket.gethostbyname(target)
    print("[+] IP Address:", ip)
except:
    print("[-] Could not resolve target")
    exit()

print("\n[+] Pinging target...")
os.system("ping -c 3 " + ip)

print("\n[+] Basic Recon Complete 😈")
    
