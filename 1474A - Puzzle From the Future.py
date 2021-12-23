n1 = int(input())
list1 = []
list2 = []
for i in range(n1):
    list1.append(int(input()))
    list2.append(input())
    
k1 = 0
b1 = False
while b1==False:
    ref_len = list1[k1]
    ref_b = list2[k1]
    a_temp = []
    final = []
    k2 = 0
    count = 0
    for i in ref_b:
        diff = 2 - int(i)
        if count == 0:
            a_temp.append(1)
            final.append(int(i)+1)
            count+=1
            continue
        if final[k2] == 2:
            
            a_temp.append(1-int(i))
            final.append(1)
            k2+=1
            continue
        if final[k2] == 1:
            if int(i) == 0:
                a_temp.append(0)
                final.append(0)
            elif int(i) == 1:
                a_temp.append(1)
                final.append(2)
            k2+=1
            continue
        if final[k2] == 0:
            a_temp.append(1)
            final.append(int(i)+1)
            k2+=1
            continue
    finallist = []
    for i in a_temp:
        finallist.append(str(i))
    print(''.join(finallist))
    k1+=1
    if k1==len(list1):
        break
                
            
        
