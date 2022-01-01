x = input().split()
list1 = []
for i in x:
    list1.append(int(i))
    
if sum(list1) % 2 != 0:
    print("NO")
else:
    x = sum(list1) / 2
    if x in list1:
        print("YES")
    else:
        b1 = False
        k1 = 0
        while b1==False:
            temp = list1.copy()
            temp.remove(list1[k1])
            if x - list1[k1] in temp:
                print("YES")
                break
            else:
                k1+=1
            if k1==len(list1):
                print("NO")
                break
