import socket
import nmap
import whois
import dns.resolver

def scan_ports(target):
    nm = nmap.PortScanner()
    try:
        nm.scan(target, arguments='-sS -Pn')
        ports = []
        for host in nm.all_hosts():
            for proto in nm[host].all_protocols():
                lport = nm[host][proto].keys()
                for port in lport:
                    state = nm[host][proto][port]['state']
                    ports.append(f"{port}/{proto} - {state}")
        return ports
    except Exception as e:
        return [f"Port scan error: {str(e)}"]

def get_whois(target):
    try:
        w = whois.whois(target)
        return w.text if hasattr(w, "text") else str(w)
    except Exception as e:
        return f"WHOIS error: {str(e)}"

def get_dns_records(domain):
    records = {}
    try:
        for rtype in ['A', 'AAAA', 'MX', 'NS', 'TXT']:
            answers = dns.resolver.resolve(domain, rtype, raise_on_no_answer=False)
            records[rtype] = [r.to_text() for r in answers] if answers else []
    except Exception as e:
        records['error'] = f"DNS error: {str(e)}"
    return records

def scan(target):
    result = {}
    # Resolve IP
    try:
        ip = socket.gethostbyname(target)
        result['IP'] = ip
    except Exception as e:
        result['IP'] = f"Could not resolve IP: {str(e)}"

    result['Ports'] = scan_ports(target)
    result['WHOIS'] = get_whois(target)
    result['DNS'] = get_dns_records(target)
    return result
