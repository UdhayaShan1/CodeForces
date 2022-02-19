n1 = int(input())
list1 = []
for i in range(n1):
    list1.append(input())
 
b1 = False
k1 = 0
while b1==False:
    if k1==len(list1):
        break
    ref = list1[k1]
    if len(ref) % 2 != 0:
        k1+=1
        print("NO")
        continue
    no_b = len([i for i, x in enumerate(ref) if x == "B"])
    if len([i for i, x in enumerate(ref) if x == "A"]) + len([i for i, x in enumerate(ref) if x == "C"]) == no_b:
        print("YES")
    else:
        print("NO")
    k1+=1
    continue
