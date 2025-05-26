import socket
import whois
import requests
from bs4 import BeautifulSoup
def passive_dns_lookup(domain):
    print(f"[+] Performing DNS Lookup for {domain}")
    try:
        ip = socket.gethostbyname(domain)
        print(f"[+] IP Address: {ip}")
        return ip
    except socket.gaierror:
        print("[-] DNS resolution failed.")
        return None

def whois_lookup(domain):
    print(f"\n[+] Performing WHOIS Lookup for {domain}")
    try:
        w = whois.whois(domain)
        print(f"[+] Domain Registrar: {w.registrar}")
        print(f"[+] Domain Creation Date: {w.creation_date}")
        print(f"[+] Domain Expiration Date: {w.expiration_date}")
        print(f"[+] Name Servers: {w.name_servers}")
    except Exception as e:
        print("[-] WHOIS lookup failed:", e)

def web_scrape_data(url):
    print(f"\n[+] Scraping data from: {url}")
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')

        print("[+] Extracted Title:", soup.title.string.strip())

        print("\n[+] Extracted Meta Description:")
        meta_desc = soup.find("meta", attrs={"name": "description"})
        if meta_desc:
            print(meta_desc.get("content"))
        else:
            print("No meta description found.")

        print("\n[+] Links on the page:")
        links = soup.find_all('a', href=True)
        for link in links[:5]:  # Display first 5 links
            print(link['href'])

    except Exception as e:
        print("[-] Web scraping failed:", e)

def osint_script(target):
    print(f"\n=== OSINT Gathering for: {target} ===")
    ip = passive_dns_lookup(target)
    whois_lookup(target)
    web_scrape_data(f"http://{target}")

# Example usage
if __name__ == "__main__":
    target_domain = input("Enter target domain (e.g. example.com): ")
    osint_script(target_domain)
