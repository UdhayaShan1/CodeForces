n1 = int(input())
list1 = []
dict1 = {}
for i in range(n1):
    x = input()
    if x not in dict1:
        dict1[x] = 0
    else:
        dict1[x] += 1
    if dict1[x] == 0:
        print("OK")
        continue
    print(x + str(dict1[x]))
