H,M=map(int, input().split())
C=int(input())
if M+C>=60:
    if (M+C)//60+H>=24:
        print((M+C)//60+H-24,(M+C)%60)
    else:
        print((M+C)//60+H,(M+C)%60)
else:
    print(H,M+C)