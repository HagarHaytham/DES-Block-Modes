import des_modes

def getBlockMode(mode):
    ModeOfOperation = None
    if mode ==1:
        ModeOfOperation = ECBBlockMode()
    elif mode ==2:
        ModeOfOperation = CBCBlockMode()
    elif mode ==3:
        ModeOfOperation = CFCBlockMode()
    else:
        ModeOfOperation = CTRBlockMode()
    return ModeOfOperation