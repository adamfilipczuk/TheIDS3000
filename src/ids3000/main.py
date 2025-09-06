#!/usr/bin/env python
import sys
import warnings
import threading
import os
from datetime import datetime
from ids3000.crew import Ids3000
from ids3000.socket_listener import socket_listener, data_queue

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """Run the crew."""

    print("Waiting for data...")
    inputs = {
        'event': data_queue.get(), #this is blocking which is ok because we will be waiting for chunks of data regardless 
        'current_year': str(datetime.now().year)
    }
    output_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'output', 'data_queue.json'))
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w') as f:
        f.write(inputs['event'])
    try:
        Ids3000().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")
    finished = True


def train():
    """Train the crew for a given number of iterations."""

    inputs = {
        "topic": "AI LLMs",
        'current_year': str(datetime.now().year)
    }
    try:
        Ids3000().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """Replay the crew execution from a specific task."""

    try:
        Ids3000().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """Test the crew execution and returns the results."""

    inputs = {
        "topic": "AI LLMs",
        "current_year": str(datetime.now().year)
    }
    
    try:
        Ids3000().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")

        
# Socket listener runs on thread in background
threading.Thread(target=socket_listener, daemon=True).start()

#Logic for running in loop
# while True:
#         run()
#         print("and again")

