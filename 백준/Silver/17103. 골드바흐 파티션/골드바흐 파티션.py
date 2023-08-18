import sys

T = int(input())

table = [True for i in range(1000001)]

for i in range(2, 1001): #소수만 True로 만들기
    if table[i]:
        for j in range(i*2, 1000001, i):
            table[j] = False
            
table[0] = table[1] = False

for i in range(T):
    result = 0
    num = int(sys.stdin.readline())

    for j in range(2,int(num/2)+1):
        if table[j] and table[num-j]:
            result = result +1
            
    print(result)