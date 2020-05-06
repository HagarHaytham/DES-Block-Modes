import zmq
import des_modes
from common import getBlockMode,desKey,secret
from Crypto.Hash import HMAC, SHA256,CMAC
from Crypto.Cipher import DES
import argparse


def makeConnection(port ="5556"):
    context = zmq.Context()
    socket = context.socket(zmq.PAIR)
    socket.connect("tcp://localhost:%s" % port)
    return socket

def writeOutput(filepath,cipheredText,msg,auth):
    with open (filepath,'w',encoding="utf-8") as f:
        f.write(cipheredText+'\n')
        f.write(msg+'\n')
        if auth:
            f.write("The message is authenticated")
        else:
            f.write("The message is NOT authenticated")
         
        

def receiveBlockMode(socket):
    msg = socket.recv()
    mode =  int(msg)
    print ("Received Block Mode No. ",mode)
    return mode

def receiveCipheredText(socket):
    cipher_mac = socket.recv()
    # print("Received message + mac:", cipher_mac)
    cipheredText = cipher_mac[0:cipher_mac.index(b'(&)')]
    mac = cipher_mac[cipher_mac.index(b'(&)')+3:]
    msgciphered = cipheredText.decode()
    print("Received Ciphered message : ",msgciphered)
    msg = msgciphered.encode('ISO-8859-1')
    print("MAC", mac)
    auth = verifyHMAC(mac,msg)
    return  msgciphered,msg,auth

def verifyHMAC(mac,msg):
    h = HMAC.new(secret, digestmod=SHA256)
    # msg = b'ppp'
    h.update(msg)
    try:
        h.hexverify(mac)
        print("The message is AUTHENTICATED" )
        return True
    except ValueError:
        print("The message or the key is WRONG")
        return False
    

def verifyCMAC(mac,msg):
    c = CMAC.new(secret, ciphermod=DES)
    # msg = b'ppp'
    c.update(msg)
    try:
        c.verify(mac)
        print("The message is AUTHENTICATED" )
        return True
    except ValueError:
        print("The message or the key is WRONG")
        return False



if __name__=="__main__":
    # filename = '../output/3.txt'
    my_parser = argparse.ArgumentParser()
    my_parser.add_argument(help='Output file name',dest='file_name')
    args = my_parser.parse_args()
    filename = args.file_name

    socket = makeConnection()
    blockMode = receiveBlockMode(socket)
    ModeOfOperation = getBlockMode(blockMode)
    msgciphered,cipheredText,auth = receiveCipheredText(socket)
    key = desKey
    plainText = ModeOfOperation.decrypt(key,cipheredText)
    # print("The Plain Message is :",plainText)
    plainText = ModeOfOperation.removePad(plainText)
    print("The Plain Message without padding is :",plainText)
    writeOutput(filename,msgciphered,plainText,auth)