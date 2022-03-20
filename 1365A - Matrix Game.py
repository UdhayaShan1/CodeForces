n1 = int(input())
list1 = []
list2 = []
for i in range(n1):
    x = input().split()
    temp = []
    for j in x:
        temp.append(int(j))
    list1.append(temp)
    list2.append([])
    for p in range(int(x[0])):
        x = input().split()
        temp = []
        for k in x:
            temp.append(int(k))
        list2[i].append(temp)

k1 = 0
b1 = False
while b1==False:
    ref1 = list1[k1]
    n = ref1[0]
    m = ref1[-1]
    ref_matrix = list2[k1]
    temp = []
    for i in ref_matrix:
        temp.append([0]*len(i))
    marked_rows = []
    marked_columns = []
    for i in range(len(ref_matrix)):
        index_one = [j for j, x in enumerate(ref_matrix[i]) if x == 1]
        if len(index_one) > 0:
            marked_rows.append(i)
        for j in index_one:
            marked_columns.append(j)
            
    turn = 0
    c1 = False
    while c1==False:
        flag = 0
        for i in range(len(ref_matrix)):
            if i in marked_rows:
                continue
            marked_rows.append(i)
            for j in range(len(ref_matrix[i])):
                if j in marked_columns:
                    continue
                marked_columns.append(j)
                flag+=1
                break
            if flag > 0:
                break
        if flag == 0 and turn % 2 == 0:
            print("Vivek")
            break
        if flag == 0 and turn % 2 != 0:
            print("Ashish")
            break
        turn+=1
    k1+=1
    if k1==len(list1):
        break
