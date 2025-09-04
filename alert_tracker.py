import time
import threading
import requests
import os
from pygtail import Pygtail
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
#needs to be changed to a work with a config file later

# Watchdog monitors eve.json for changes (event-driven, no polling)
# When a change occurs, Pygtail reads only the new lines from the file.
# Without Watchdog, Pygtail would need to be called in a loop, which means
# constant polling of the file for new data.

buffer = []
last_append_time = 0
appends = 0
lock = threading.Lock()

class LoggingEventHandler(FileSystemEventHandler):
    content = []
    def __init__(self, target_file): #ensuring only to watch the specified file
        self.target_file = os.path.abspath(target_file)

    def on_modified(self, event):
        global appends, last_append_time
        if not event.is_directory and os.path.abspath(event.src_path) == self.target_file:
            print("modified") # debug
            with lock:
                for line in Pygtail(event.src_path): #should include a first run check to avoid reading the whole file
                    clean_line = line.rstrip("\n")
                    if clean_line:  # avoid adding empty lines
                        buffer.append(clean_line)
                        appends += 1 #dont want to send too 
                        last_append_time = time.time()

def process_buffer():
    global buffer
    global appends
    data_to_process = []
    while True:
        time.sleep(0.1)
        with lock:
            if (buffer and (time.time() - last_append_time) > 20) or (appends >= 20):  # 1 second of inactivity or buffer size limit
               data_to_process = "\n".join(buffer) # make a copy of the buffer and make it into a single string
               print(data_to_process)
               buffer.clear()
               appends = 0
        if data_to_process:
            print("sent data")
            requests.post("http://localhost:5000/new_data",data_to_process)#passing the new data to the server
            data_to_process = []  # clear the local copy after processing
            
if __name__ == "__main__":
    path = os.path.abspath(
    os.path.join("..", "..", "..", "suricata-tcpreplay", "suricata", "eve.json")
    )
    print(path)
    event_handler = LoggingEventHandler(path)
    observer = Observer()
    observer.schedule(event_handler, os.path.dirname(path) or ".", recursive=True)
    observer.start()

    threading.Thread(target=process_buffer, daemon=True).start() #starting a thread to process the buffer in background

    try:
        while True:
            time.sleep(1)  # Sleep to avoid busy waiting
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

#https://python-watchdog.readthedocs.io/en/stable/api.html
