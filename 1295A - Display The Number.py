n1 = int(input())
list1 = []
for i in range(n1):
    list1.append(int(input()))
 
k1 = 0
b1 = False
while b1==False:
    ref = list1[k1]
    if ref == 3:
        print(7)
    elif ref == 2:
        print(1)
    else:
        if ref % 2 == 0:
            print("1"*(ref//2))
        else:
            print("7"+(ref//2-1)*"1")
    k1+=1
    if k1==len(list1):
        break
