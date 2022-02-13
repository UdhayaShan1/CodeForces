x = input().split()
n = int(x[0])
m = int(x[1])

if n>=m:
    print(n-m)
else:
    count = 0
    b1 = False
    while b1==False:
        if m % 2 == 0:
            m = m/2
            count+=1
        else:
            m+=1
            count+=1
        if n>=m:
            count += (n-m)
            break
    print(int(count))
