import time
import threading
import os
import socket
from pygtail import Pygtail
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
#needs to be changed to a work with a config file later

#polling only as windows & mac does some werid caching that makes watchdog not work
# comments marked with #standalone are for when this is used as a standalone script

buffer = []
last_append_time = 0
appends = 0
lock = threading.Lock()
port = 65432

HOST = "127.0.0.1"
PORT = 65432
CHUNK_SIZE = 5  # Number of lines to send in one chunk
DATA_SEND_DELAY = 5  # seconds of inactivity before sending data

class file_watcher:
    def __init__(self, target_file): #ensuring only to watch the specified file
        self.target_file = os.path.abspath(target_file)

    def watch(self):
        global appends, last_append_time
        while True:
            time.sleep(1)  # Sleep to avoid busy waiting
            with lock:
                for line in Pygtail(self.target_file): #should include a first run check to avoid reading the whole file
                    clean_line = line.rstrip("\n")
                    if clean_line:  # avoid adding empty lines
                        buffer.append(clean_line)
                        appends += 1 #dont want to send too 
                        last_append_time = time.time()

class socket_sender:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def send_data(self, data, retries = 5, delay = 5): #delay in seconds, server should have a slower delay so that it can catch up
        attempts = 0
        loops = 0
        while attempts < retries and loops < retries:
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.connect((self.host, self.port)) 
                    s.sendall(("|".join(data) + "\n").encode("utf-8"))
                    #print("Data sent successfully") #standalone
                    break  # Exit the loop if successful
            except Exception as e:
                print(f"Error sending data on port {self.port}: retrying in {delay} seconds...") #standalone
                attempts += 1
                self.port += 1
                time.sleep(delay)
                if attempts >= retries:
                    print("No response across ports, looping back to first port") #standalone
                    loops += 1
                    attempts = 0
                    self.port = PORT
                if loops >= retries:
                    print("Max retries reached, dropping data")#standalone
                    break
            
def process_buffer():
    global buffer
    global appends
    data_to_process = None
    while True:
        time.sleep(0.1)
        now = time.time()
        with lock:
            if (buffer and (now - last_append_time) > DATA_SEND_DELAY) or (appends >= CHUNK_SIZE):
                data_to_process = buffer[:] # stops working with global varaible
                buffer.clear()    # clear the buffer
                appends = 0

        if data_to_process:
            #print(data_to_process)#debug

            while len(data_to_process) >= CHUNK_SIZE:
                chunk = data_to_process[:CHUNK_SIZE] #grab a chunk
                data_to_process = data_to_process[CHUNK_SIZE:]#remove the chunk that will be sent

                #print("Sending data") #standalone
                send_data = socket_sender(HOST, PORT)
                send_data.send_data(chunk)

            if data_to_process: #remaining data is imporant so half wait time
                chunk = data_to_process[:]  # take all remaining lines
                print("Sending remaining data") #standalone
                send_data = socket_sender(HOST, PORT)
                send_data.send_data(chunk)
                data_to_process = None  # clear after sending

            if not data_to_process:
                data_to_process = None
            
def alert_tracker():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    watch_path = os.path.abspath(os.path.join(script_dir, "..", "..", "suricata-tcpreplay", "suricata", "eve.json"))

    if not os.path.isfile(watch_path):
        os.makedirs(os.path.dirname(watch_path), exist_ok=True)
        open(watch_path, 'a').close()  # create the file if it doesn't exist
        print(f"Created missing file at {watch_path}, ensure Suricata is configured to write to this path.") #standalone

    threading.Thread(target=process_buffer, daemon=True).start() #starting a thread to process the buffer in background
    fw = file_watcher(watch_path)
    fw.watch()

# Controls standalone output
if __name__ == "__main__":
    try:
        start_alert_tracker()
    except KeyboardInterrupt:
        print("stopping")
