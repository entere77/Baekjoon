a=input()
b=['c=','c-','dz=','d-','lj','nj','s=','z=']
for i in range(len(b)):
    if(a.find(b[i])!=-1):
        a = a.replace(b[i],'*')
print(len(a))