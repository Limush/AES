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
        # print(f"{hex(Text[i % 4])[2:].upper()} {Mix[round(i // 4)][0]}\n"
        #       f"{hex(Text[i % 4 + 4])[2:].upper()} {Mix[round(i // 4)][1]}\n"
        #       f"{hex(Text[i % 4 + 8])[2:].upper()} {Mix[round(i // 4)][2]}\n"
        #       f"{hex(Text[i % 4 + 12])[2:].upper()} {Mix[round(i // 4)][3]}\n")
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
    # a = New_Text
    # print([hex(a[i])[2:].upper() for i in range(len(a))])
    return New_Text

# Table = [164, 72, 231, 78, 33, 80, 131, 174, 51, 158, 244, 245, 84, 230, 190, 94]
# # ['A4', '48', 'E7', '4E',
# #  '21', '50', '83', 'AE',
# #  '33', '9E', 'F4', 'F5',
# #  '54', 'E6', 'BE', '5E']
# Table2 = [87, 24, 1, 222, 231, 183, 67, 83, 31, 14, 78, 243, 77, 193, 34, 53]
# [['57', '18', '01', 'de'],
#  ['e7', 'b7', '43', '53'],
#  ['1f', '0e', '4e', 'f3'],
#  ['4d', 'c1', '22', '35']]


# q1 = MixColumn(Table)
# q2 = MixColumnInv(Table2)
#
# print(q1)
# print(q2)
# print()
# for i in q2:
#     print(i)

