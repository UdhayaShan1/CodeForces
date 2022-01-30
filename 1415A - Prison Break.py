n1 = int(input())
list1 = []
for i in range(n1):
    x = input().split()
    temp = []
    for j in x:
        temp.append(int(j))
    list1.append(temp)
    
k1 = 0
b1 = False
while b1==False:
    ref_list = list1[k1]
    rows = ref_list[0]
    columns = ref_list[1]
    r = ref_list[2]
    c = ref_list[3]
    print(max((rows-r+columns-c),(r-1+c-1),(r-1+columns-c),(rows-r+c-1)))
    k1+=1
    if k1==len(list1):
        break
