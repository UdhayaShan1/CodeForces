n1 = int(input())
n2 = input()
dict1 = {}

for i in range(len(n2)-1):
    str1 = n2[i] + n2[i+1]
    if str1 not in dict1:
        dict1[str1] = 1
    else:
        dict1[str1] += 1

dict2 = dict(zip(list(dict1.values()),list(dict1.keys())))
print(dict2[max(dict1.values())])
