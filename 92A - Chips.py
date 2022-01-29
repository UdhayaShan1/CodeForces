x = input().split()
n = int(x[0])
m = int(x[1])
list1 = []
for i in range(1,n+1):
    list1.append(i)
b1 = False
flag = 0
while b1==False:
    for i in list1:
        if m<i:
            flag+=1
            break
        m-=i
        if m==0:
            flag+=1
            break
    if flag == 1:
        print(m)
        break
