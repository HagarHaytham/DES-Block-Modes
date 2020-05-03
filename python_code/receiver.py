import zmq
import random
import sys
import time
import des_modes
import common

def makeConnection(port ="5556"):
    context = zmq.Context()
    socket = context.socket(zmq.PAIR)
    socket.connect("tcp://localhost:%s" % port)
    return socket

def receiveBlockMode(socket):
    msg = socket.recv()
    mode =  int(msg)
    print ("Received Block Mode No. ",mode)
    return mode

def receiveCipheredText(socket):
    cipheredText = socket.recv()
    print("Received Ciphered message : ",cipheredText)
    return cipheredText

if __name__=="__main__":
    socket = makeConnection()
    blockMode = receiveBlockMode(socket)
    ModeOfOperation = getBlockMode(blockMode)
    cipheredText = receiveCipheredText(socket)
    plainText = ModeOfOperation.decrypt(cipheredText)
    print("The Plain Message is :",plainText)