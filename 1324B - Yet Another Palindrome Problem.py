n1 = int(input())
list1 = []
list2 = []
for i in range(n1):
    list1.append(int(input()))
    x = input().split()
    temp = []
    for j in x:
        temp.append(int(j))
    list2.append(temp)
 
k1 = 0
b1 = False
while b1==False:
    ref_n = list1[k1]
    ref_list = list2[k1]
    start = 0
    c1 = False
    while c1==False:
        if start == len(ref_list)-2:
            print("NO")
            break
        ref1 = ref_list[start]
        flag = 0
        for i in range(start+2,len(ref_list)):
            if ref_list[i] == ref1:
                flag+=1
                break
        if flag == 1:
            print("YES")
            break
        else:
            start+=1
    k1+=1
    if k1==len(list1):
        break
