import psutil
import socket

def networkinfo():
    print("=== Active Network Interfaces ===")
    interfaces = psutil.net_if_addrs()
    for interface in interfaces:
        addresses = interfaces[interface]
        print(f"\nInterface: {interface}")
        for addr in addresses:
            if addr.family == socket.AF_INET:
                print(f"  IP Address: {addr.address}")
            elif addr.family == socket.AF_PACKET:
                print(f"  MAC Address: {addr.address}")

    print("\n=== Current Network Connections ===")
    connections = psutil.net_connections()
    for conn in connections:
        laddr = f"{conn.laddr.ip}:{conn.laddr.port}" if conn.laddr else "N/A"
        raddr = f"{conn.raddr.ip}:{conn.raddr.port}" if conn.raddr else "N/A"
        status = conn.status
        pid = conn.pid

        print(f"Local: {laddr}  ->  Remote: {raddr}  | Status: {status} | PID: {pid}")
