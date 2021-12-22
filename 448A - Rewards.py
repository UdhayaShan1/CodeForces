import math
n1 = input().split()
n2 = input().split()
n3 = int(input())
sum_cups = 0
sum_medals = 0
for i in n1:
    sum_cups += int(i)
for i in n2:
    sum_medals += int(i)

min_cup_shelves = math.ceil(sum_cups / 5)
min_medal_shelves = math.ceil(sum_medals / 10)
if min_medal_shelves + min_cup_shelves <= n3:
    print("YES")
else:
    print("NO")
