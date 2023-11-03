import sys
def solution(c):
    row_num=[0]*(n+1)
    col_num=[0]*(m+1)
    res=1e9
    s=[[0]*(m+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            if ((i+j)%2==1 and chess[i-1][j-1]==c) or ((i+j)%2==0 and chess[i-1][j-1]!=c): 
                row_num[i]+=1
                col_num[j]+=1
                s[i][j]=1
            s[i][j]=s[i-1][j-1]+row_num[i]+col_num[j]-s[i][j]
    for i in range(1, n+1):
        row_num[i]+=row_num[i-1]
    for i in range(1, m+1):
        col_num[i]+=col_num[i-1]
    for i in range(k, n+1):
        for j in range(k, m+1):
            temp=s[i][j]-s[i-k][j]-s[i][j-k]+s[i-k][j-k]
            res=min(res, temp)
    return res
n, m, k =map(int, sys.stdin.readline().split())
chess=[list(sys.stdin.readline().strip('\n')) for _ in range(n)]
print(min(solution('B'), solution('W')))