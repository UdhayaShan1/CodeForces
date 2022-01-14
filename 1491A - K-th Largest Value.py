x = input().split()
x1 = input().split()
list1 = []
no_one = 0
no_zero = 0
for j in x1:
    if int(j) == 0:
        no_zero+=1
    elif int(j) == 1:
        no_one+=1
    list1.append(int(j))
    
queries = []    
for i in range(int(x[1])):
    x2 = input().split()
    temp = []
    for j in x2:
        temp.append(int(j))
    queries.append(temp)
    
k1 = 0
b1 = False
while b1==False:
    if k1==len(queries):
        break
    n = int(x[0])
    ref_query = queries[k1]
    if ref_query[0] == 2:
        if ref_query[1] <= no_one:
            print(1)
        else:
            print(0)
    else:
        temp2 = list1[ref_query[1]-1]
        list1[ref_query[1]-1] = 1 - temp2
        if temp2 == 0:
            no_one+=1
            no_zero-=1
        else:
            no_zero+=1
            no_one-=1
    k1+=1
    continue
