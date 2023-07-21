n=int(input())
for i in range(n):
    num, string=map(str, input().split())
    answer=''
    for c in string:
        answer+=c*int(num)
    print(answer)