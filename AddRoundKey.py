def AddRoundKey(Text, round_key):
    for i in range(len(Text)):
        Text[i] = Text[i] ^ round_key[i]
    return Text