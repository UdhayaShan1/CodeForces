n1 = int(input())
list1 = []
for i in range(n1):
    list1.append(int(input()))
 
k1 = 0
b1 = False
while b1==False:
    ref = list1[k1]
    list2 = [6,10,14]
    if ref <= 30:
        print("NO")
    elif ref - (6+10+14) in list2:
        print("YES")
        print(6,10,15,ref-(6+10+15))
    else:
        print("YES")
        print(6,10,14,ref-(6+10+14))
    k1+=1
    if k1==len(list1):
        break
