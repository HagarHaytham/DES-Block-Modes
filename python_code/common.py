import des_modes

desKey = b'dummyKey' 
iv =b'dummy iv'

def getBlockMode(mode):
    ModeOfOperation = None
    if mode ==1:
        ModeOfOperation = des_modes.ECBBlockMode()
    elif mode ==2:
        ModeOfOperation = des_modes.CBCBlockMode()
    elif mode ==3:
        ModeOfOperation = des_modes.CFCBlockMode()
    else:
        ModeOfOperation = des_modes.CTRBlockMode()
    return ModeOfOperation