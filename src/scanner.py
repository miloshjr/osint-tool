import dns.resolver
import whois
import nmap
import socket
import sys
from reporter import generate_report
print(">>> PYTHON PATH:", sys.executable)

def scan_dns(domain):
    print(f"[DNS] Skanuję: {domain}")
    results = {}
    record_types = ["A", "MX", "NS", "TXT"]

    for rtype in record_types:
        try:
            answers = dns.resolver.resolve(domain, rtype)
            results[rtype] = [r.to_text() for r in answers]
        except Exception as e:
            results[rtype] = [f"Brak ({str(e)})"]

    return results


def scan_whois(domain):
    print(f"[WHOIS] Skanuję: {domain}")
    try:
        w = whois.whois(domain)
        return {
            "domain_name": w.domain_name,
            "registrar": w.registrar,
            "creation_date": str(w.creation_date),
            "expiration_date": str(w.expiration_date),
            "name_servers": w.name_servers
        }
    except Exception as e:
        return {"error": str(e)}


def scan_ports(ip):
    print(f"[NMAP] Skanuję porty IP: {ip}")
    try:
        nm = nmap.PortScanner()
        nm.scan(ip, arguments='-Pn -T4')
        ports = {}
        for proto in nm[ip].all_protocols():
            for port in nm[ip][proto]:
                state = nm[ip][proto][port]['state']
                ports[f"{proto.upper()} {port}"] = state
        return ports
    except Exception as e:
        return {"error": str(e)}


def main(domain):
    try:
        ip = socket.gethostbyname(domain)
    except Exception as e:
        ip = domain
        print(f"[WARN] Nie mogę rozwiązać IP: {e}")

    dns_info = scan_dns(domain)
    whois_info = scan_whois(domain)
    port_info = scan_ports(ip)

    return {
        "dns": dns_info,
        "whois": whois_info,
        "ports": port_info
    }


if __name__ == "__main__":
    domain = "onet.pl"  # ← Tu wpisz co chcesz
    result = main(domain)

    print("\n=== WYNIK ===")
    for section, content in result.items():
        print(f"\n--- {section.upper()} ---")
        for k, v in content.items():
            print(f"{k}: {v}")
