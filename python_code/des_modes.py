class BlockMode:   
    def __init__(self):
        pass
    
    def splitAndPad(self,msg,blockSize=8):
        print(len(msg))
        padLen = blockSize - len(msg)%blockSize
        print(padLen)
        msg += padLen * '_'
        blocks=[]
        print(len(msg))
        for i in range (0,len(msg),blockSize):
            blocks.append(msg[i : i+ blockSize])
            print(msg[i : i+blockSize])

    def encrypt(self,plainText):
        pass
    def decrypt(self,cipherText):
        pass
   
class ECBBlockMode(BlockMode):

    def encrypt(self,plainText):
        pass
    def decrypt(self,cipherText):
        pass

class CBCBlockMode(BlockMode):

    def encrypt(self,plainText):
        pass
    def decrypt(self,cipherText):
        pass

class CFCBlockMode(BlockMode):

    def encrypt(self,plainText):
        pass
    def decrypt(self,cipherText):
        pass

class CTRBlockMode(BlockMode):

    def encrypt(self,plainText):
        pass
    def decrypt(self,cipherText):
        pass
