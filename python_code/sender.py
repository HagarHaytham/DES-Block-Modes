import zmq
import random
import sys
import time
import os
import errno
import des_modes
from common import getBlockMode,desKey,secret
from Crypto.Hash import HMAC, SHA256
import time

def readInfo(filepath):
    if not os.path.isfile(filepath,):
        raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), filepath)
    with open (filepath,'r') as f:
        lines =f.readlines()
    blockMode = int(lines[0])
    plainTextMsg = lines[1]
    return blockMode, plainTextMsg

def makeConnection(port ="5556"):
    context = zmq.Context()
    socket = context.socket(zmq.PAIR)
    socket.bind("tcp://*:%s" % port)
    return socket

def sendBlockMode(socket,mode):
    print("Sending Block Mode No. ",mode)
    socket.send_string(str(mode))

def sendCipheredText(socket,msg):
    print("Sending Ciphered message : ",msg.decode('ISO-8859-1'))
    socket.send_string(str(msg.decode('ISO-8859-1')))
    mac = getHMAC(msg)
    socket.send_string(str(mac))


def getHMAC(msg):
    h = HMAC.new(secret, digestmod=SHA256)
    h.update(msg)
    print("MAC",h.hexdigest())
    return h.hexdigest()

if __name__ =="__main__":
    blockMode,plainTextMsg = readInfo('../testcases/1.txt')
    socket = makeConnection()
    print("Plain Text: ",plainTextMsg)
    sendBlockMode(socket,blockMode)
    ModeOfOperation = getBlockMode(blockMode)
    plainTextMsg = ModeOfOperation.pad(plainTextMsg)
    print("Padded Message:",plainTextMsg)
    key = desKey 
    cipherText=ModeOfOperation.encrypt(key,plainTextMsg)
    sendCipheredText(socket,cipherText)
