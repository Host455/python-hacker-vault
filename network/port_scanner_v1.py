import socket
from datetime import datetime

print("🔥 Tool #002 — Port Scanner v1 🔥")

target = input("Enter target IP: ")

try:
    target_ip = socket.gethostbyname(target)
except:
    print("[-] Invalid target")
    exit()

print("\n[+] Scanning started at:", datetime.now())
print("[+] Target:", target_ip)
print("-" * 40)

for port in range(1, 1025):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.3)
    result = s.connect_ex((target_ip, port))

    if result == 0:
        print("[OPEN] Port", port)

    s.close()

print("-" * 40)
print("[+] Scan complete at:", datetime.now())
print("😈 Done.")
