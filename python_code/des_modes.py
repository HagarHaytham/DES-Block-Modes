from Crypto.Cipher import DES
from common import iv

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

    def byteXOR(self,block1, block2):
        return bytes([a ^ b for a, b in zip(block1, block2)])

    def encrypt(self,key,plainTextMsg):
        pass
    def decrypt(self,key,cipherText):
        pass
   
class ECBBlockMode(BlockMode):

    def encrypt(self,key,plainTextMsg):
        messageBlocks = super().split(plainTextMsg)
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

    def encrypt(self,key,plainTextMsg):
        messageBlocks= super().split(plainTextMsg)
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
    def __init__(self):
        self.S = 2

    def encrypt(self,key,plainTextMsg):
        messageBlocks= super().split(plainTextMsg,self.S)
        bytesBlocks = [block.encode() for block in messageBlocks]
        IVshiftRegister = iv
        ciphered = b''
        des = DES.new(key, DES.MODE_ECB)
        print('-------------------------------')
        for block in bytesBlocks:
            allBits = des.encrypt(IVshiftRegister)
            sBits = allBits[0:self.S]
            sCiphered = super().byteXOR(block,sBits)
            ciphered += sCiphered
            IVshiftRegister = bytearray(IVshiftRegister)
            IVshiftRegister [0:len(IVshiftRegister)-self.S] = IVshiftRegister[self.S:]
            IVshiftRegister [len(IVshiftRegister)-self.S:] = sCiphered
            IVshiftRegister = bytes(IVshiftRegister)
        return ciphered        

    def decrypt(self,key,cipherText):
        blocks = super().split(cipherText,self.S)
        originalText =b''
        des = DES.new(key, DES.MODE_ECB)
        IVshiftRegister = iv
        for block in blocks:
            allBits = des.encrypt(IVshiftRegister)
            sBits = allBits[0:self.S]
            sOriginal = super().byteXOR(block,sBits)
            originalText += sOriginal
            IVshiftRegister = bytearray(IVshiftRegister)
            IVshiftRegister [0:len(IVshiftRegister)-self.S] = IVshiftRegister[self.S:]
            IVshiftRegister [len(IVshiftRegister)-self.S:] = block
            IVshiftRegister = bytes(IVshiftRegister)
        originalText = originalText.decode()
        return originalText

            

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

    def encrypt(self,key,plainTextMsg):
        messageBlocks= super().split(plainTextMsg)
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
