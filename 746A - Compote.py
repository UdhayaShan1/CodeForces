list1 = []
for i in range(3):
    list1.append(int(input()))
    
lemons = list1[0]
apples = list1[1]
pears = list1[-1]

start = 1
count1= 0
count2 = 0
b1 = False
while b1==False:
    if start * 2 > apples or start * 4 > pears or start > lemons:
        print(start + count1 + count2-1)
        break
    if start * 2 <= apples and start *4 <= pears:
        count1 = start*2
        count2 = start*4
    start+=1
