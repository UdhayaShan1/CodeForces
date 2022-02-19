n1 = int(input())
list1 = []
list2 = []
list3 = []
count = 0
for i in range(3):
    x = input().split()
    temp = []
    for j in x:
        temp.append(int(j))
    if count == 0:
        list1+=temp
    elif count == 1:
        list2+=temp
    else:
        list3+=temp
    count+=1
 
print(sum(list1)-sum(list2))
print(sum(list2)-sum(list3))
