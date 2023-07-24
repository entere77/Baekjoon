import sys

string=input()
string=string.upper()
list1=list(set(string))
count_list=[0 for i in range(len(list1))]
for j in range(len(list1)):
    count_list[j]=string.count(list1[j])

max=0
duplicated_max=0
for k in range(len(count_list)):
    if max<count_list[k]:
        max=count_list[k]
    elif max==count_list[k]:
        duplicated_max=count_list[k]
        max=duplicated_max

if max==duplicated_max:
    print('?')
else:
    index_n=count_list.index(max)
    print(list1[index_n])