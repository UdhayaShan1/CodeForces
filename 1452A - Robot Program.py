n1 = int(input())
list1 = []
for i in range(n1):
    list1.append(input().split())
 
k1 = 0
b1 = False
while b1==False:
    ref = list1[k1]
    x = int(ref[0])
    y = int(ref[1])
    min1 = min(x,y)
    max1 = max(x,y)
    steps = min1 * 2
    if max1 != min1:
        steps += 1+((max1-min1)-1)*2
    print(steps)
    k1+=1
    if k1==len(list1):
        break
