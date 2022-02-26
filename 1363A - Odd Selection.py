n1 = int(input())
list1 = []
list2 = []
for i in range(n1):
    x = input().split()
    y = input().split()
    temp = []
    odd = 0
    even = 0
    for j in y:
        z = int(j)
        if z % 2 == 0:
            even += 1
        else:
            odd += 1
    list1.append(x)
    list2.append([odd,even])
 
k1 = 0
b1 = False
while b1==False:
    n = int(list1[k1][0])
    x = int(list1[k1][1])
    ref = list2[k1]
    odd = ref[0]
    even = ref[1]
    if x % 2 == 0:
        temp_odd = x-1
        temp_even = 1
        flag = 0
        b1 = False
        while b1==False:
            if temp_odd <= odd and temp_even <= even and odd != 0:
                flag+=1
                break
            if temp_odd <= 0 or temp_even >=n:
                break
            temp_odd -= 2
            temp_even = x - temp_odd
        if flag == 1:
            print("Yes")
        else:
            print("No")
    else:
        temp_odd = x
        temp_even = 0
        flag = 0
        b1 = False
        while b1==False:
            if temp_odd <= odd and temp_even <= even and odd != 0:
                flag+=1
                break
            if temp_odd <= 0 or temp_even >= n:
                break
            temp_odd -= 2
            temp_even = x - temp_odd
        if flag == 1:
            print("Yes")
        else:
            print("No")
    k1+=1
    if k1==len(list1):
        break
