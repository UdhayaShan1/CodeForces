n1 = int(input())
list1 = []
left = 0
right = 0
for i in range(n1):
    x = input().split()
    temp = []
    for j in x:
        temp.append(int(j))
    left += temp[0]
    right += temp[1]

count = 0 
if n1 - left> left - 0:
    count += left
elif left > n1 - left:
    count+= n1 - left
else:
    count += left

if n1 - right> right - 0:
    count += right
elif right > n1 - right:
    count+= n1 - right
else:
    count += right

print(count)
