from AES import Encypt, Decypt, generate_key

import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
import numpy as np
import random
import math


def arrayINT_to_hex(q):
    h = ''
    for i in q:
        num = str(hex(i)[2:])
        h += '0' + num if len(num) == 1 else num
    return f"0x{h}"


def hexSTR_to_array(h):
    h_2 = []
    for i in range(2, len(h), 2):
        num1 = ord(h[i]) - 87 if h[i] in ['a', 'b', 'c', 'd', 'e', 'f'] else int(h[i])
        num2 = ord(h[i + 1]) - 87 if h[i + 1] in ['a', 'b', 'c', 'd', 'e', 'f'] else int(h[i + 1])
        h_2.append(num1 * 16  + num2)
    return h_2


def New_key(size):
    gen_key = generate_key(size)
    scrol_key_en.delete(1.0, tkinter.END)
    scrol_key_en.insert(tkinter.END, arrayINT_to_hex(gen_key))
    return


def Enc128():
    New_key(16)
    Key = scrol_key_en.get('1.0', 'end-1c')
    Text = entry_text_en.get()
    text_en, time = Encypt(Text, hexSTR_to_array(Key), 16)
    scrol_text_en.delete(1.0, tkinter.END)
    scrol_text_en.insert(tkinter.END, text_en)
    lbl_2_en.configure(text=round(time, 6))
    return


def Enc192():
    New_key(24)
    Key = scrol_key_en.get('1.0', 'end-1c')
    Text = entry_text_en.get()
    text_en, time = Encypt(Text, hexSTR_to_array(Key), 24)
    scrol_text_en.delete(1.0, tkinter.END)
    scrol_text_en.insert(tkinter.END, text_en)
    lbl_2_en.configure(text=round(time, 6))
    return


def Enc256():
    New_key(32)
    Key = scrol_key_en.get('1.0', 'end-1c')
    Text = entry_text_en.get()
    text_en, time = Encypt(Text, hexSTR_to_array(Key), 32)
    scrol_text_en.delete(1.0, tkinter.END)
    scrol_text_en.insert(tkinter.END, text_en)
    lbl_2_en.configure(text=round(time, 6))
    return


def Dec128():
    Key = scrol_key_en.get('1.0', 'end-1c')
    if Key:
        Text = entry_text_de.get()
        text_en, time = Decypt(Text, hexSTR_to_array(Key), 16)
        scrol_text_de.delete(1.0, tkinter.END)
        scrol_text_de.insert(tkinter.END, text_en)
        lbl_2_de.configure(text=round(time, 6))
    else:
        print(f"ключ не соответствует норме")
    return


def Dec192():
    Key = scrol_key_en.get('1.0', 'end-1c')
    Text = entry_text_de.get()
    if Key:
        text_en, time = Decypt(Text, hexSTR_to_array(Key), 24)
        scrol_text_de.delete(1.0, tkinter.END)
        scrol_text_de.insert(tkinter.END, text_en)
        lbl_2_de.configure(text=round(time, 6))
    else:
        print(f"ключ не соответствует норме")
    return


def Dec256():
    Key = scrol_key_en.get('1.0', 'end-1c')
    Text = entry_text_de.get()
    if Key:
        text_en, time = Decypt(Text, hexSTR_to_array(Key), 32)
        scrol_text_de.delete(1.0, tkinter.END)
        scrol_text_de.insert(tkinter.END, text_en)
        lbl_2_de.configure(text=round(time, 6))
    else:
        print(f"ключ не соответствует норме")
    return


AES_window = Tk()
AES_window.title("AES")
AES_window.geometry("1500x700+100+20")


# Шифр
lbl_1_en = Label(AES_window, text='Время        ->', font=("Time new roman", 14))
lbl_1_en.place(x=20, y=610)

lbl_2_en = Label(AES_window, text='', font=("Time new roman", 14))
lbl_2_en.place(x=140, y=610)

lbl_3_en = Label(AES_window, text='Мб память ->', font=("Time new roman", 14))
lbl_3_en.place(x=20, y=640)

lbl_4_en = Label(AES_window, text='-', font=("Time new roman", 14))
lbl_4_en.place(x=140, y=640)

entry_text_en = Entry(AES_window, width=41, font='times 12')
entry_text_en.place(x=20, y=120)

scrol_text_en = scrolledtext.ScrolledText(AES_window, width=41, height=28)
scrol_text_en.place(x=20, y=150)

scrol_key_en = scrolledtext.ScrolledText(AES_window, width=41, height=5)
scrol_key_en.place(x=20, y=20)


button_AES128_en = Button(AES_window, width=15, height=9, text='AES128', command=Enc128)
button_AES128_en.place(x=380, y=120)

button_AES192_en = Button(AES_window, width=15, height=9, text='AES192', command=Enc192)
button_AES192_en.place(x=380, y=285)

button_AES256_en = Button(AES_window, width=15, height=9, text='AES256', command=Enc256)
button_AES256_en.place(x=380, y=455)

#Расшифр
lbl_1_de = Label(AES_window, text='Время        ->', font=("Time new roman", 14))
lbl_1_de.place(x=530, y=610)

lbl_2_de = Label(AES_window, text='', font=("Time new roman", 14))
lbl_2_de.place(x=650, y=610)

lbl_3_de = Label(AES_window, text='Мб память ->', font=("Time new roman", 14))
lbl_3_de.place(x=530, y=640)

lbl_4_de = Label(AES_window, text='-', font=("Time new roman", 14))
lbl_4_de.place(x=650, y=640)
#
entry_text_de = Entry(AES_window, width=41, font='times 12')
entry_text_de.place(x=530, y=120)

scrol_text_de = scrolledtext.ScrolledText(AES_window, width=41, height=28)
scrol_text_de.place(x=530, y=150)

scrol_key_de = scrolledtext.ScrolledText(AES_window, width=41, height=5)
scrol_key_de.place(x=530, y=20)

button_AES128_de = Button(AES_window, width=15, height=9, text='AES128', command=Dec128)
button_AES128_de.place(x=890, y=120)

button_AES192_de = Button(AES_window, width=15, height=9, text='AES192', command=Dec192)
button_AES192_de.place(x=890, y=285)

button_AES256_de = Button(AES_window, width=15, height=9, text='AES256', command=Dec256)
button_AES256_de.place(x=890, y=455)


AES_window.mainloop()



