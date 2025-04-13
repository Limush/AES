import random
from ASCII_forming import ASCII
from KeyExtension import KeyExtension
from AddRoundKey import AddRoundKey
from SubBytes import SubBytes, SubBytesInv
from ShiftRow import ShiftRow, ShiftRowInv
from MixColumn import MixColumn, MixColumnInv

#           Нужно реализовать:
#   Ключ из текста  -
#   KeyExtension    +
#   AddRoundKey     +
#   SubBytes        +       SubBytesInv     +
#   ShiftRow        +       ShiftRowInv     +
#   MixColumn       +       MixColumnInv    +
#   Encoded         +
#   Decoded         +


def str_in_int(text):
    Text_all = [int(ASCII_p_2[i], 2) for i in text]
    if len(Text_all) % 16 != 0:
        for num in range(16 - len(Text_all) % 16):
            Text_all.append(0)
    return Text_all


def int_in_str(text):
    Text_all = []
    for i in text:
        simv = bin(i)[2:]
        Text_all.append(ASCII_p_2_inv['0'*(8 - len(simv)) + simv])
    return ''.join(Text_all)

def encryption(Text, Expansion_key, Rounds):
    Text = AddRoundKey(Text, Expansion_key[0])
    for i in range(Rounds - 1):
        Text = SubBytes(Text)
        Text = ShiftRow(Text, Rounds)
        Text = MixColumn(Text)
        Text = AddRoundKey(Text, Expansion_key[i+1])
    Text = SubBytes(Text)
    Text = ShiftRow(Text, Rounds)
    Text = AddRoundKey(Text, Expansion_key[Rounds])
    return Text


def decryption(Text, Expansion_key, Rounds):
    Text = AddRoundKey(Text, Expansion_key[-1])
    Text = ShiftRowInv(Text, Rounds)
    Text = SubBytesInv(Text)
    for i in range(Rounds - 1, 0, -1):
        Text = AddRoundKey(Text, Expansion_key[i])
        Text = MixColumnInv(Text)
        Text = ShiftRowInv(Text, Rounds)
        Text = SubBytesInv(Text)
    Text = AddRoundKey(Text, Expansion_key[0])
    return Text


ASCII_p_2, ASCII_p_2_inv = ASCII()

Secret_key = [random.randint(0, 255) for _ in range(16)]
Expansion_key = KeyExtension(Secret_key)


text = 'Курсовая работа AES128'
print(f"Начальная строка:\n"
      f"\t{text}\n")
Text_all = str_in_int(text)

row, column = 4, 4
size = row * column
Rounds = 10 if size == 16 else (12 if size == 18 else 14)
encrypt_all = []
for i in range(len(Text_all) // size):
    encrypt = encryption(Text_all[0 + i * size:size + i * size], Expansion_key, Rounds)

    encrypt_all.extend(encrypt)
else:
    print(f"Зашифрованная строка:\n"
          f"\t{int_in_str(encrypt_all)}\n")

decrypt_all = []
for i in range(len(Text_all) // 16):
    decrypt = decryption(encrypt_all[0 + i * size:size + i * size], Expansion_key, Rounds)
    decrypt_all.extend(decrypt)
else:
    print(f"Расшифрованная строка:\n"
          f"\t{int_in_str(decrypt_all)}\n")
