n = int(input())
x = input().split()
list1 = [0]*(n+1)

count = 0
max1 = 0

for i in range(2*n):
    if list1[int(x[i])] == 0:
        count+=1
        if count > max1:
            max1 = count
        list1[int(x[i])] = 1
    else:
        count -= 1
        list1[int(x[i])] = 0

print(max1)
    
        
    
