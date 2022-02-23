
n1 = int(input())
list1 = []
for i in range(n1):
    x = input().split()
    temp = []
    for j in x:
        temp.append(int(j))
    list1.append(temp)
 
k1 = 0
b1 = False
while b1==False:
    n = list1[k1][0]
    k = list1[k1][1]
    if k % 2 == 0:
        if n % 2 != 0:
            print("NO")
        else:
            sum1 = (k/2)*(2+(k-1)*(2))
            if sum1 <= n:
                print("YES")
            else:
                print("NO")
    else:
        if n % 2 == 0:
            print("NO")
        else:
            sum1 = (k/2)*(2+(k-1)*(2))
            if sum1 <= n:
                print("YES")
            else:
                print("NO")
    k1+=1
    if k1==len(list1):
        break
