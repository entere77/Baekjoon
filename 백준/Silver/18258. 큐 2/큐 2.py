import sys
import collections

input = sys.stdin.readline
n = int(input())

a=collections.deque([])

for i in range(n):

    b = input()
    b = b.strip()
    if b == 'front':
        if len(a) == 0:
            print(-1)
        else:
            print(a[0])
    elif b == 'back':
        if len(a) == 0:
            print(-1)
        else:
            print(a[-1])
    elif b =='size':
        print(len(a))
    elif b == 'pop':
        if len(a) == 0:
            print(-1)
        else:
            print(a[0])
            a.popleft()
    elif b == 'empty':
        if len(a) == 0:
            print(1)
        else:
            print(0)
    else:
        c = b.split()
        if c[0] == 'push':
            a.append(int(c[1]))
