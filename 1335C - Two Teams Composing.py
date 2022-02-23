n1 = int(input())
listn = []
list1 = []
for i in range(n1):
    listn.append(int(input()))
    x = input().split()
    temp = []
    for j in x:
        temp.append(int(j))
    list1.append(temp)
 
k1 = 0
b1 = False
while b1==False:
    n = listn[k1]
    ref_list = list1[k1]
    ref_list.sort()
    streak = 0
    ref1 = -1
    max1 = -1
    for i in range(len(ref_list)-1):
        if ref_list[i] == ref_list[i+1]:
            streak+=1
            if streak+1>max1:
                max1 = streak+1
                ref1 = ref_list[i]
        else:
            streak = 0
    list2 = []
    dict1 = {}
    for i in ref_list:
        if i != ref1 and i not in dict1:
            list2.append(i)
            dict1[i] = 1
        else:
            pass
    if max1 == -1:
        if n > 1:
            print(1)
        else:
            print(0)
    else:
        if len(list2) >= max1:
            print(max1)
        else:
            if max1 - len(list2) >= 2:
                print(len(list2)+1)
            else:
                print(len(list2))
    k1+=1
    if k1==len(list1):
        break
