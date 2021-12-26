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
    ref_n = list1[k1]
    ref_str = list(list2[k1])
    ref2 = ref_str.copy()
    ref2.sort()
    k2 = 0
    c1 = False
    diffcount = 0
    
    while c1==False:
        if ref2[k2] != ref_str[k2]:
            diffcount+=1
        k2+=1
        if k2==len(ref_str):
            print(diffcount)
            break
    k1+=1
