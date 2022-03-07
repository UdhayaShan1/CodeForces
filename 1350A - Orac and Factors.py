
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
    if n % 2 == 0:
        print(2*k + n)
    else:
        min1 = n
        for i in range(2,int(n**0.5)+1):
            if n % i == 0:
                if i < min1:
                    min1 = i
                    break
        n += min1
        k -= 1
        print(2*k + n)
    k1+=1
    if k1==len(list1):
        break
