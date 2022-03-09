n1 = int(input())
list1 = []
for i in range(n1):
    list1.append([])
    for j in range(9):
        list1[i].append(input())
 
 
k1 = 0
b1 = False
while b1==False:
    ref = list1[k1]
    for i in range(len(ref)):
        temp1 = list(ref[i])
        for j in range(len(temp1)):
            if temp1[j] == "1":
                temp1[j] = "2"
        ref[i] = "".join(temp1)
    for i in range(9):
        print(ref[i])
    k1+=1
    if k1==len(list1):
        break
