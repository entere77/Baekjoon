first, second=map(str,input().split())
reverse_first=first[::-1]
reverse_second=second[::-1]
if reverse_first>reverse_second:
    print(reverse_first)
else:
    print(reverse_second)