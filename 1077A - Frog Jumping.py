n1 = int(input())
list1 = []
for i in range(n1):
    list1.append(input().split())
 
k1 = 0
b1 = False
while b1==False:
    ref = list1[k1]
    a = int(ref[0])
    b = int(ref[1])
    k = int(ref[2])
    if k%2 == 0:
        ref1 = k // 2
        print(ref1 * a - ref1 * b)
    else:
        ref1 = (k-1) // 2
        print((ref1+1) * (a) - ref1 * b)
    k1+=1
    if k1==len(list1):
        break
