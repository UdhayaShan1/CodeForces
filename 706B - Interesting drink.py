from bisect import bisect_left
n1 = int(input())
dp = {}
x = input().split()
list1 = []
for i in x:
    list1.append(int(i))
 
list1.sort()
 
list2 = []
days = int(input())
for i in range(days):
    list2.append(int(input()))
    
def BinarySearch(a, x):
    i = bisect_left(a, x)
    if i:
        return (i-1)
    else:
        return -1
 
k1 = 0
b1 = False
while b1==False:
    ref = list2[k1]
    res = BinarySearch(list1, ref+1)
    print(res+1)
    k1+=1
    if k1==len(list2):
        break
