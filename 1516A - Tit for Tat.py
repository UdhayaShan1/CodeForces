n1 = int(input())
list1 = []
for i in range(n1):
    list1.append([])
    list1[i].append(input().split())
    x=input().split()
    temp = []
    for j in x:
        temp.append(int(j))
    list1[i].append(temp)
    
k1 = 0
b1 = False
while b1==False:
    if k1==len(list1):
        break
    n = int(list1[k1][0][0])
    k = int(list1[k1][0][-1])
    ref_list = list1[k1][-1]
    
    if len(ref_list) == 2:
        temp1 = ref_list[0]
        temp2 = ref_list[-1]
        if ref_list[0] <= k:
            ref_list[0] = 0
            ref_list[-1] = temp2+temp1
        else:
            ref_list[0] = temp1 - k
            ref_list[-1] = temp2 + k
        finallist = []
        for i in ref_list:
            finallist.append(str(i))
        print(' '.join(finallist))
        k1+=1
        continue
    c1 = False
    k2 = 0
    while c1==False:
        if k==0 or k2 == len(ref_list)-1:
            finallist = []
            for i in ref_list:
                finallist.append(str(i))
            
            print(' '.join(finallist))
            break
        diff = ref_list[k2]-0
        if diff <=k:
            temp1 = ref_list[k2]
            temp2 = ref_list[-1]
            ref_list[k2] = 0
            ref_list[-1] = temp2+temp1
            k2+=1
            k-= temp1
            continue
        if diff > k:
            temp1 = ref_list[k2]
            temp2 = ref_list[-1]
            ref_list[k2] = temp1-k
            ref_list[-1] = temp2+k
            k=0
            finallist = []
            for i in ref_list:
                finallist.append(str(i))
            print(' '.join(finallist))
            break
            
    k1+=1
        
