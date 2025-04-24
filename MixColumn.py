from Table import Mix, MixINV


def galoisMult(a, b):
    p = 0
    for i in range(8):
        if b & 1 == 1:
            p = p ^ a
        hiBitSet = a & 0x80
        a <<= 1
        if hiBitSet == 0x80:
            a = a ^ 0x1b
        b >>= 1
    return p % 256


def MixColumn(Text):
    New_Text = []
    for i in range(len(Text)):
        array_time = [galoisMult(Text[i % 4], Mix[round(i // 4)][0]),
                      galoisMult(Text[i % 4 + 4], Mix[round(i // 4)][1]),
                      galoisMult(Text[i % 4 + 8], Mix[round(i // 4)][2]),
                      galoisMult(Text[i % 4 + 12], Mix[round(i // 4)][3])]
        num = array_time[0] ^ array_time[1] ^ array_time[2] ^ array_time[3]
        New_Text.append(num)
    return New_Text


def MixColumnInv(Text):
    New_Text = []
    for i in range(len(Text)):
        array_time = [galoisMult(Text[i % 4], MixINV[round(i // 4)][0]),
                      galoisMult(Text[i % 4 + 4], MixINV[round(i // 4)][1]),
                      galoisMult(Text[i % 4 + 8], MixINV[round(i // 4)][2]),
                      galoisMult(Text[i % 4 + 12], MixINV[round(i // 4)][3])]
        num = array_time[0] ^ array_time[1] ^ array_time[2] ^ array_time[3]
        New_Text.append(num)
    return New_Text