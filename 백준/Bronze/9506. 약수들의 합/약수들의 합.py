while True:
    n=int(input())
    if n==-1:
        break
    factor_list=[]
    for i in range(1,n+1):
        if n%i==0:
            if n!=i:
                factor_list.append(i)
    if sum(factor_list)==n:
        print(n,'=',end=' ')
        for j in factor_list:
            if j == factor_list[-1]:
                print(j)
            else:
                print(j,'+',end=' ')
    else:
        print(n,'is NOT perfect.')