n1 = int(input())
list1 = []
for i in range(n1):
    list1.append(input().split())
 
k1 = 0
b1 = False
while b1==False:
    ref = list1[k1]
    n = int(ref[0])
    m = int(ref[1])
    i = int(ref[2])
    j = int(ref[3])
    if j != 1 and j != m:
        print(1,1,n,m)
    else:
        if j == 1:
            if i == 1:
                print(n,1,1,m)
            elif i == m:
                print(1,1,n,m)
            else:
                if i <= (n/2):
                    print(n,m,1,m)
                else:
                    print(1,1,n,m)
        elif j == m:
            if i == 1:
                print(n,m,1,1)
            elif i == m:
                print(1,1,n,1)
            else:
                if i <= (n/2):
                    print(n,m,1,1)
                else:
                    print(1,1,n,m)
    k1+=1
    if k1==len(list1):
        break
