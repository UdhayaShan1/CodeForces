n1 = int(input())
list1 = []
for i in range(n1):
    list1.append(int(input()))

k1 = 0
b1 = False
while b1==False:
    n = list1[k1]
    if n <=3:
        if n == 1:
            print(9)
        elif n == 2:
            print(98)
        else:
            print(989)
    else:
        remain = n - 3
        ref = "0123456789"
        str1 = (remain//len(ref))*ref + ref[0:(remain%len(ref))]
        print("989"+str1)
    k1+=1
    if k1==len(list1):
        break
