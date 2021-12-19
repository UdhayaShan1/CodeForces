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
    list_even = []
    list_odd = []
    for i in ref_list:
        if i % 2==0:
            list_even.append(i)
        else:
            list_odd.append(i)
            
    list_odd += list_even
    finallist = []
    for i in list_odd:
        finallist.append(str(i))
    print(' '.join(finallist))
    k1+=1
    if k1==len(listn):
        break