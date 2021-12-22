n1 = int(input())
listn = []
list1 = []
for i in range(n1):
    listn.append(int(input()))
    x = input().split()
    temp = []
    for j in x:
        temp.append(int(j))
    list1.append(temp)
    
k1 = 0
b1 = False
while b1==False:
    refn = listn[k1]
    ref_list = list1[k1]
    list_areas = []
    k2 = 0
    for i in range(len(ref_list)):
        start = ref_list[i]
        for j in ref_list[i+1:]:
            area = 0.5 * (j- ref_list[i]) * 1
            if area not in list_areas:
                list_areas.append(area)
    print(len(list_areas))
    k1+=1
    if k1==len(list1):
        break
