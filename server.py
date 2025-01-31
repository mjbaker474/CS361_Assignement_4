# Name:  Matthew Baker
# OSU Email:  bakerma2@oregonstate.edu
# Course: CS361 - Software Engineering 1
# Assignment: 4 - Pipe Spike
# Description: Server for ZeroMQ demo.

import time
import zmq


def main():
    # Create a ZMQ context opject and use it to bind a socket.
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5555")

    # Listen for a request from client.
    while True:
        message = socket.recv()
        # Message received.
        if len(message) > 0:
            print(f"Received request from the client: {message.decode()}")
            if message.decode() == 'Q':
                break
            time.sleep(3)
            response = "Wow, thank you for your CS361 message!"
            print(f"Sending response to the client: {response}")
            socket.send_string(response)  # Respond to message
    context.destroy()  # RIP old friend


if __name__ == '__main__':
    main()
