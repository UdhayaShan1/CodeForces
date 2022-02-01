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
    if k1==len(list1):
        break
    n = listn[k1]
    ref_list = list1[k1]
    count = len([i for i, x in enumerate(ref_list) if x == 1])+1
    flag = 0
    for i in range(len(ref_list)-1):
        if ref_list[i] == 0 and ref_list[i+1] == 0:
            count = -1
            flag+=1
            break
        if ref_list[i] == 0:
            continue
    if flag>0:
        print(count)
        k1+=1
        continue
    for i in range(len(ref_list)-1):
        if ref_list[i] == 1 and ref_list[i+1] == 1:
            count+=4
    print(count)
    k1+=1
    continue
