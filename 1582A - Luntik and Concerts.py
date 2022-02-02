n1 = int(input())
list1 = []
for i in range(n1):
    x = input().split()
    a = int(x[0])
    b = int(x[1])
    c = int(x[2])
    sum1 = a*1+b*2+c*3
    if sum1%2==0:
        list1.append(0)
    else:
        list1.append(1)
for i in list1:
    print(i)
