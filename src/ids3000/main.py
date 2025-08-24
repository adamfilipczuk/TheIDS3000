#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from ids3000.crew import Ids3000

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information


#this neeeds to be put into a tool later to not clutter the main file
#will be replaced by JSON RAG Search
def read_file_as_string(file_path, max_lines=None):
    content = []
    try:
        with open(file_path, 'r') as file:
            for i, line in enumerate(file):
                if max_lines is None or i >= max_lines:
                    break
                content.append(line.rstrip("\n"))
    except FileNotFoundError:
        print(f"The file at {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return "\n".join(content)


dummy_event = read_file_as_string('eve.json', 100)

def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': 'Mirai Botnet Detection & DDOS Classification',
        'event': dummy_event,
        'current_year': str(datetime.now().year)
    }
    
    try:
        Ids3000().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


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
