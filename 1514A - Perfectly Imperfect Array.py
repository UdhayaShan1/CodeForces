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
    ref_n = listn[k1]
    ref_list = list1[k1]
    count = 0
    for i in ref_list:
        if i**0.5 - int(i**0.5) == 0:
            count+=1
    if count < len(ref_list):
        print("YES")
    else:
        print("NO")
    k1+=1
    if k1==len(list1):
        break
