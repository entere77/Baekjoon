num_list=list(map(int, input().split()))
original=[1,1,2,2,2,8]
answer=[0 for i in range(6)]
for i in range(6):
    answer[i]=(original[i]-num_list[i])
for j in range(6):
    print(answer[j],end=' ')