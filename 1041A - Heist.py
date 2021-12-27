n1 = int(input())
x = input().split()
list1 = []
for i in x:
    list1.append(int(i))
list1.sort()
count = 0
for i in range(len(list1)-1):
    count+=list1[i+1] - list1[i] - 1
    
print(count)
    
