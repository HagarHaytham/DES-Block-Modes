from Crypto.Cipher import DES , DES3
from Crypto.Random import get_random_bytes

key = b'-8B key-'
cipher = DES.new(key, DES.MODE_CBC)
plaintext = b'We are no longer the knights who say ni!'

by = b'i\xa8ltw\xa1\x1e\xe0'
iv = b'dummykey'
bt = b''
# for i in range (0,len(by)):
#     a = by[i:i+1]
#     print(a)
#     b = iv[i:i+1]
#     print(b)
#     c =chr(ord(a)^ord(b))
#     print(c)

# for (a,b) in zip(by, iv):
#     print(type(by[0:1]))
#     print(type(b))
#     b+= a^b
#     print(a,b)
def byteXOR(block1, block2):
    return bytes([a ^ b for a, b in zip(block1, block2)])
encrypted = byteXOR(by,iv)
print(encrypted)
# print(type(encrypted))
# print(b)
# print(type(b))

# print(encrypted[0].to_bytes(2, byteorder='big'))

# print(len(plaintext))
# msg = cipher.encrypt(b'We are no longer the knights who say ni!')
# print(msg)
# msg = cipher.encrypt(b'We are n')
# print(msg)
# msg = cipher.encrypt(b'o longer')
# print(msg)

# plain = cipher.decrypt(msg)
# print(plain)


# print(type(cipher.iv))
# print(cipher.iv)
# st ="b'\xef\xac\x88\xac\xd6\x8a\xf7\xbe'"
# st = cipher.iv.decode('latin-1').encode("utf-8")
# # st.replace('\\','0')
# print(type(st))
# print(st)
# x =st.decode()
# print(x)
# print(x.decode())