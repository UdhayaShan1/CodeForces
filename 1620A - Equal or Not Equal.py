n1 = int(input())
list1 = []
for i in range(n1):
    list1.append(input())
    
k1 = 0
b1 = False
while b1==False:
    no_n = len([i for i, x in enumerate(list1[k1]) if x == "N"])
    if no_n >= 2 or no_n == 0:
        print("YES")
    else:
        print("NO")
    k1+=1
    if k1==len(list1):
        break
