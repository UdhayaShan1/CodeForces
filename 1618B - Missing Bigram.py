n1 = int(input())
list1 = []
list2 = []
for i in range(n1):
    list1.append(int(input()))
    x = input().split()
    list2.append(x)
    
k1 = 0
b1 = False
while b1==False:
    if k1==len(list1):
        break
    n = list1[k1]
    ref_list = list2[k1]
    c1 = False
    if len(ref_list) == 1:
        print(ref_list[0]+"a")
        k1+=1
        continue
    k2 = 0
    temp1 = ''
    while c1==False:
        if ref_list[k2][-1] == ref_list[k2+1][0]:
            temp1 = ref_list[k2] + ref_list[k2+1][-1]
            ref_list[k2] = temp1
            ref_list.pop(k2+1)
            k2 = 0
        else:
            temp1 = ref_list[k2]+ref_list[k2+1]
            ref_list[k2] = temp1
            ref_list.pop(k2+1)
        if len(ref_list) == 1:
            break
    str2 = ''.join(ref_list)
    print(str2+ (int(n) - len(str2))*"a")
    k1+=1
