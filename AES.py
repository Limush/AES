import random
import time
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


def Encryption_block(Text, Expansion_key, Rounds, size):
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


def Decryption_block(Text, Expansion_key, Rounds, size):
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


def Encypt(Text, Secret_key, size):
    start_time = time.time()
    Expansion_key = KeyExtension(Secret_key)
    Rounds = 10 if size == 16 else (12 if size == 24 else 14)
    Text = str_in_int(Text)
    encrypt_all = []
    for i in range(len(Text) // 16):
        encrypt = Encryption_block(Text[0 + i * 16:16 + i * 16], Expansion_key, Rounds, size)
        encrypt_all.extend(encrypt)
    return int_in_str(encrypt_all), time.time() - start_time


def Decypt(Text, Secret_key, size):
    start_time = time.time()

    Expansion_key = KeyExtension(Secret_key)
    Rounds = 10 if size == 16 else (12 if size == 24 else 14)
    Text = str_in_int(Text)
    decrypt_all = []
    for i in range(len(Text) // 16):
        decrypt = Decryption_block(Text[0 + i * 16:16 + i * 16], Expansion_key, Rounds, size)
        decrypt_all.extend(decrypt)
    return int_in_str(decrypt_all), time.time() - start_time


def generate_key(size):
    Secret_key = [random.randint(0, 255) for _ in range(size)]
    return Secret_key

ASCII_p_2, ASCII_p_2_inv = ASCII()

# print(Encypt('Курсовая работа AES128', generate_key(32), 32))

# text = 'Курсовая работа AES128'
# print(f"Начальная строка:\n"
#       f"\t{text}\n"
#       f"Ключ:\n"
#       f"\t {Expansion_key[0]}")
# Text_all = str_in_int(text)

# encrypt = Encypt(Text_all, Rounds)
# print(f"Зашифрованная строка:\n"
#       f"\t{int_in_str(encrypt)}\n")
#
#
# decrypt = Decypt(encrypt, Rounds)
# print(f"Расшифрованная строка:\n"
#       f"\t{int_in_str(decrypt)}\n")