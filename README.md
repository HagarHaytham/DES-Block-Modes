# DES-Block-Modes
Two parties communciacting through sockets using [ZMQ](https://pyzmq.readthedocs.io/en/latest/api/index.html)
The sender sends an encrypted message associated with its mac for authentication
The receiver decryptes the message and verifies it using the mac received.

Implementing the following modes of operation of [DES](https://pycryptodome.readthedocs.io/en/latest/src/cipher/des.html)
* Electronic Codebook (ECB)
* Cipher Block Chaining (CBC)
* Cipher Feedback (CFB)
* Counter (CTR)

Using [HMAC](https://pycryptodome.readthedocs.io/en/latest/src/hash/hmac.html) for message authentication