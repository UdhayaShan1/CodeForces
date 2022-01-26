n1 = int(input())
list1 = []
list2 = []
for i in range(n1):
    x = input().split()
    temp = []
    for j in x:
        temp.append(int(j))
    list1.append(temp)
    list2.append(input())
    
k1 = 0 
b1 = False
while b1==False:
    if k1==len(list1):
        break
    n = list1[k1][0]
    m = list1[k1][1]
    count = 0
    c1 = False
    ref_list = list(list2[k1])
    templist = ref_list.copy()
    while c1==False:
        change = 0
        for i in range(len(ref_list)):
            if i == 0:
                if ref_list[i] == "1":
                    continue
                else:
                    if ref_list[i+1] == "1":
                        templist[i] = "1"
                        change+=1
            elif i == len(ref_list)-1:
                if ref_list[i] == "1":
                    continue
                else:
                    if ref_list[i-1] == "1":
                        templist[i] = "1"
                        change+=1
            else:
                flag = 0
                if ref_list[i-1] == "1":
                    flag+=1
                if ref_list[i+1] == "1":
                    flag+=1
                if flag == 1:
                    if ref_list[i] == "1":
                        continue
                    else:
                        templist[i] = "1"
                        change+=1
        count+=1
        ref_list = templist.copy()
        if count >= m or change ==0:
            print(''.join(ref_list))
            break
    k1+=1 
        
