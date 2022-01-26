x = input().split()
l = int(x[0])
r = int(x[1])
a = int(x[2])

min1 = min(l,r)
max1 = max(l,r)
diff = max1 - min1

if diff > 0:
    if diff > a:
        print((min1+a)*2)
    else:
        a-=diff
        divide = int(a/2)
        print((max1+divide)*2)
else:
    print((min1+int(a/2))*2)
