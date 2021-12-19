n1 = int(input())
list1 = []
list2 = []
for i in range(n1):
    x = input().split()
    list1.append(x)
    list2.append(input())
 
b1 = False
k1 = 0
while b1==False:
    if k1==len(list1):
        break
    ref_list = list1[k1]
    y = list2[k1]
    x1 = int(ref_list[0])
    y1 = int(ref_list[-1])
    index_r = [i for i, x in enumerate(y) if x == "R"]
    index_l = [i for i, x in enumerate(y) if x == "L"]
    index_u = [i for i, x in enumerate(y) if x == "U"]
    index_d = [i for i, x in enumerate(y) if x == "D"]
 
    if x1 >=0:
        if y1 >=0:
            diff_x = x1-0
            diff_y = y1-0
            if diff_x <= len(index_r) and diff_y <= len(index_u):
                print("YES")
            else:
                print("NO")
        else:
            diff_x = x1-0
            diff_y = abs(y1-0)
            if diff_x <= len(index_r) and diff_y <= len(index_d):
                print("YES")
            else:
                print("NO")
    else:
        if y1 >= 0:
            diff_x = abs(x1-0)
            diff_y = y1-0
            if diff_x <= len(index_l) and diff_y <= len(index_u):
                print("YES")
            else:
                print("NO")
        else:
            diff_x = abs(x1-0)
            diff_y = abs(y1-0)
            if diff_x <= len(index_l) and diff_y <= len(index_d):
                print("YES")
            else:
                print("NO")
    k1+=1
