n1 = int(input())
list1 = []
for i in range(n1):
    list1.append(input().split())
 
k1 = 0
b1 = False
while b1==False:
    ref = list1[k1]
    l = int(ref[0])
    r = int(ref[1])
    k = int(ref[2])
    if r == l:
        if r == 1:
            print("NO")
        else:
            print("YES")
    else:
        a = l
        b = r
        r = a
        l = b
        if r % 2 == 0:
            if l%2 == 0:
                even = (l-r)/2 + 1
                odd = (l-r + 1) - even
            else:
                even = (l+1-r)/2
                odd = (l-r + 1) - even
        else:
            if l % 2 != 0:
                odd = (l-r)/2+1
                even = (l-r+1) - odd
            else:
                odd = (l+1-r)/2
                even = (l-r+1) - odd
        if odd > k:
            print("NO")
        else:
            print("YES")
    k1+=1
    if k1==len(list1):
        break
