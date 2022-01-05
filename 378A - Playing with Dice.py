x = input().split()
a = int(x[0])
b = int(x[1])

count_a = 0
count_b = 0
count_draw = 0
for i in range(1,7):
    if abs(i-a) > abs(i-b):
        count_b += 1
    elif abs(i-b) > abs(i-a):
        count_a += 1
    else:
        count_draw += 1
        
print(count_a,count_draw,count_b)
