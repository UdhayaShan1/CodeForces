n1 = int(input())
list1 = []
list2 = []
list3 = []
for i in range(n1):
    list1.append(int(input()))
    x = input().split()
    temp = []
    for j in x:
        temp.append(int(j))
    list2.append(temp)
    x = input().split()
    temp = []
    for j in x:
        temp.append(int(j))
    list3.append(temp)
    
k1 = 0
b1 = False
while b1==False:
    if k1==len(list3):
        break
    n = list1[k1]
    neck = list2[k1]
    bracelets = list3[k1]
    neck.sort()
    bracelets.sort()
    print(*neck)
    print(*bracelets)
    k1+=1 
    
