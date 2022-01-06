x = input().split()
list1 = []
for i in x:
    list1.append(int(i))
    
a = list1[0]
b = list1[1]
c = list1[2]

if (a+b)<=c:
    print(c-(a+b)+1)
elif (a+c)<=b:
    print(b-(a+c)+1)
elif (b+c)<=a:
    print(a-(b+c)+1)
else:
    print(0)
