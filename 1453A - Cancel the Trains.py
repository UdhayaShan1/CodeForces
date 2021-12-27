n1 = int(input())
list1 = []
list2 = []
list3 = []
for i in range(n1):
    list1.append(input().split())
    x = input().split()
    temp = []
    for j in x:
        temp.append(int(j))
    list2.append(temp)
    x = input().split()
    temp = []
    for j in x:
        temp.append(int(j))
    list3.append(temp)
    
k1 = 0
b1 = False
while b1==False:
    if k1==len(list1):
        break
    n = list1[k1][0]
    m = list1[k1][-1]
    list_one = list2[k1]
    list_two = list3[k1]
    k2 = 0 
    c1 = False
    count = 0
    for i in list_one:
        for j in list_two:
            if i == j:
                count+=1
    print(count)
    k1+=1
    
