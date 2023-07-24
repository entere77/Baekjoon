n=int(input())
count_word=0
for i in range(n):
    string=input()
    err=0
    for j in range(len(string)-1):
        if string[j]!=string[j+1]:
            new=string[j+1:]
            if new.count(string[j])>0:
                err+=1                
    if err==0:
        count_word+=1
print(count_word)