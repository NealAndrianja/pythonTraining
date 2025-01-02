import socket

def scan_port(host, port):
    """

    :param host:
    :param port:
    :return:
    """
    try:
        sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result=sock.connect_ex((host,port))
        sock.close()
        return result==0
    except Exception as e:
        return False

def main():
    host=input("Enter the host to scan (e.g. 127.0.0.1): ")
    start_port=int(input("Enter the starting port: "))
    end_port=int(input("Enter the ending port: "))

    print(f"Scanning ports {start_port}-{end_port} on host {host}...")
    for port in range(start_port, end_port+1):
        if scan_port(host,port):
            print(f"Port {port} is open")
        else:
            print(f"Port {port} is closed")

if __name__ == '__main__':
    main()