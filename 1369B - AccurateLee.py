n1 = int(input())
list1 = []
list2 = []
for i in range(n1):
    list1.append(int(input()))
    list2.append(input())
 
k1 = 0
b1 = False
while b1==False:
    if k1==len(list2):
        break
    ref_n = list1[k1]
    ref_str = list2[k1]
    first_one = -1
    last_zero = -1
    flag_one = 0
    for i in range(ref_n):
        if ref_str[i] == "1" and flag_one == 0:
            first_one = i
            flag_one+=1
        if ref_str[i] == "0":
            last_zero = i
    if last_zero < first_one:
        print(ref_str)
        k1+=1
        continue
    ref2 = ref_str[first_one:last_zero+1]
    ref3 = ref_str[0:first_one] + "0" + ref_str[last_zero+1:]
    print(ref3)
    k1+=1
