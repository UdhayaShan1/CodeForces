n1 = int(input())
str1 = input()

b1 = False
list1 = list("0"*10)

for i in str1:
    if i == "L":
        for j in range(len(list1)):
            if list1[j] == "0":
                list1[j] = "1"
                break
        continue
    if i == "R":
        list1.reverse()
        for j in range(len(list1)):
            if list1[j] == '0':
                list1[j] = "1"
                list1.reverse()
                break
        continue
    list1[int(i)] = "0"
    continue

print(''.join(list1))
