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
    n = list1[k1]
    ref_list = list2[k1]
    if sum(ref_list) % n == 0:
        print(0)
    else:
        print(1)
    k1+=1
    if k1==len(list1):
        break
