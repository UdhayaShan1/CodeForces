n1 = int(input())
list_nm = []
list_directions = []
for i in range(n1):
    list_nm.append(input().split())
    list_directions.append([])
    for j in range(int(list_nm[i][0])):
        list_directions[i].append(input())
        
k1 = 0
b1 = False
while b1==False:
    if k1==len(list_nm):
        break
    ref_nm = list_nm[k1]
    n = int(ref_nm[0])
    m = int(ref_nm[1])
    ref_list = list_directions[k1]
    to_check_rightside = []
    to_check_down = ''
    for i in range(len(ref_list)-1):
        to_check_rightside.append(ref_list[i][-1])
    to_check_down = ref_list[-1]
    count_to_be_down = 0
    count_to_be_right = -1
    
    for i in to_check_rightside:
        if i != "D":
            count_to_be_down+=1
    for i in to_check_down:
        if i != "R":
            count_to_be_right +=1
    print(count_to_be_right+count_to_be_down)
    k1+=1
    
