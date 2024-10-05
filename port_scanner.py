import requests
import socket
import time
import http
import threading



# port scanner for requests, for port scannings and banner grabbing

def port_scanner(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        sock.connect((ip, port))
        print(f" {port} on {ip} is open")
    
    except socket.error:
        print(f" {port} on {ip} is closed")



# Create main function
def main_start():

    start_time = time.time()
    ip = input("[~] Enter a target ip address :")
    port = input(" [~] Enter port to connect :")
    port_range = port.split(":")
    start_port = int(port_range[0])
    end_port = int(port_range[1])
    
    print ("Scanning")


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