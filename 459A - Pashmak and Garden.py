x = input().split()
x1 = int(x[0])
y1 = int(x[1])
x2 = int(x[2])
y2 = int(x[3])

if x2 != x1 and y2 != y1:
    if abs(x2-x1) != abs(y2-y1):
        print(-1)
    else:
        x3 = x2
        y3 = y1
        x4 = x1
        y4 = y2
        print(x3,y3,x4,y4)
else:
    if x2 == x1:
        diff = abs(y2-y1)
        print(x1+diff,y1,x1+diff,y2)
    elif y2 == y1:
        diff = abs(x2-x1)
        print(x1,y1-diff,x2,y2-diff)
