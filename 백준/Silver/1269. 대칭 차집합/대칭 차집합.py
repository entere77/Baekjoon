a,b=map(int, input().split())
a_set=set(list(map(int, input().split())))
b_set=set(list(map(int, input().split())))

duplicated=a_set&b_set
length=len(list(duplicated))
print(a+b-length*2)