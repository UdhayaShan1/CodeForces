n1 = int(input())
list1 = []
list2 = []
for i in range(n1):
    list1.append(int(input()))
    x = input().split()
    temp = []
    for j in x:
        temp.append(int(j))
    list2.append(temp)

k1 = 0
b1 = False
while b1==False:
    n = list1[k1]
    ref = list2[k1]
    pos_array = [0]
    neg_array = [-100000000000000000000000]
    sum1 = 0
    flag = 0
    for i in range(len(ref)):
        if ref[i] < 0:
            if flag == 0:
                sum1 += max(pos_array)
                pos_array = [0]
                flag+=1
                neg_array.append(ref[i])
            else:
                neg_array.append(ref[i])
        else:
            if flag > 0:
                sum1+=max(neg_array)
                neg_array = [-100000000000000000000000]
                flag = 0
                pos_array.append(ref[i])
            else:
                pos_array.append(ref[i])
        if i == len(ref)-1:
            
            if neg_array == [-100000000000000000000000]:
                sum1+=max(pos_array)
            else:
                sum1 += max(neg_array)
    print(sum1)
    k1+=1
    if k1==len(list2):
        break
