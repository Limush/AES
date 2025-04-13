from Table import RCON
from SubBytes import SubBytes


def KeyExtension(Secret_key):
    Expansion_key = [Secret_key]
    Size = len(Secret_key)
    Rounds = 10 if Size == 16 else (12 if Size == 20 else 14)
    for rounds in range(Rounds):
        Time = []
        for i in range(4):
            if i % 4 == 0:
                tec = [Expansion_key[-1][i] for i in range(Size) if i % 4 == 3]
                tec.append(tec[0])
                del tec[0]
                tec = SubBytes(tec)
                Time.extend([tec[0] ^ Expansion_key[-1][0] ^ RCON[rounds], tec[1] ^ Expansion_key[-1][4], tec[2] ^ Expansion_key[-1][8], tec[3] ^ Expansion_key[-1][12]])
            else:
                tec = [Expansion_key[-1][w] for w in range(Size) if w % 4 == i]
                Time.extend([tec[0] ^ Time[-4], tec[1] ^ Time[-3], tec[2] ^ Time[-2], tec[3] ^ Time[-1]])
        else:
            count = 0
            Key = []
            for _ in range(4):
                for i in range(len(Time)):
                    if i % 4 == count:
                        Key.append(Time[i])
                count += 1
            Expansion_key.append(Key)
    return Expansion_key