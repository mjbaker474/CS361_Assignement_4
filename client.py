# Name:  Matthew Baker
# OSU Email:  bakerma2@oregonstate.edu
# Course: CS361 - Software Engineering 1
# Assignment: 4 - Pipe Spike
# Description: Client for ZeroMQ demo

import zmq


def main():
    # Create a ZMQ context object and use it to connect to a socket.
    context = zmq.Context()
    print("Client attempting to connect to server...")
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")

    # Send a request to the server.
    request = "This is a CS361 request."
    print(f"Sending the following request to the server: {request}")
    socket.send_string(request)

    # Receive response from the server.
    response = socket.recv()
    print(f"Server replied: {response.decode()}")
    socket.send_string("Q")


if __name__ == '__main__':
    main()
