n1 = int(input())
list1 = []
list2 = []
for i in range(n1):
    x = input().split()
    temp = []
    for j in x:
        temp.append(int(j))
    list1.append(temp)
    x = input().split()
    temp = []
    for j in x:
        temp.append(int(j))
    list2.append(temp)
    
k1 = 0
b1 = False
while b1==False:
    ref_list1 = list1[k1]
    n = ref_list1[0]
    m = ref_list1[1]
    scores = list2[k1]
    if m > sum(scores):
        print(sum(scores))
    else:
        print(m)
    k1+=1
    if k1==len(list1):
        break
