from Table import RCON
from SubBytes import SubBytes


def KeyExtension(Secret_key):
    Expansion_key = [Secret_key]
    Size = len(Secret_key)
    Rounds = 10 if Size == 16 else (12 if Size == 24 else 14)
    for rounds in range(Rounds):
        Time = []
        for i in range(Size // 4):
            if i % 4 == 0:
                tec = Expansion_key[-1][-4:]
                tec.append(tec[0])
                del tec[0]
                tec = SubBytes(tec)
                Time.extend([tec[0] ^ Expansion_key[-1][0] ^ RCON[rounds], tec[1] ^ Expansion_key[-1][1], tec[2] ^ Expansion_key[-1][2], tec[3] ^ Expansion_key[-1][3]])
            else:
                tec = Expansion_key[-1][4*i:4*i+4]
                Time.extend([tec[0] ^ Time[-4], tec[1] ^ Time[-3], tec[2] ^ Time[-2], tec[3] ^ Time[-1]])
        else:
            Expansion_key.append(Time)
    return Expansion_key