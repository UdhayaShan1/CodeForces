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
    if k1==len(list2):
        break
    n = list1[k1]
    ref_list = list2[k1]
    list3 = []
    for i in range(len(ref_list)):
        if ref_list[i] > (i+1):
            list3.append(ref_list[i] - (i+1))
    if len(list3) == 0:
        print(0)
        k1+=1
        continue
    print(max(list3))
    k1+=1
