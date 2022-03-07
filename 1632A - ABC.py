n1 = int(input())
list1 = []
list2 = []
for i in range(n1):
    list1.append(int(input()))
    list2.append(input())
 
k1 = 0
b1 = False
while b1==False:
    if k1==len(list1):
        break
    n = list1[k1]
    ref = list2[k1]
    if n == 1:
        print("YES")
        k1+=1
        continue
    if n == 2:
        if ref == "11" or ref == "00":
            print("NO")
        else:
            print("YES")
        k1+=1
        continue
    print("NO")
    k1+=1
