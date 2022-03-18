n1 = int(input())
list1 = []
for i in range(n1):
    list1.append(input().split())
 
k1 = 0
b1 = False
while b1==False:
    ref = list1[k1]
    n = int(ref[0])
    m = int(ref[1])
    list2 = []
    for i in range(n):
        if i == 0:
            list2.append("W" + (m-1)*"B")
        else:
            list2.append("B"*m)
    for i in list2:
        print(i)
    k1+=1
    if k1==len(list1):
        break
