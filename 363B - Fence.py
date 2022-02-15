x = input().split()
n = int(x[0])
k = int(x[1])
x = input().split()
list1 = []
for i in x:
    list1.append(int(i))

min1 = 10**9
final = 1
b1 = False
start_list = list1[0:k]
start_sum = sum(start_list)
start = 0

while b1==False:
    if start_sum < min1:
        min1 = start_sum
        final = start
    if start == n-k:
        break
    start_sum -= list1[start]
    start_sum += list1[start+k]
    start+=1

print(final+1)
