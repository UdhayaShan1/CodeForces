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
    if k1==len(listn):
        break
    ref_n = listn[k1]
    ref_list = list1[k1]
    flag = 0
    for i in range(ref_n-1):
        if ref_list[i+1] != ref_list[i]:
            flag+=1
            break
        else:
            continue
    if flag>0:
        print(1)
    else:
        print(ref_n)
    k1+=1
    if k1==len(listn):
        break
        
