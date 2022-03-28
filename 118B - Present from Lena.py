n1 = int(input())
total = n1*2+1 + n1*2
list1 = []
count = 1
for i in range(n1+1):
    list1.append([])
    list1[i].append(" "*((total-count)//2))
    for j in range(0,i+1):
        list1[i].append(str(j))
        list1[i].append(" ")
    for j in range(i-1,-1,-1):
        list1[i].append(str(j))
        if j != 0:
            list1[i].append(" ")
    count+=4
 
list1[0].pop(-1)
 
list1 += (list1[0:n1])[::-1]
 
for i in list1:
    print(''.join(i))
