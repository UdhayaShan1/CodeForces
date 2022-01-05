n1 = int(input())
list1 = []
list2 = []
for i in range(n1):
    list1.append(int(input()))
    list2.append(input())
    
    
k1 = 0
b1 = False
while b1==False:
    if k1==len(list1):
        break
    digits = list1[k1]
    ref_list = list2[k1]
    if int(ref_list) == 0:
        print(0)
        k1+=1
        continue
    c1 = False
    count = 0
    for i in ref_list:
        count+=int(i)
    count1 = 0
    for i in ref_list[:-1]:
        if i !="0":
            count1+=1
    
    print(count1+count)
    k1+=1
    continue
    
        
    
