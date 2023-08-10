n=int(input())

info=[]
for i in range(n):
    age, word = input().split()  
    info.append([age,word,i])
    
info.sort(key=lambda x : (int(x[0]), int(x[2])))
for j in info:
    print(j[0],j[1])