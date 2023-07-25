grade={'A+':4.5,
'A0':4.0,
'B+':3.5,
'B0':3.0,
'C+':2.5,
'C0':2.0,
'D+':1.5,
'D0':1.0,
'F':0.0}
sum_score=0
sum_major=0

for i in range(20):
    name, score, rank=input().split()
    if rank!='P':
        sum_score+=float(score)
        sum_major+=float(score)*grade[rank]
print('%.6f'%(sum_major/sum_score))