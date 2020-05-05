from Crypto.Hash import HMAC, SHA256
# from common import secret
secret = b'Swordfish'

def getHMAC(msg):
    h = HMAC.new(secret, digestmod=SHA256)
    h.update(msg)
    print(h.hexdigest())
    return h.hexdigest()

def verifyHMAC(mac,msg):
    h = HMAC.new(secret, digestmod=SHA256)
    # msg = b'ppp'
    h.update(msg)
    try:
        h.hexverify(mac)
        print("The message '%s' is authentic" % msg)
    except ValueError:
        print("The message or the key is wrong")


if __name__=='__main__':
    m = b'HELOOOOO'
    x=getHMAC(m)
    verifyHMAC(x,m)