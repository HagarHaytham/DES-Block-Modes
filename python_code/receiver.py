import zmq
import random
import sys
import time
import des_modes
from common import getBlockMode,desKey

def makeConnection(port ="5556"):
    context = zmq.Context()
    socket = context.socket(zmq.PAIR)
    socket.connect("tcp://localhost:%s" % port)
    return socket
def writeOutput(filepath,msg):
     with open (filepath,'w') as f:
         f.write(msg)
def receiveBlockMode(socket):
    msg = socket.recv()
    mode =  int(msg)
    print ("Received Block Mode No. ",mode)
    return mode

def receiveCipheredText(socket):
    cipheredText = socket.recv()
    msg = cipheredText.decode()
    print("Received Ciphered message : ",msg)
    return msg.encode('ISO-8859-1')

if __name__=="__main__":
    socket = makeConnection()
    blockMode = receiveBlockMode(socket)
    ModeOfOperation = getBlockMode(blockMode)
    cipheredText = receiveCipheredText(socket)
    key = desKey
    # ModeOfOperation.decrypt(key,cipheredText)
    plainText = ModeOfOperation.decrypt(key,cipheredText)
    print("The Plain Message is :",plainText)
    plainText = ModeOfOperation.removePad(plainText)
    print("The Plain Message without padding is :",plainText)
    writeOutput('../output/4.txt',plainText)