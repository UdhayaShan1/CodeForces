n1 = int(input())
list1 = []
list2 = []
for i in range(n1):
    list1.append(int(input()))
    list2.append(input())
    
k1 = 0
b1 = False
while b1==False:
    n = list1[k1]
    ref_list = list(list2[k1])
    index_r = [i for i, x in enumerate(ref_list) if x == "r"]
    k2 = 0
    for i in index_r:
        temp1 = ref_list[k2]
        ref_list[i] = temp1
        ref_list[k2] = "r"
        k2+=1
    print(''.join(ref_list))
    k1+=1
    if k1==len(list2):
        break
