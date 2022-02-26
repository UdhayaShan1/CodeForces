n1 =  int(input())
listn = []
list1 = []
for i in range(n1):
    listn.append(int(input()))
    x = input().split()
    temp = []
    for j in x:
        temp.append(int(j))
    list1.append(temp)

k1 = 0
b1 = False
while b1==False:
    n = listn[k1]
    ref = list1[k1]
    one_index = [i for i, x in enumerate(ref) if x == 1]
    ref = ref[one_index[0]:one_index[-1]+1]
    print(len([i for i, x in enumerate(ref) if x == 0]))
    k1+=1
    if k1==len(list1):
        break
