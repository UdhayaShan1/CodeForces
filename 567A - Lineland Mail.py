n1 = int(input())
list1 = input().split()
list2 = []
for i in list1:
    list2.append(int(i))
 
mid_point = (list2[0]+list2[-1])/2
 
for i in range(len(list2)):
    if list2[i] <= mid_point and i > 0 and i < n1-1:
        max_i = abs(list2[-1] - list2[i])
        min_i = min(abs(list2[i+1]-list2[i]),abs(list2[i]-list2[i-1]))
        print(min_i,max_i)
    elif list2[i] > mid_point and i > 0 and i < n1-1:
        max_i = abs(list2[0] - list2[i])
        min_i = min(abs(list2[i+1]-list2[i]),abs(list2[i]-list2[i-1]))
        print(min_i,max_i)
    elif i == 0:
        print(abs(list2[i+1]-list2[i]),list2[-1] - list2[i])
    else:
        print(abs(list2[i]-list2[i-1]),abs(list2[0]-list2[i]))
