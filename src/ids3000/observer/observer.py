from pygtail import Pygtail
import os

file_to_watch = "eve.json"
watch_dir = os.path.abspath(
    os.path.join("..", "..", "..", "suricata-tcpreplay", "suricata")
)
full_path = os.path.join(watch_dir, file_to_watch)

def observer():
    while True:
        for line in Pygtail(full_path):
            return line
            