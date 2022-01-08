n1 = int(input())
list1 = []
for i in range(n1):
    x = input().split()
    sum1 = 0
    for j in x:
        sum1+=int(j)
    list1.append(sum1)

guy = list1[0]
list1.sort()
list1 = list1[::-1].copy()
print([i for i, x in enumerate(list1) if x == guy][0]+1)
