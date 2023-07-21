from string import ascii_lowercase

alphabet_list = list(ascii_lowercase)
string=list(input())

for i in alphabet_list:
    if i in string:
        print(string.index(i), end =' ')
    else:
        print(-1, end=' ')