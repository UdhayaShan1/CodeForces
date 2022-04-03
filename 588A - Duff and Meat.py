n1 = int(input())
list1 = []
list2 = []
min_price = 10000000
for i in range(n1):
    x = input().split()
    if int(x[1]) < min_price:
        min_price = int(x[1])
    list1.append(int(x[0]))
    list2.append(min_price)
 
cost = 0
meat = 0
for i in range(n1):
    if list2[i] == min_price:
        cost += (sum(list1) - meat) * list2[i]
        break
    else:
        cost += (list2[i]*list1[i])
        meat += list1[i]
 
print(cost)
