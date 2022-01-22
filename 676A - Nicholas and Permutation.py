n1 = int(input())
list1 = []
x = input().split()
for i in x:
    list1.append(int(i))
    

index_max = 0
index_min =0
flag = 0
for i in range(len(list1)):
    if list1[i] == n1:
        index_max = i
        flag+=1
    elif list1[i]==1:
        index_min = i
        flag+=1
    if flag==2:
        break

print(max(index_max-0,n1-1 - index_max,n1-1 - index_min, index_min-0))
