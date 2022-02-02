n1 = int(input())
x = input().split()
og_birds = []
for i in x:
    og_birds.append(int(i))
n2 = int(input())
list1 = []
for i in range(n2):
    x = input().split()
    temp = []
    for j in x:
        temp.append(int(j))
    list1.append(temp)

k1 = 0
b1 = False
while b1==False:
    if n2 == 0:
        break
    if len(og_birds)>1:
        ref = list1[k1]
        x = ref[0]
        y = ref[1]
        if x == 1:
            og_birds[x] += og_birds[x-1] - y
            og_birds[x-1] = 0
        elif x == n1:
            og_birds[x-2] += y-1
            og_birds[x-1] = 0
        else:
            og_birds[x] += og_birds[x-1] - y
            og_birds[x-2] += y-1
            og_birds[x-1] = 0
        k1+=1
        if k1==len(list1):
            break
    else:
        ref = list1[k1]
        x = ref[0]
        y = ref[1]
        og_birds[0] = 0
        break
        
for i in og_birds:
    print(i)
