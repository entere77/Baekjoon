n=int(input())
scores=list(map(int, input().split()))
max_score=max(scores)
s=0
for i in range(n):
    s+=scores[i]/max_score*100
print('%.2f'%(s/n))