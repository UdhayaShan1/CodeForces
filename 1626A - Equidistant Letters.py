n1 = int(input())
list1 = []
for i in range(n1):
    list1.append(input())
    
k1 = 0
b1 = False
while b1==False:
    ref_str = list1[k1]
    ref_set = list(set(ref_str))
    list2 = []
    for i in ref_set:
        length = len([j for j, x in enumerate(ref_str) if x == i])
        if length == 2:
            list2.append(i*2)
        else:
            list2.append(i*length)
    print(''.join(list2))
    k1+=1
    if k1==len(list1):
        break
