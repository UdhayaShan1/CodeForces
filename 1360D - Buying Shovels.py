n1 = int(input())
list1 = []
for i in range(n1):
    list1.append(input().split())

k1 = 0
b1 = False
while b1==False:
    ref = list1[k1]
    n = int(ref[0])
    k = int(ref[1])
    min1 = 1000000000
    for i in range(1,int(n**0.5)+1):
        if n % i == 0:
            if i <= k and n//i < min1:
                min1 = n//i
            if (n//i) <= k and (i) <= min1:
                min1 = i
    print(min1)
    k1+=1
    if k1==len(list1):
        break
