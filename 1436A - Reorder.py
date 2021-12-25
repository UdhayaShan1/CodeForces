n1 = int(input())
list1 = []
list2 = []
for i in range(n1):
    x = input().split()
    temp1 = []
    for j in x:
        temp1.append(int(j))
    list1.append(temp1)
    x = input().split()
    temp1 = []
    for j in x:
        temp1.append(int(j))
    list2.append(temp1)
    
k1 = 0
b1 = False
while b1==False:
    if k1==len(list1):
        break
    n = list1[k1][0]
    m = list1[k1][-1]
    ref_list = list2[k1]
    k2 = 0
    count = 0
    c1 = False
    
    while c1==False:
        for i in range(k2+1,len(ref_list)+1):
            
            count += ref_list[i-1]/i
        k2+=1
        
        if k2==len(ref_list):
            
            if m- 0.00001 <= count and m+0.00001 >= count:
                print("YES")
            else:
                print("NO")
            k1+=1
            break
        
