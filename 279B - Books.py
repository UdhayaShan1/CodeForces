x = input().split()
n = int(x[0])
t = int(x[1])
x = input().split()
list1 = []
for j in x:
    list1.append(int(j))

i = 0
j = 0
count = 0
sum1 = 0
b1 = False
max1 = 0
while b1==False:
    
    if i == len(list1):
        if sum1 > t:
            count -= 1
        if count > max1:
            max1 = count
        break
    sum1 += list1[i]
    count += 1
    if sum1 > t:
        count -= 1
        if count > max1:
            max1 = count
        sum1 -= list1[j]
        i+=1
        j+=1
        continue
    i+=1

print(max1)
