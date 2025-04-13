def AddRoundKey(Text, round_key):
    New_Text = []
    for row in range(len(Text)):
        New_Text.append([])
        for column in range(len(Text[row])):
            bin_string = bin(int(Text[row][column], 16))[2:]
            bin_key = bin(int(round_key[row][column], 16))[2:]

            bin_string = '0' * (8 - len(bin_string)) + bin_string
            bin_key = '0' * (8 - len(bin_key)) + bin_key

            output = ''
            for num in range(len(bin_string)):
                output += '0' if bin_string[num] == bin_key[num] else "1"
            number = hex(int(output, 2))[2:].upper()
            number = '0'*(2-len(number)) + number
            New_Text[row].append(number)
    return New_Text