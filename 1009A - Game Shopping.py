x = input().split()
n = int(x[0])
m = int(x[1])
list1 = []
list2 = []
x = input().split()
for i in x:
    list1.append(int(i))
x = input().split()
for i in x:
    list2.append(int(i))
    
count = 0
b1 = False
k1 = 0
k2 = 0
while b1==False:
    if k2 == len(list2) or k1 == len(list1):
        print(count)
        break
    if list2[k2]>= list1[k1]:
        count+=1
        k1+=1
        k2+=1
        continue
    if list2[k2] < list1[k1]:
        k1+=1
        continue
