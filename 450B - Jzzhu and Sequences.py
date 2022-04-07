x1 = input().split()
x = int(x1[0])
y = int(x1[1])
list1 = [x,y]
b1 = False
f1 = x
f2 = y
while b1==False:
    list1.append(f2-f1)
    a = f2-f1
    b = f2
    f2 = a
    f1 = b
    if len(list1) == 6:
        break
 
n1 = int(input())
pos = n1 % 6
if pos == 0:
    fn = list1[-1]
    print(fn % 1000000007)
else:
    fn = list1[pos-1]
    print(fn % 1000000007)
