x = int(input())
n1 = input().split()
list1 = []
for i in n1:
    list1.append(int(i))
list1.sort()
list1 = list1[::-1]
count = 1
sum1 = sum(list1)
sum2 = 0
b1 = False
while b1==False:
    sum2+=list1[0]
    if sum2>(sum1-sum2):
        print(count)
        break
    list1.pop(0)
    count+=1
