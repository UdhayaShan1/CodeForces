x = input().split()
str1 = input()
n = int(x[0])
k = int(x[1])

if len(set(str1)) < k:
    print(0)
else:
    list1 = []
    count = 0
    for i in sorted(set(str1)):
        list1.append(len([j for j, x in enumerate(str1) if x == i]))
        count+=1
        if count == k:
            break
    print(min(list1)*k)
