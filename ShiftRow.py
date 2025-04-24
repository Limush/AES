def ShiftRow(Text, Rounds, size):
    shift = [0, 1, 2, 3] if Rounds == 10 or Rounds == 12 else [0, 1, 3, 4]
    Text = [Text[i:i+(size//4)] for i in range(0, len(Text), (size//4))]
    New_Text = [Text[num][shift[num]:] + Text[num][:shift[num]] for num in range(len(Text))]
    Text = []
    for i in New_Text:
        Text.extend(i)
    return Text


def ShiftRowInv(Text, Rounds, size):
    shift = [0, 1, 2, 3] if Rounds == 10 or Rounds == 12 else [0, 1, 3, 4]
    Text = [Text[i:i+(size//4)] for i in range(0, len(Text), (size//4))]
    New_Text = [Text[num][-shift[num]:] + Text[num][:-shift[num]] for num in range(len(Text))]
    Text = []
    for i in New_Text:
        Text.extend(i)
    return Text