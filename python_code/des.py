from Crypto.Cipher import DES , DES3
from Crypto.Random import get_random_bytes

# Avoid Option 3
# while True:
#     try:
#         key = DES3.adjust_key_parity(get_random_bytes(8))
#         break
#     except ValueError:
#         pass
key = b'-8B key-'
cipher = DES.new(key, DES.MODE_ECB)
plaintext = b'We are no longer the knights who say ni!'
print(len(plaintext))
msg = cipher.encrypt(b'We are no longer the knights who say ni!')
print(msg)
msg = cipher.encrypt(b'We are n')
print(msg)
msg = cipher.encrypt(b'o longer')
print(msg)

plain = cipher.decrypt(msg)
print(plain)
