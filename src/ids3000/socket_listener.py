import socket
import queue

# method for adding lines of data to a queue
data_queue = queue.Queue()

# server info
HOST = "127.0.0.1"
PORT = 65432

def socket_listener():
    global data_queue
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        while True:
            conn, addr = s.accept()
            with conn:
                print(f"Connected by {addr}")
                data = conn.recv(65432)
                if data:
                    # commented out this printing as it shows in crewai run
                    # print(f"[NEW DATA] {data.decode('utf-8')}")

                    data_queue.put(data.decode('utf-8'))
