n1 = int(input())
list1 = []
list2 = []
list3 = []
for i in range(n1):
    x = input().split()
    temp = []
    for j in x:
        temp.append(int(j))
    list1.append(temp)
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
    n = list1[k1][0]
    k = list1[k1][1]
    ref_list1 = list2[k1]
    ref_list2 = list3[k1]
    
    c1 = False
    while c1==False:
        flag=0
        for i in range(len(ref_list1)):
            if k >= ref_list1[i]:
                k+= ref_list2[i]
                flag+=1
                ref_list2.pop(i)
                ref_list1.pop(i)
                break
        if flag == 0:
            print(k)
            break
    k1+=1
    if k1==len(list3):
        break
            
