# Name:  Matthew Baker
# OSU Email:  bakerma2@oregonstate.edu
# Course: CS361 - Software Engineering 1
# Assignment: 4 - Pipe Spike
# Description: Server for ZeroMQ demo.

import time
import zmq


def main():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5555")

    while True:
        message = socket.recv()
        print(f"Received request from the client: {message.decode()}")
        if len(message) > 0:
            if message.decode() == 'Q':
                break
            time.sleep(3)
            socket.send_string("This is a response.")
    context.destroy()  # RIP old friend

if __name__ == '__main__':
    main()