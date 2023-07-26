alphabet = [chr(a) for a in range(65, 91)]
N,B=input().split()
B=int(B)
j=len(N)-1
total=0
for i in range(len(N)):
    if N[i] in alphabet:
        total+=(B**(j-i))*(ord(N[i])-55)
    else:
        total+=(B**(j-i))*(ord(N[i])-48)
print(total)