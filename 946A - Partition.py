n1 = int(input())
x=input().split()
list1 = []
for i in x:
    list1.append(int(i))
list_positive = []
list_negative = []

for i in list1:
    if i >= 0:
        list_positive.append(i)
    else:
        list_negative.append(i)
        
print(sum(list_positive) - sum(list_negative))
