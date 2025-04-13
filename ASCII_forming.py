def ASCII():
    with open(r"ASCII_personal", encoding='UTF8') as file:
        mass = [s.rstrip('\n') for s in file.readlines()]
    file.close()

    ASCII_p_10 = dict()
    for i in range(len(mass)):
        value, key = mass[i].split('==')
        ASCII_p_10[key] = value

    ASCII_p_2 = dict()
    for i in ASCII_p_10:
        key, value = i, bin(int(ASCII_p_10[i]))[2:]
        if len(value) < 8:
            value = '0'*(8-len(value)) + value
        ASCII_p_2[key] = value

    ASCII_p_2_inv = dict()
    for i in ASCII_p_10:
        key, value = bin(int(ASCII_p_10[i]))[2:], i
        if len(key) < 8:
            key = '0' * (8 - len(key)) + key
        ASCII_p_2_inv[key] = value

    return ASCII_p_2, ASCII_p_2_inv