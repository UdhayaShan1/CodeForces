n1 = input().split()
list1 = []
for i in n1:
    list1.append(int(i))
list2 = []
for i in range(list1[0]):
    
    list2.append(input())



rows_clear = []
colums_not_clear = []
for i in list2:
    if "S" not in i:
        rows_clear.append(1)
    if "S" in i:
        index_s = [j for j, x in enumerate(i) if x == "S"]
        for k in index_s:
            if k not in colums_not_clear:
                colums_not_clear.append(k)
    

colums_clear = []
total = len(rows_clear) * list1[-1]
for i in range(list1[-1]):
    if i not in colums_not_clear:
        colums_clear.append(i)
        
if len(colums_clear) == 0:
    total += 0
    print(total)
else:
    for i in colums_clear:
        total += list1[0] - len(rows_clear)
    print(total)
