n1 = int(input())
list1 = []
for i in range(n1):
    x = input().split()
    temp = []
    for j in x:
        temp.append(int(j))
    list1.append(temp)
    
k1 = 0
b1 = False
while b1==False:
    if k1==len(list1):
        break
    ref_list = list1[k1]
    ref_one = ref_list[0:2]
    ref_two = ref_list[2:]
    if ref_one[0] == ref_two[0]:
        if ref_two[0] + 1 in range(ref_two[0],ref_two[1]+1):
            print(ref_one[0],ref_two[0]+1)
            k1+=1
            continue
        elif ref_one[0] + 1 in range(ref_one[0],ref_one[1]+1):
            print(ref_one[0]+1,ref_two[0])
            k1+=1
            continue
    else:
        print(ref_one[0],ref_two[0])
        k1+=1
        continue
