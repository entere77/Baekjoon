while True:
    angles=[]
    a,b,c=map(int, input().split())
    angles.append(a)
    angles.append(b)
    angles.append(c)
    if sum(angles)==0:
        break
    else:
        max_value=max(angles)
        angles.remove(max_value)
        if max_value>=sum(angles):
            print('Invalid')
        else:
            angles.append(max_value)
            if len(set(angles))==1:
                print('Equilateral')
            elif len(set(angles))==2:
                print('Isosceles')
            else:
                print('Scalene')