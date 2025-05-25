import socket
def scanner():
    host = input("Entrez une adresse IP ou un nom d'hôte : ").strip()
    start_port = int(input("Port de début : "))
    end_port = int(input("Port de fin : "))
    print(f"\n Scan des ports de {host} ({start_port} à {end_port})...\n")
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)  
        result = sock.connect_ex((host, port)) 
        if result == 0:
            print(f"Port {port} ouvert")
        sock.close()

