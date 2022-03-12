n1 = int(input())
listn = []
list1 = []
for i in range(n1):
    listn.append(int(input()))
    x = input().split()
    temp = []
    for j in x:
        temp.append(int(j))
    temp.sort()
    list1.append(temp)

k1 = 0
b1 = False
while b1==False:
    if k1==len(list1):
        break
    ref_list = list1[k1]
    count = 1
    last = 0
    max1 = -1
    for i in range(len(ref_list)):
        if ref_list[i] <= count:
            if i > max1:
                max1 = i
        count+=1
    print(max1+2)
    k1+=1
