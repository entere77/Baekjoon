n,m=map(int, input().split())
person_h=set()
for i in range(n):
    name=input()
    person_h.add(name)
    
person_s=set()
for j in range(m):
    name=input()
    person_s.add(name)

hs=sorted(list(person_h&person_s))
print(len(hs))
for name in hs:
    print(name)