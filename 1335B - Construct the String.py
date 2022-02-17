n1 = int(input())
list1 = []
for i in range(n1):
    x = input().split()
    temp = []
    for j in x:
        temp.append(int(j))
    list1.append(temp)
str1 = "abcdefghijklmnopqrstuvwxyz"
k1 = 0
b1 = False
while b1==False:
    n = list1[k1][0]
    a = list1[k1][1]
    b = list1[k1][2]
    cut = str1[:b]
    num1 = n//b
    final = cut * num1
    final += cut[:n%b]
    print(final)
    k1+=1
    if k1==len(list1):
        break
