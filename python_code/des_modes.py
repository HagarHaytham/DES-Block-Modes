from Crypto.Cipher import DES
import struct
class BlockMode:   
    def __init__(self):
        pass
    
    def pad(self,msg,blockSize=8):
        padLen = blockSize - len(msg)%blockSize
        msg += padLen * '_'
        return msg
    def split(self,msg,blockSize=8):
        blocks =[]
        for i in range (0,len(msg),blockSize):
            blocks.append(msg[i : i+ blockSize])
        return blocks
    def convertToBytes(self,msg):
        # print(msg)
        msg = msg[1:]
        msg = msg[1:]
        msg = msg[:-1]
        listOfBytes =[]
        for p in msg : listOfBytes += [ord(p)] 
        bytesMsg = bytes(listOfBytes)
        # bytesMsg = b''
        # for i in msg:
        #     bytesMsg += struct.pack("b", ord(i))

        print("BYTEEEEEES")
        # bytesMsg.replace('\\','')
        print(len(bytesMsg))
        return bytesMsg


    def encrypt(self,key,messageBlocks):
        pass
    def decrypt(self,key,cipherText):
        pass
   
class ECBBlockMode(BlockMode):

    def encrypt(self,key,messageBlocks):
        ciphered = b''
        des = DES.new(key, DES.MODE_ECB)
        for block in messageBlocks:
            ciphered += des.encrypt(block.encode())
        return ciphered

    def decrypt(self,key,cipherText):
        blocks = super().split(cipherText,8*8)
        originalText =b''
        # cipherText = super().convertToBytes(cipherText)
        des = DES.new(key, DES.MODE_ECB)
        for block in blocks:
            original = des.decrypt(block)
            originalText += original
  
        originalText = des.decrypt(cipherText)

        return originalText.decode()

class CBCBlockMode(BlockMode):

    def encrypt(self,key,messageBlocks):
        pass
    def decrypt(self,key,cipherText):
        pass

class CFCBlockMode(BlockMode):

    def encrypt(self,key,messageBlocks):
        pass
    def decrypt(self,key,cipherText):
        pass

class CTRBlockMode(BlockMode):

    def encrypt(self,key,messageBlocks):
        pass
    def decrypt(self,key,cipherText):
        pass
