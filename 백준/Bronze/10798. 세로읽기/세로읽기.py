words = [input() for _ in range(5)]
max_len=0
for i in range(5):
    if max_len<len(words[i]):
        max_len=len(words[i])
for column in range(max_len):
    for row in range(5):
        if column<len(words[row]):
            print(words[row][column], end='')