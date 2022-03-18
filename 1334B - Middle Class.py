n1 = int(input())
list1 = []
list2 = []
for i in range(n1):
    list1.append(input().split())
    temp = []
    for j in input().split():
        temp.append(int(j))
    list2.append(temp)

k1 = 0
b1 = False
while b1==False:
    ref1 = list1[k1]
    n = int(ref1[0])
    x = int(ref1[1])
    ref_savings =  list2[k1]
    ref_savings.sort()
    ref_savings = ref_savings[::-1]
    sum1 = 0
    count = 0
    for i in range(n):
        sum1 += ref_savings[i]
        if sum1 >= x * (i+1):
            count += 1
    print(count)
    k1+=1
    if k1==len(list1):
        break
