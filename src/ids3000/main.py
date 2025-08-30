#!/usr/bin/env python
import sys
import warnings
import time
import queue
import socket
import threading
from datetime import datetime
from ids3000.crew import Ids3000

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

data_queue = queue.Queue()

HOST = "127.0.0.1"
PORT = 65432

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """

    print("Waiting for data...")
    inputs = {
        'topic': 'Mirai Botnet Detection & DDOS Classification',
        'event': data_queue.get(), #this is blocking which is ok because we will be waiting for chunks of data regardless 
        'current_year': str(datetime.now().year)
    }
    try:
        Ids3000().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")
    finished = True


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "AI LLMs",
        'current_year': str(datetime.now().year)
    }
    try:
        Ids3000().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        Ids3000().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": "AI LLMs",
        "current_year": str(datetime.now().year)
    }
    
    try:
        Ids3000().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")


#need to make it non-blocking
def socket_listener():
    global data_queue
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        while True:
            conn, addr = s.accept()
            with conn:
                print(f"Connected by {addr}")
                data = conn.recv(65432) # receive the chunk from the port
                if data:
                    print(f"[NEW DATA] {data.decode('utf-8')}")
                    data_queue.put(data.decode('utf-8'))


threading.Thread(target=socket_listener, daemon=True).start()

while True:
        run()
        print("and again")



    #socket is listening on port 65432
    #socket is on a seperate thread so it can run in the background
