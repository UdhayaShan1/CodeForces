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
    ref = list1[k1]
    n = ref[0]
    a = ref[1]
    b = ref[2]
    c = ref[3]
    d = ref[4]
    lower1 = (a-b)*n
    higher1 = (a+b)*n
    if higher1 >= (c+d) and lower1 <= (c+d):
        print("Yes")
    elif higher1 < (c+d) and higher1 >= (c-d):
        print("Yes")
    else:
        print("No")
    k1+=1
    if k1==len(list1):
        break
