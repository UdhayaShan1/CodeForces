n1 = int(input())
list1 = []
list2 = []
for i in range(n1):
    list1.append(int(input()))
    list2.append([])
    for j in range(list1[i]):
        list2[i].append(list(input()))
 
k1 = 0
b1 = False
while b1==False:
    n = list1[k1]
    ref = list2[k1]
    
    for i in range(n):
        if ref[i][-1] == "1":
            ref[i][-1] = "2"
        else:
            continue
    for i in range(n):
        if ref[n-1][i] == "1":
            ref[n-1][i] = "2"
    
    start_row = n-2
    d1 = False
    while d1==False:
        for i in range(n-2,-1,-1):
            if ref[start_row][i] == "1":
                if ref[start_row][i+1] == "2" or ref[start_row+1][i] == "2":
                    ref[start_row][i] = "2"
                else:
                    continue
        start_row -= 1
        if start_row <= -1:
            break
    flag = 0
    for i in ref:
        if "1" in i:
            flag+=1
            break
    if flag == 1:
        print("NO")
    else:
        print("YES")
        
    k1+=1
    if k1==len(list1):
        break
