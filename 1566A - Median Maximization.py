import math
n1 = int(input())
list1 = []
for i in range(n1):
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
    ref_list = list1[k1]
    n = ref_list[0]
    s = ref_list[1]
    x = math.ceil(n/2)
    spaces = n - x + 1
    print(int(s//spaces))
    k1+=1
