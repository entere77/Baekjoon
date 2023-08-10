import sys
input=sys.stdin.readline

n=int(input())
mine=set(map(int, input().split()))

m=int(input())
card=list(map(int, input().split()))

result=[]
for num in card:
    if num in mine:
        result.append(1)
    else:
        result.append(0)
print(*result)