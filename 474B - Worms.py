from bisect import bisect_left
n1 = int(input())
list1 = []
x = input().split()
for i in x:
    list1.append(int(i))
n2 = int(input())
list2 = []
x = input().split()
for i in x:
    list2.append(int(i))
 
list3 = []
b1 = False
start = 0
sum1 = list1[start]
while b1==False:
    list3.append(sum1)
    start+=1
    if start == len(list1):
        break
    sum1 += list1[start]
 
c1 = False
start1 = 0
while c1==False:
    i = bisect_left(list3, list2[start1])
    print(i+1)
    start1+=1
    if start1 == len(list2):
        break
