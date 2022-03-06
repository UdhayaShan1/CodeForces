n1 = int(input())
if n1==1:
    print(1)
elif n1==2:
    print(3)
else:
    start = 2
    start1 = 1
    count = 0
    b1 = False
    while b1==False:
        count += (n1 - start + 1) * start1
        start += 1
        start1 += 1
        if start == n1:
            break
    print(count+n1+(n1-1))
