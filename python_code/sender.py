import zmq
import random
import sys
import time

block_mode = 1

port = "5556"
context = zmq.Context()
socket = context.socket(zmq.PAIR)
socket.bind("tcp://*:%s" % port)

print("Sending Block Mode No. ",block_mode)
socket.send_string(str(block_mode))

# while True:
#     socket.send_string("Server message to client3")
#     msg = socket.recv()
#     print (msg)
#     time.sleep(1)