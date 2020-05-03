import zmq
import random
import sys
import time
import os
import errno
import des_modes

def readInfo(filepath):
    if not os.path.isfile(filepath):
        raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), filepath)
    with open (filepath) as f:
        lines =f.readlines()
    blockMode = int(lines[0])
    plainTextMsg = lines[1]
    return blockMode, plainTextMsg

def makeConnection(port ="5556"):
    context = zmq.Context()
    socket = context.socket(zmq.PAIR)
    socket.bind("tcp://*:%s" % port)
    return socket

def getBlockMode(mode):
    ModeOfOperation = None
    if mode ==1:
        ModeOfOperation = ECBBlockMode()
    elif mode ==2:
        ModeOfOperation = CBCBlockMode()
    elif mode ==3:
        ModeOfOperation = CFCBlockMode()
    else:
        ModeOfOperation = CTRBlockMode()
    return ModeOfOperation

def sendBlockMode(socket,mode):
    print("Sending Block Mode No. ",mode)
    socket.send_string(str(mode))

def sendCipheredText(socket,msg):
    print("Sending Ciphered message : ",msg)
    socket.send_string(str(msg))

if __name__ =="__main__":
    blockMode,plainTextMsg = readInfo('../testcases/1.txt')
    socket = makeConnection()
    print("Plain Text: ",plainTextMsg)
    ModeOfOperation = getBlockMode(blockMode)
    messageBlocks= ModeOfOperation.splitAndPad(plainTextMsg)
    cipherText=ModeOfOperation.encrypt(messageBlocks)
    sendCipheredText(socket,cipherText)
