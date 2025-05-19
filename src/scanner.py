# src/scanner.py

import argparse
import shodan
from src.reporter import generate_report
from src.config import SHODAN_API_KEY

def scan_target(target):
    api = shodan.Shodan(SHODAN_API_KEY)
    try:
        host = api.host(target)
    except shodan.exception.APIError as e:
        return f"Błąd zapytania do Shodan: {str(e)}"
    
    return generate_report(host)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="OSINT Vuln Scanner")
    parser.add_argument("--target", required=True, help="IP lub domena do przeskanowania")
    args = parser.parse_args()

    output = scan_target(args.target)
    print(output)
