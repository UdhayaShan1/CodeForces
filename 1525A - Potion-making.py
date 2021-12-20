n1 = int(input())
list1 = []
for i in range(n1):
    list1.append(int(input()))
    
k1 = 0 
b1 = False
while b1==False:
    if k1==len(list1):
        break
    ref_litre = list1[k1]
    if ref_litre==100:
        print(1)
        k1+=1
        continue
    a = ref_litre
    b = 100 - ref_litre
    max1 = max(a,b)
    min1 = min(a,b)
    n1 = min1
    c1 = False
    while c1==False:
        if n1==0 or n1==1:
            break
        if max1 % n1 == 0 and min1 % n1 ==0:
            max1 = max1 / n1
            min1 = min1 / n1
            n1 = min1+1
        n1-=1
    
    print(int(max1+min1))
    k1+=1
    
            
        
