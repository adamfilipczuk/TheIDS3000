import socket
import queue
# #standalone is for print statements that are useful when running this file alone

# method for adding lines of data to a queue
data_queue = queue.Queue()

# server info
HOST = "127.0.0.1"
PORT = 65432
DELAY = 5  # seconds of inactivity before sending data
LOOPS = 3  # number of loops to try to connect before dropping data
RETRIES = 5  # number of retries per loop

def recv_all(conn, buffer_size=4096):
    data= b""
    conn.settimeout(0.5)  # Set a timeout for blocking socket operations
    while True:
        try:
            chunk = conn.recv(buffer_size)
            if not chunk:
                break
            data += chunk
            if len(chunk) < buffer_size:
                break
        except socket.timeout:
            break
        return data
    
def socket_listener():
    global data_queue
    tries = 0
    loop = 0
    port = PORT
    while loop < LOOPS:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.bind((HOST, port))
                s.listen()
                while True:
                    conn, addr = s.accept()
                    with conn:
                        print(f"Connected by {addr}")
                        data = recv_all(conn)  # calls function to receive all data dynamically
                        if data:
                            # commented out this printing as it shows in crewai run
                            #print(f"[NEW DATA] {data.decode('utf-8')}")
                            print(list(data_queue.queue))
                            for line in data.decode('utf-8').splitlines():
                                if line.strip():
                                    data_queue.put(line.strip())
            except OSError as e:
                if e.errno == 10048:
                    port += 1
                    print(f"Port {port-1} in use, trying port {port}...")#standalone
                    if tries >= RETRIES:
                        print(f"Port {PORT} in use, retrying in {DELAY} seconds... (loop {loop+1}/{LOOPS})")#standalone
                        tries = 0
                        loop += 1
                        port = PORT
