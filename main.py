import ping
import portScanner
import bandwidth
import network_info
def main():
    while True:
        print("\n=== network traffic monitor===")
        print("1. Afficher les interfaces réseau")
        print("2. Ping un hôte")
        print("3. Scanner des ports")
        print("4. Surveiller la bande passante")
        print("0. Quitter")
        choice = input("Choix : ")
        if choice == "1":
            network_info.networkinfo()
        elif choice == "2":
            ping.ping()
        elif choice == "3":
            portScanner.scanner()
        elif choice == "4":
            bandwidth.bandwidth()
        elif choice == "0":
            print("...")
            break
        else:
            print("Choix invalide.")
main()