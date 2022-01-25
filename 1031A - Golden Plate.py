x = input().split()
list1 = []
for i in x:
    list1.append(int(i))
    
w = list1[0]
h = list1[1]
k = list1[2]
rings = 1
b1 = False
sum1 = 0
while b1==False:
    sum1 += (w-4*(rings-1))*(h-4*(rings-1))
    sum1 -= ((w-4*(rings-1))-2)*((h-4*(rings-1))-2)
    rings+=1
    if ((w-4*(rings-1))) < 0 or ((h-4*(rings-1))) < 0 or rings>k:
        print(sum1)
        break
