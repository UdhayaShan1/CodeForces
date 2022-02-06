n1 = int(input())
x = input().split()
list1 = []
for i in x:
    list1.append(int(i))
list2 = [0]*n1
list2[-1] = list1[-1]
k1 = 0
b1 = False
while b1==False:
    list2[k1] = list1[k1]+list1[k1+1]
    k1+=1
    if k1 == len(list1)-1:
        break
print(*list2)
