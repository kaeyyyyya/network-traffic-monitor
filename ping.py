import subprocess
import ipaddress
def ping():
    hostname=input("whats ur hostname or ip:").strip()
    request=int(input("how many request u gonna ask for"))
    try:
        ipaddress.ip_address(hostname)
    except ValueError:
        print("ip adress not valid")
    subprocess.call(["ping",hostname, "-c" , str(request)])


