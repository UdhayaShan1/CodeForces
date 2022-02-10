n1 = int(input())
x = input().split()
list1 = []
for i in x:
    list1.append(int(i))
count = 0
crimes = 0
for i in list1:
    if i == -1:
        count-=1
        if count <0:
            crimes+=1
            count = 0
    else:
        count+=i

print(crimes)
