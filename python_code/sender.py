import zmq
import os
import errno
import des_modes
from common import getBlockMode,desKey,secret
from Crypto.Hash import HMAC, SHA256,CMAC
from Crypto.Cipher import DES
 

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
    msgstr = msg.decode('ISO-8859-1')
    print("Ciphered message :",msgstr)
    mac = getHMAC(msg)
    print("MAC :",mac)
    msg_mac = msgstr +'(&)'+mac
    # print("Ciphered msg + MAC:",msg_mac)
    socket.send_string(str(msg_mac))

def getHMAC(msg):
    h = HMAC.new(secret, digestmod=SHA256)
    h.update(msg)
    # print("MAC",h.hexdigest())
    return h.hexdigest()

def getCMAC(msg):
    cobj = CMAC.new(secret, ciphermod=DES)
    cobj.update(msg)
    print( cobj.hexdigest())
    return  cobj.hexdigest()

if __name__ =="__main__":
    filename = '../testcases/3.txt'
    blockMode,plainTextMsg = readInfo(filename)
    socket = makeConnection()
    print("Plain Text: ",plainTextMsg)
    sendBlockMode(socket,blockMode)
    ModeOfOperation = getBlockMode(blockMode)
    key = desKey 
    cipherText=ModeOfOperation.encrypt(key,plainTextMsg)
    sendCipheredText(socket,cipherText)
