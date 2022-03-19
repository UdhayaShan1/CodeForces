n1 = int(input())
list1 = []
for i in range(n1):
    list1.append(list(str(input())))

k1 = 0
b1 = False
while b1==False:
    ref = list1[k1]
    set1 = set()
    set1.add(ref[0])
    temp = [ref[0]]
    start = ref[0]
    min1 = 100000000
    for i in range(1,len((ref))):
        if len(set1) == 1 and ref[i] in set1:
            temp = [ref[i]]
            start = ref[i]
        elif len(set1) == 1 and ref[i] not in set1:
            temp.append(ref[i])
            set1.add(ref[i])
        elif len(set1) == 2 and ref[i] in set1 and ref[i] == start:
            start = ref[i-1]
            temp = [ref[i-1],ref[i]]
        elif len(set1) == 2 and ref[i] in set1 and ref[i] != start:
            temp.append(ref[i])
        elif len(set1) == 2 and ref[i] not in set1:
            temp.append(ref[i])
            if len(temp) < min1:
                min1 = len(temp)
            start = ref[i-1]
            temp = [ref[i-1],ref[i]]
            set1 = set()
            set1.add(ref[i-1])
            set1.add(ref[i])
    if min1 == 100000000:
        print(0)
    else:
        print(min1)
    k1+=1
    if k1==len(list1):
        break
