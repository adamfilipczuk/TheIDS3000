from pygtail import Pygtail
import os

file_to_watch = "eve.json"
watch_dir = os.path.abspath(
    os.path.join("..", "..", "..", "suricata-tcpreplay", "suricata")
)
full_path = os.path.join(watch_dir, file_to_watch)

while True:
    for line in Pygtail(full_path):
        print(f"{file_to_watch} updated: {line}")
        # Filter and Insert call to crewAI to action. 

