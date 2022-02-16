n1 = int(input())
limit = int(n1/2)+1
list1 = []
dict1 = {}
for i in range(n1):
    x = input()
    if x not in dict1:
        dict1[x] = 1
        if dict1[x] >= limit:
            print(x)
            break
    else:
        dict1[x] += 1
        if dict1[x] >= limit:
            print(x)
            break
