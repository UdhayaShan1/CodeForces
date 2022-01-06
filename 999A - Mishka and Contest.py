n1 = input().split()
list1 = []
for i in n1:
    list1.append(int(i))
n2 = input().split()
list2 = []
for i in n2:
    list2.append(int(i))
    
k1 = 0
b1 = False
n = list1[0]
k = list1[1]
count = 0
while b1==False:
    if len(list2) == 0:
        print(count)
        break
    temp1 = list2[0]
    temp2 = list2[-1]
    if temp1 <= k:
        count+=1
        list2.pop(0)
        continue
    elif temp2 <= k:
        count+=1
        list2.pop(-1)
        continue
    else:
        print(count)
        break
