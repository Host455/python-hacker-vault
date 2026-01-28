#!/usr/bin/env python3
"""
Tool #0XX - IP Info Lookup (Defensive)

Purpose:
- Shows basic public information about an IP address
- Useful for SOC, threat intel, and defensive recon

Legal Use Only:
- Do NOT use for stalking, harassment, or illegal tracking
"""

import requests

BANNER = r"""
=========================================
      IP Info Lookup Tool (Defensive)
          Author: Jils 😈
=========================================
"""

def lookup_ip(ip):
    url = f"http://ip-api.com/json/{ip}"

    try:
        response = requests.get(url, timeout=10)
        data = response.json()

        if data["status"] != "success":
            print("[-] Lookup failed!")
            return

        print("\n[+] IP Information Report")
        print("-----------------------------------------")
        print(f"IP Address   : {data.get('query')}")
        print(f"Country      : {data.get('country')}")
        print(f"Region       : {data.get('regionName')}")
        print(f"City         : {data.get('city')}")
        print(f"ISP          : {data.get('isp')}")
        print(f"Organization : {data.get('org')}")
        print(f"ASN          : {data.get('as')}")
        print("-----------------------------------------")

        print("\n[!] Note: Location is approximate, not exact.")
        print("[!] This tool is for defensive use only.\n")

    except Exception as e:
        print("[-] Error:", e)

def main():
    print(BANNER)

    ip = input("Enter IP address to lookup: ").strip()

    if not ip:
        print("[-] No IP entered.")
        return

    lookup_ip(ip)

if __name__ == "__main__":
    main()
