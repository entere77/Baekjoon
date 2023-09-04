import sys
from collections import deque
n=int(input())
a=list(map(int, input().split()))
b=list(map(int, input().split()))
m=int(input())
c=list(map(int, input().split()))
d=deque([])
for i in range(n):
    if a[i]==0:
        d.appendleft(b[i])
if d==[]:
    print(*c)
else:
    for i in range(m):
        d.append(c[i])
        print(d.popleft(),end=" ")