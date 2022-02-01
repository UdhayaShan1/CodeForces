n1 = int(input())

if n1 == 1:
    print(-1)
elif n1 == 2 or n1 == 3:
    print(2,2)
else:
    b1 = False
    while b1==False:
        if n1%2 == 0:
            break
        n1-=1
    print(n1,2)
