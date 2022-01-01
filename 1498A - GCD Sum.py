n1 = int(input())
list1 = []
for i in range(n1):
    list1.append(int(input()))
    
k1 = 0
b1 = False
while b1==False:
    list2 = []
    ref_int = list1[k1]
    set2 = {}
    for i in range(1,31622+1):
        x = i **2
        y = i **3
        if x > ref_int and y >ref_int:
            break
        set2.add(x)
        set2.add(y)
        
    print(len(set2))
    k1+=1
    if k1==len(list1):
        break
        
