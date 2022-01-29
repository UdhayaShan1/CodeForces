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
    s = ref_list[0]
    a = ref_list[1]
    b = ref_list[2]
    c = ref_list[3]
    choco_in_set = a+b
    price_set = a*c
    count = (s//price_set) * choco_in_set
    count += (s-((s//price_set) * price_set)) // c
    print(count)
    k1+=1
    if k1==len(list1):
        break
