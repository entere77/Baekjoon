str=list(map(int, input()))
str.sort(reverse=True)
for i in range(len(str)):
    print(str[i], end='')