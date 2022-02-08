n1 = int(input())
x = input().split()
list1 = []
for i in x:
    list1.append(int(i))

min_pos = [i for i, x in enumerate(list1) if x == min(list1)][-1]
max_pos = [i for i, x in enumerate(list1) if x == max(list1)][0]

if n1 - 1 - min_pos >= max_pos:
    b1 = False
    count = 0
    max_pos = [i for i, x in enumerate(list1) if x == max(list1)][0]
    while b1==False:
        
        if list1[0] == max(list1):
            break
        temp1 = list1[max_pos]
        temp2 = list1[max_pos-1]
        list1[max_pos] = temp2
        list1[max_pos-1] = temp1
        max_pos-=1
        count+=1
    c1 = False
    min_pos = [i for i, x in enumerate(list1) if x == min(list1)][-1]
    while c1==False:
        if list1[-1] == min(list1):
            break
        temp1 = list1[min_pos]
        temp2 = list1[min_pos+1]
        list1[min_pos] = temp2
        list1[min_pos+1] = temp1
        min_pos+=1
        count+=1
    print(count)
else:
    count = 0
    c1 = False
    min_pos = [i for i, x in enumerate(list1) if x == min(list1)][-1]
    while c1==False:
        if list1[-1] == min(list1):
            break
        temp1 = list1[min_pos]
        temp2 = list1[min_pos+1]
        list1[min_pos] = temp2
        list1[min_pos+1] = temp1
        min_pos+=1
        count+=1

    b1 = False
    max_pos = [i for i, x in enumerate(list1) if x == max(list1)][0]
    while b1==False:
        if list1[0] == max(list1):
            break
        temp1 = list1[max_pos]
        temp2 = list1[max_pos-1]
        list1[max_pos] = temp2
        list1[max_pos-1] = temp1
        max_pos-=1
        count+=1
    print(count)
