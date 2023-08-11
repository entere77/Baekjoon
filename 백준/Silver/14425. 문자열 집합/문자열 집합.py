n,m=map(int, input().split())
set_str=[]
for _ in range(n):
    set_str.append(input())
    
test_str=[]
for _ in range(m):
    test_str.append(input())

cnt=0
for i in test_str:
    if i in set_str:
        cnt+=1
print(cnt)