x = input().split()
list1 = []
for i in x:
    list1.append(int(i))
x = input().split()
list2 = []
for i in x:
    list2.append(int(i))
    
x = list1[0]
y = list1[1]
z = list1[2]

a = list2[0]
b = list2[1]
c = list2[2]

b1 = False
while b1==False:
    if x>a:
        print("NO")
        break
    a -= x
    if y > a+b:
        print("NO")
        break
    if z> (a+b-y)+c:
        print("NO")
        break
    print("YES")
    break
