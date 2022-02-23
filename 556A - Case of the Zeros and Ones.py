n1 = int(input())
n2 = input()
 
count_0 = 0
count_1 = 0
for i in n2:
    if i == "0":
        count_0 += 1
    else:
        count_1 += 1
 
print(n1 - 2*min(count_1,count_0))
