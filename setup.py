# Run this before sketch.py
import zmq
import json

context = zmq.Context()

#  Socket to talk to server
print("Running setup.")
print("Connecting to simulator…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

with open('setup.json', 'r') as file:
    message_json = file.read()

socket.send_string(message_json)

#  Get the reply.
message = socket.recv()
print("Received reply %s" % message)
print("Setup complete.")