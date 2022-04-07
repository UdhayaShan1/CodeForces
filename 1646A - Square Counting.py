n1 = int(input())
list1 = []
for i in range(n1):
    list1.append(input().split())
 
k1 = 0
b1 = False
while b1==False:
    ref = list1[k1]
    n = int(ref[0])
    s = int(ref[1])
    print(s // (n**2))
    k1+=1
    if k1==len(list1):
        break
