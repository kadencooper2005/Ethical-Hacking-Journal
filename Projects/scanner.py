import socket
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed


def scan_port(host_ip, port, timeout=0.5):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            s.connect((host_ip, port))
            return port, True
    except:
        return port, False


def parse_range(r):
    if '-' in r:
        a, b = r.split('-', 1)
        return int(a), int(b)
    n = int(r)
    return n, n

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usuage: python3 test.py <host> <port|start-end> [workers]")
        sys.exit(1)
    
    host = sys.argv(1)
    port_arg = sys.argv[2]
    max_workers = int(sys.argv[3]) if len(sys.argv) > 3 else 200

    # Error catching incase the domain is unknown
    try:
        ip = socket.gethostbyname(host)
    except socket.gaierror:
        print("Could not resolve host.")
        sys.exit(1)

    start, end = parse_range(port_arg)
    start = max(1, start)
    end = min(65535, end)

    print(f"Scanning {host} ({ip}) ports {start}-{end} with {max_workers} workers...") 

    open_ports = []
    with ThreadPoolExecutor(max_workers=max_workers) as exe:
        futures = {exe.submit(scan_port, ip, p): p for p in range(start, end + 1)}
        for f in as_completed(futures):
            port, is_open = f.result()
            if is_open:
                print(f"[OPEN] {port}/tcp")
                open_ports.append(port)
    
    print("Scan complete Open ports:", sorted(open_ports))