#testing tool
import socket
import time
import os
import threading

print("\nIDS3000 - Testing Tool")

class TestTools:
    def __init__(self):
        pass

    def port_occupier(self, port = 65432, localhost='127.0.0.1', stop_event = None):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.bind((localhost, port))
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"Port {port} occupied on {localhost}")
            try:
                while not stop_event.is_set():
                    time.sleep(1)
            finally:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"Port {port} released on {localhost}")

    # means that crewAI doesn't need to be running
    def socket_tester(self, port=65432, localhost='127.0.0.1', stop_event=None):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((localhost, int(port)))
            s.listen()
            s.settimeout(1.0)  # prevents blocking indefinitely on accept()
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"Socket tester listening on {localhost}:{port}")
            try:
                while not stop_event.is_set():
                    try:
                        conn, addr = s.accept()
                        with conn:
                            print(f"\nConnected by {addr}")
                            data = conn.recv(1024)
                            if data:
                                print(f"\n[NEW DATA] {data.decode('utf-8')}")
                    except socket.timeout:
                        continue
            finally:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"Socket tester stopping on port {port}")

    def dummy_data_populator(self, filename="eve.json", dummy_data = '{"type": "test", "data": "this is a test"}', iterations=1, delay = 0, stop_event = None):
        file_path = os.path.join('suricata-tcpreplay', 'suricata', filename)
        with open(file_path, 'w') as f:
            for i in range(iterations):
                if stop_event.is_set():
                    break
                f.write(dummy_data + '\n')
                time.sleep(delay)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Dummy data written to {filename}")

if __name__ == "__main__":
    tools = TestTools()

    # Keep track of threads + stop events
    jobs = {
        "port": {"thread": None, "stop": None},
        "socket": {"thread": None, "stop": None},
        "dummy": {"thread": None, "stop": None},
    }

    while True:
        print("\nSelect a test to run or suspend:")
        print("1. Port Occupier - occupies a specified port")
        print("2. Socket Tester - listens on a specified port and prints incoming data")
        print("3. Dummy Data Populator - writes dummy data to a specified file")
        print("4. End port occupier")
        print("5. End socket tester")
        print("6. End dummy data populator")
        print("q. Quit")
        choice = input("Enter choice: ")

        if choice == '1':
            port = int(input("Enter port to occupy (default 65432): ") or 65432)
            localhost = input("Enter localhost IP (default 127.0.0.1): ") or '127.0.0.1'
            stop_event = threading.Event()
            thread = threading.Thread(target=tools.port_occupier, args= (port, localhost, stop_event), daemon=True)
            jobs["port"] = {"thread": thread, "stop": stop_event}
            thread.start()
            
        elif choice == '2':
            port = int(input("Enter port to occupy (default 65432): ") or 65432)
            localhost = input("Enter localhost IP (default 127.0.0.1): ") or '127.0.0.1'
            stop_event = threading.Event()
            thread = threading.Thread(target=tools.socket_tester, args= (port, localhost, stop_event), daemon=True)
            jobs["socket"] = {"thread": thread, "stop": stop_event}
            thread.start()

        elif choice == '3':
            filename = input("Enter filename to write to (default eve.json): ") or "eve.json"
            dummy_data = input("Enter dummy data to write: ") or '{"type": "test", "data": "this is a test"}'
            iterations = int(input("Enter number of iterations (default 1): ") or 1)
            delay = float(input("Enter delay between writes in seconds (default 0): ") or 0)
            stop_event = threading.Event()
            thread = threading.Thread(target=tools.dummy_data_populator, args=(filename, dummy_data, iterations, delay, stop_event), daemon=True)
            jobs["dummy"] = {"thread": thread, "stop": stop_event}
            thread.start()
        
        elif choice == '4':
            if jobs["port"]["thread"]:
                jobs["port"]["stop"].set()
                jobs["port"]["thread"].join()
                jobs["port"] = {"thread": None, "stop": None}
                print("Port occupier stopped.")
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Port occupier is not running.")

        elif choice == '5':
            if jobs["socket"]["thread"]:
                jobs["socket"]["stop"].set()
                jobs["socket"]["thread"].join()
                jobs["socket"] = {"thread": None, "stop": None}
                print("Socket tester stopped.")
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Socket tester is not running.")

        elif choice == '6':
            if jobs["dummy"]["thread"]:
                jobs["dummy"]["stop"].set()
                jobs["dummy"]["thread"].join()
                jobs["dummy"] = {"thread": None, "stop": None}
                print("Dummy data stopped.")
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Dummy data is not running.")
        
        
        elif choice.lower() == 'q':
            print("Exiting...")
            for job in jobs.values():
                if job["stop"]:
                    job["stop"].set()
                    job["thread"].join()
            break

        time.sleep(0.5)

