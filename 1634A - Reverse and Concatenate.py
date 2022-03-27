n1 = int(input())
list1 = []
list2 = []
for i in range(n1):
    list1.append(input().split())
    list2.append(input())
 
k1 = 0
b1 = False
while b1==False:
    ref1 = list1[k1]
    n = int(ref1[0])
    k = int(ref1[1])
    str1 = list2[k1]
    if str1 == str1[::-1] or k == 0:
        print(1)
    else:
        print(2)
    k1+=1
    if k1==len(list1):
        break
