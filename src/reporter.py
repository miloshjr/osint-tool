# src/reporter.py

def generate_report(host_data):
    lines = []

    lines.append(f"📍 IP: {host_data.get('ip_str')}")
    lines.append(f"🌍 Lokalizacja: {host_data.get('city')}, {host_data.get('country_name')}")
    lines.append(f"🛰️ ISP: {host_data.get('isp')}")
    lines.append(f"🧠 Organizacja: {host_data.get('org')}")
    lines.append("\n🔓 Otwarte porty i usługi:")

    for item in host_data.get('data', []):
        port = item.get("port")
        banner = item.get("product", "brak info")
        lines.append(f"  - Port {port}: {banner}")

    lines.append("\n⚠️ Wskazówki:")
    risky_ports = [23, 21, 445, 3389]
    for port in risky_ports:
        if any(p['port'] == port for p in host_data.get('data', [])):
            lines.append(f"  ❗ Port {port} jest potencjalnie niebezpieczny!")

    return "\n".join(lines)
