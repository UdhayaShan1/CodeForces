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
    columns = ref_list[0]
    rows = ref_list[1]
    x = ref_list[2]+1
    y = ref_list[3]+1
    print(max(((columns-x)*rows,(x-1)*rows,(rows-y)*columns,(y-1)*columns)))
    k1+=1
    if k1==len(list1):
        break
