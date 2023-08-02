rods=list(map(int, input().split()))
max_value=max(rods)
rods.remove(max_value)
if max_value>=sum(rods):
    max_value=sum(rods)-1
rods.append(max_value)
print(sum(rods))