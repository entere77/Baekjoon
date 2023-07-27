n = int(input())

for i in range(n):
    cent = int(input())

    quarter = cent // 25
    cent = cent % 25

    dime = cent // 10
    cent = cent % 10

    nickel = cent // 5
    cent = cent % 5

    penny = cent // 1

    if (cent % 1)==0 :
        print(quarter, dime, nickel, penny)