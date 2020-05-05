import zmq
import des_modes
from common import getBlockMode,desKey,secret
from Crypto.Hash import HMAC, SHA256,CMAC
from Crypto.Cipher import DES


def makeConnection(port ="5556"):
    context = zmq.Context()
    socket = context.socket(zmq.PAIR)
    socket.connect("tcp://localhost:%s" % port)
    return socket

def writeOutput(filepath,cipheredText,msg):
     with open (filepath,'w',encoding="utf-8") as f:
         f.write(cipheredText+'\n')
         f.write(msg)

def receiveBlockMode(socket):
    msg = socket.recv()
    mode =  int(msg)
    print ("Received Block Mode No. ",mode)
    return mode

def receiveCipheredText(socket):
    cipheredText = socket.recv()
    msgciphered = cipheredText.decode()
    print("Received Ciphered message : ",msgciphered)
    msg = msgciphered.encode('ISO-8859-1')
    mac = socket.recv()
    print("MAC", mac)
    verifyHMAC(mac,msg)
    return  msgciphered,msg

def verifyHMAC(mac,msg):
    h = HMAC.new(secret, digestmod=SHA256)
    # msg = b'ppp'
    h.update(msg)
    try:
        h.hexverify(mac)
        print("The message is AUTHENTICATED" )
    except ValueError:
        print("The message or the key is WRONG")

def verifyCMAC(mac,msg):
    c = CMAC.new(secret, ciphermod=DES)
    # msg = b'ppp'
    c.update(msg)
    try:
        c.verify(mac)
        print("The message is AUTHENTICATED" )
    except ValueError:
        print("The message or the key is WRONG")



if __name__=="__main__":
    filename = '../output/4.txt'
    socket = makeConnection()
    blockMode = receiveBlockMode(socket)
    ModeOfOperation = getBlockMode(blockMode)
    msgciphered,cipheredText = receiveCipheredText(socket)
    key = desKey
    plainText = ModeOfOperation.decrypt(key,cipheredText)
    print("The Plain Message is :",plainText)
    plainText = ModeOfOperation.removePad(plainText)
    print("The Plain Message without padding is :",plainText)
    writeOutput(filename,msgciphered,plainText)