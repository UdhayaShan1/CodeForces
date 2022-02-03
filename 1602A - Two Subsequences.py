n1 = int(input())
list1 = []
for i in range(n1):
    list1.append(input())
    
k1 = 0
b1 = False
while b1==False:
    ref_str = list1[k1]
    min1 = 'z'
    for i in range(len(ref_str)):
        if ref_str[i]<min1:
            min1 = ref_str[i]
    list2 = list(ref_str)
    list2.remove(min1)
    print(min1,''.join(list2))
    k1+=1
    if k1==len(list1):
        break
