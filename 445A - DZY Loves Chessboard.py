
x = input().split()
n = int(x[0])
m = int(x[1])
 
list1 = []
flag = 0
for i in range(n):
    list1.append([])
    for j in range(m):
        if flag % 2 == 0:
            if j % 2 == 0:
                list1[i].append("B")
            else:
                list1[i].append("W")
        else:
            if j % 2 == 0:
                list1[i].append("W")
            else:
                list1[i].append("B")
    flag+=1
 
list2 = []
for i in range(n):
    y = input()
    index_tochange = [j for j, x in enumerate(y) if x == "-"]
    for k in index_tochange:
        list1[i][k] = "-"
 
for i in list1:
    print(''.join(i))
