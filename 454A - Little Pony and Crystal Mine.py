import math
n1 = int(input())
count1 = (n1-1)//2
count2 = 1
for i in range(math.ceil(n1/2)):
    print(count1 * "*" + count2 * "D"+count1 * "*")
    count1-=1
    count2+=2

count1 = 1
count2 = n1 - 2
for i in range(n1 - math.ceil(n1/2)):
    print(count1 * "*" + count2 * "D" + count1 * "*")
    count1 +=1
    count2 -= 2
