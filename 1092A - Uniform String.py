n1 = int(input())
list1 = []
for i in range(n1):
    x = input().split()
    temp = []
    for j in x:
        temp.append(int(j))
    list1.append(temp)

alpha = "abcdefghijklmnopqrstuvwxyz"    
k1 = 0
b1 = False
while b1==False:
    n = list1[k1][0]
    k = list1[k1][1]
    str1 = alpha[:k]
    str2 = (n//k)*str1
    str2 += str1[:(n%k)]
    print(str2)
    k1+=1
    if k1==len(list1):
        break
