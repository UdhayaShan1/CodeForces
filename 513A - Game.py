x = input().split()
temp = []
for i in x:
    temp.append(int(i))
x = temp.copy()
n1 = x[0]
n2 = x[1]
k1 = x[2]
k2 = x[-1]
c1 = False
while c1==False:
    if n1==0:
        print("Second")
        break
    n1 -= 1
    if n2 == 0:
        print("First")
        break
    n2 -= 1
