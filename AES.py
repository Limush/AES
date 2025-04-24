import random
from ASCII_forming import ASCII
from KeyExtension import KeyExtension
from AddRoundKey import AddRoundKey
from SubBytes import SubBytes, SubBytesInv
from ShiftRow import ShiftRow, ShiftRowInv
from MixColumn import MixColumn, MixColumnInv


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


def Encryption_block(Text, Expansion_key, Rounds):
    Text = AddRoundKey(Text, Expansion_key[0])
    for i in range(Rounds - 1):
        Text = SubBytes(Text)
        Text = ShiftRow(Text, Rounds, size)
        Text = MixColumn(Text)
        Text = AddRoundKey(Text, Expansion_key[i+1])
    Text = SubBytes(Text)
    Text = ShiftRow(Text, Rounds, size)
    Text = AddRoundKey(Text, Expansion_key[Rounds])
    return Text


def Decryption_block(Text, Expansion_key, Rounds):
    Text = AddRoundKey(Text, Expansion_key[-1])
    Text = ShiftRowInv(Text, Rounds, size)
    Text = SubBytesInv(Text)
    for i in range(Rounds - 1, 0, -1):
        Text = AddRoundKey(Text, Expansion_key[i])
        Text = MixColumnInv(Text)
        Text = ShiftRowInv(Text, Rounds, size)
        Text = SubBytesInv(Text)
    Text = AddRoundKey(Text, Expansion_key[0])
    return Text


def Encypt(Text, Rounds):
    encrypt_all = []
    for i in range(len(Text) // 16):
        encrypt = Encryption_block(Text[0 + i * 16:16 + i * 16], Expansion_key, Rounds)
        encrypt_all.extend(encrypt)
    return encrypt_all


def Decypt(Text, Rounds):
    decrypt_all = []
    for i in range(len(Text_all) // 16):
        decrypt = Decryption_block(Text[0 + i * 16:16 + i * 16], Expansion_key, Rounds)
        decrypt_all.extend(decrypt)
    return decrypt_all

ASCII_p_2, ASCII_p_2_inv = ASCII()

row, column = 4, 8
size = row * column
Rounds = 10 if size == 16 else (12 if size == 24 else 14)

Secret_key = [random.randint(0, 255) for _ in range(size)]
Expansion_key = KeyExtension(Secret_key)

text = 'Курсовая работа AES128'
print(f"Начальная строка:\n"
      f"\t{text}\n"
      f"Ключ:\n"
      f"\t {Secret_key}")
Text_all = str_in_int(text)


encrypt = Encypt(Text_all, Rounds)
print(f"Зашифрованная строка:\n"
      f"\t{int_in_str(encrypt)}\n")


decrypt = Decypt(encrypt, Rounds)
print(f"Расшифрованная строка:\n"
      f"\t{int_in_str(decrypt)}\n")
