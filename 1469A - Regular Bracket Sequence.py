n1 = int(input())
list1 = []
for i in range(n1):
    list1.append(list(input()))

k1 = 0
b1 = False
while b1==False:
    if k1==len(list1):
        break
    ref = list1[k1]
    if ref[0] == ")" or ref[-1] == "(":
        print("NO")
        k1+=1
        continue
    if len(ref) % 2 == 0:
        print("YES")
    else:
        print("NO")
    k1+=1
