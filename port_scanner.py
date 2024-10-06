import requests
import socket
import time
import http
import threading
import pyfiglet
from colorama import Fore, Style




# ascii banner
ascii_banner = pyfiglet.figlet_format("Cyberlock Hacker")
print(Fore.LIGHTCYAN_EX + ascii_banner)
print("Author: @C9b3rD3vi1")
print("Version: 1.0.0")
print("Description: Simple python port scanner using multithreading and requests")
print(" ")



# port scanner for requests, for port scannings and banner grabbing

def port_scanner(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        sock.connect((ip, port))

        print(f"{Fore.GREEN} {port} on {ip} is open")
    
    except socket.error:
        print(f"{Fore.RED} {port} on {ip} is closed")



# Create main function
def main_start():

    start_time = time.time()
    print(f"{Fore.YELLOW} Current time: {time.ctime()}")
    print("\n")
    ip = input(" [~] Enter a target ip address :")
    port = input(" [~] Enter port to connect :")
    port_range = port.split(":")
    start_port = int(port_range[0])
    end_port = int(port_range[1])

    print(" \n")
    
    
    print (f"{Fore.BLUE} Starting Port Scanning................")
    print(f"{Fore.BLUE} Scanning ports {start_port} to {end_port}")
    print(f"{Fore.BLUE} Press Ctrl+C to stop scanning")
    print(" ")


    # Create a new thread for each port to scan
    for port in range(start_port, end_port + 1):
        t = threading.Thread(target=port_scanner, args=(ip, port))
        t.start()
        time.sleep(0.1)
    

    # Wait for all threads to finish
    for t in threading.enumerate():
        if t is not threading.main_thread():
            t.join()
    
    end_time = time.time()
    print(f"Scan completed in {end_time - start_time} seconds")


if __name__ == "__main__":
    main_start()