from Crypto.Cipher import DES
from common import iv
import struct

blocksize = 8
class BlockMode:   
    def __init__(self):
        pass
    
    def removePad(self,msg):
        return msg.replace('~','')

    def pad(self,msg,blockSize=blocksize):
        padLen = blockSize - len(msg)%blockSize
        msg += padLen * '~'
        return msg
    def split(self,msg,blockSize=blocksize):
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

    def byteXOR(self,block1, block2):
        return bytes([a ^ b for a, b in zip(block1, block2)])

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
        blocks = super().split(cipherText)
        originalText =b''
        # cipherText = super().convertToBytes(cipherText)
        des = DES.new(key, DES.MODE_ECB)
        for block in blocks:
            original = des.decrypt(block)
            originalText += original
        originalText = des.decrypt(cipherText)
        originalText = originalText.decode()
        return originalText

class CBCBlockMode(BlockMode):

    def encrypt(self,key,messageBlocks):
        ciphered = b''
        bytesBlocks = [block.encode() for block in messageBlocks] 
        prevCipher = iv
        des = DES.new(key, DES.MODE_ECB)
        for block in bytesBlocks:
            xoredBlock = super().byteXOR(prevCipher,block)
            prevCipher = des.encrypt(xoredBlock)
            ciphered += prevCipher
        return ciphered

    def decrypt(self,key,cipherText):
        blocks = super().split(cipherText)
        originalText =b''
        des = DES.new(key, DES.MODE_ECB)
        prevCipher = iv
        for block in blocks:
            decrypted = des.decrypt(block)
            original = super().byteXOR(prevCipher,decrypted)
            originalText += original
            prevCipher = block
        originalText = originalText.decode()
        return originalText

    

class CFCBlockMode(BlockMode):

    def encrypt(self,key,messageBlocks):
        pass
    def decrypt(self,key,cipherText):
        pass

class CTRBlockMode(BlockMode):
    def __init__(self):
        self.counter =0

    def CounterInc (self):
        self.counter +=1
        strCounter = str(self.counter)
        k = len(strCounter)
        padCounter = (blocksize - k) * '0' 
        Counter = padCounter + strCounter
        return Counter.encode()

    def encrypt(self,key,messageBlocks):
        bytesBlocks = [block.encode() for block in messageBlocks]
        ciphered = b''
        des = DES.new(key, DES.MODE_ECB)
        for block in bytesBlocks:
            cnt = self.CounterInc()
            cntEnc = des.encrypt(cnt)
            ciphered += super().byteXOR(cntEnc,block)
        return ciphered

    def decrypt(self,key,cipherText):
        blocks = super().split(cipherText)
        originalText =b''
        des = DES.new(key, DES.MODE_ECB)
        for block in blocks:
            cnt = self.CounterInc()
            cntEnc = des.encrypt(cnt)
            originalText += super().byteXOR(cntEnc,block)
        originalText = originalText.decode()
        return originalText
