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
    ref = list1[k1]
    n = ref[0]
    m = ref[1]
    x = ref[2]
    first_columns = math.ceil(x/n)
    if x%n == 0:
        first_rows = n
    else:
        first_rows = x%n
    
    value = (m) * (first_rows-1) + 1 + first_columns
    print(value-1)
    k1+=1
    if k1==len(list1):
        break
