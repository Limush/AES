from Table import SBlock, SBlockInv


def SubBytes(Text):
    New_Text = []
    for num in Text:
        New_Text.append(SBlock[num])
    return New_Text


def SubBytesInv(Text):
    New_Text = []
    for num in Text:
        New_Text.append(SBlockInv[num])
    return New_Text