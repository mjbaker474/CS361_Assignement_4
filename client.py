# Name:  Matthew Baker
# OSU Email:  bakerma2@oregonstate.edu
# Course: CS361 - Software Engineering 1
# Assignment: 4 - Pipe Spike
# Description: Client for ZeroMQ demo

import time
import zmq



def main():
    context = zmq.Context()
    print("Client attempting to connect to server...")
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")
    print("Sending a request...")
    socket.send_string("This is a request.")
    message = socket.recv()
    print(f"Server sent back: {message.decode()}")
    socket.send_string("Q")


if __name__ == '__main__':
    main()
