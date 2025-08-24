import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os


#needs to be changed to a work with a config file later

class LoggingEventHandler(FileSystemEventHandler):
    def __init__(self, target_file):
        self.target_file = os.path.abspath(target_file)

    def on_created(self, event):
        if not event.is_directory and os.path.abspath(event.src_path) == self.target_file:
            print(f"File created: {event.src_path}")

    def on_modified(self, event):
        if not event.is_directory and os.path.abspath(event.src_path) == self.target_file:
            print(f"File modified: {event.src_path}")


if __name__ == "__main__":
    path = "D:\Suricata\log\eve.json"  # Path to the log file
    event_handler = LoggingEventHandler(path)
    observer = Observer()
    observer.schedule(event_handler, os.path.dirname(path) or ".", recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)  # Sleep to avoid busy waiting
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

#https://python-watchdog.readthedocs.io/en/stable/api.html