n1 = int(input())
listn = []
list1 = []
for i in range(n1):
    x = int(input())
    listn.append(x)
    list1.append([])
    for j in range(x):
        list1[i].append(input())
        
 
k1 = 0
b1 = False
while b1==False:
    if k1==len(list1):
        break
    ref_list = ''.join(list1[k1])
    ref_n = listn[k1]
    list2 = []
    for i in list1[k1]:
        list2.append(list(i))
    
    indices_asterik_simpler = []
    indices_backup = []
    row = []
    count = -1
    for i in list1[k1]:
        count+=1
        if len([j for j, x in enumerate(i) if x == "*"])>0:
            indices_asterik_simpler.append([j for j, x in enumerate(i) if x == "*"][0])
            indices_backup.append([j for j, x in enumerate(i) if x == "*"])
            row.append(count)   
 
    if len(row) > 1:
        if (indices_asterik_simpler[0] == indices_asterik_simpler[1]) and indices_asterik_simpler[0] == 0 and len(row)>1:
            for i in row:
                list2[i][1] = '*'
        elif (indices_asterik_simpler[0] == indices_asterik_simpler[1]) and indices_asterik_simpler[0] == ref_n-1 and len(row)>1:
            for i in row:
                list2[i][-2] = '*'
        elif (indices_asterik_simpler[0] == indices_asterik_simpler[1]) and indices_asterik_simpler[0] != 0 and indices_asterik_simpler[0] != ref_n-1 and len(row)>1:
            for i in row:
                list2[i][indices_asterik_simpler[0]+1] = '*'
        else:
            if len(row)>1:
                max1 = max(indices_asterik_simpler)
                min1 = min(indices_asterik_simpler)
                count1 = -1
                for i in row:
                    count1+=1
                    if indices_asterik_simpler[count1] == max1:
                        list2[i][min1] = '*'
                    else:
                        list2[i][max1] = '*'
    else:
        max1 = max(indices_backup[0][0],indices_backup[0][1])
        min1 = min(indices_backup[0][0],indices_backup[0][1])
        if row[0] == ref_n-1:
            list2[-2][min1] = '*'
            list2[-2][max1] = '*'
        elif row[0] == 0:
            list2[1][min1] = '*'
            list2[1][max1] = '*'
        else:
            list2[row[0]+1][min1] = '*'
            list2[row[0]+1][max1] = '*'
        
    
    for i in list2:
        print(''.join(i))
    k1+=1
