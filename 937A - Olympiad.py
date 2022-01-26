n1 = int(input())
x = input().split()
list1 = []
for i in x:
    if int(i) != 0:
        list1.append(int(i))
        
print(len(set(list1)))
