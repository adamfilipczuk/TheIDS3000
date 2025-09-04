from flask import Flask, request
from queue import Queue

app = Flask(__name__)
event_queue = Queue()

@app.route("/new_data", methods=["POST"])
def new_data():
    # Read the raw request body as a string
    message = request.data.decode("utf-8")
    if not message:
        return "No data received", 400

    print(f"[NEW DATA] {message}")
    event_queue.put(message)
    return "ok", 200

if __name__ == "__main__":
    print("Starting local server on http://127.0.0.1:5000")
    app.run(host="127.0.0.1", port=5000, debug=False)
