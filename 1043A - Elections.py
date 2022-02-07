n1 = int(input())
list1 = []
x = input().split()
for i in x:
    list1.append(int(i))

total = sum(list1)*2+1
b1 = False
while b1==False:
    if total % n1 == 0:
        if total / n1 <= max(list1):
            print(max(list1))
        else:
            print(int(total/n1))
        break
    total+=1
