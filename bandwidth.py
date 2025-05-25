import psutil
import time
def bandwidth():
    print(" Surveillance de la bande passante (Ctrl+C pour quitter)")

    old_value = psutil.net_io_counters()
    time.sleep(1)

    while True:
        new_value = psutil.net_io_counters()
        download_speed = (new_value.bytes_recv - old_value.bytes_recv) / 1024  
        upload_speed = (new_value.bytes_sent - old_value.bytes_sent) / 1024

        print(f"⬇{download_speed:.2f} KB/s  |  ⬆{upload_speed:.2f} KB/s")
        old_value = new_value
        time.sleep(1)
