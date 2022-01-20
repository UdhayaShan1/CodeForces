x = input().split()
list1 = []
for i in x:
    list1.append(int(i))
y = list1[0]
b = list1[1]
r = list1[-1]
b1 = False
while b1==False:
    if (y+1) <= b and (y+2) <= r:
        print(y+y+1+y+2)
        break
    y-=1
