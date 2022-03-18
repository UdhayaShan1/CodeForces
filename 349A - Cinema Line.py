n1 = int(input())
x = input().split()
list1 = []
for i in x:
    list1.append(int(i))
twentyfive_notes = 0
fifty_notes = 0
flag = 0
for i in range(n1):
    if list1[i] == 25:
        twentyfive_notes+=1
        continue
    if list1[i] == 50:
        if twentyfive_notes > 0:
            twentyfive_notes-=1
            fifty_notes+=1
            continue
        else:
            flag+=1
            break
    if list1[i] == 100:
        if twentyfive_notes > 0 and fifty_notes > 0:
            twentyfive_notes-=1
            fifty_notes-=1
            continue
        if twentyfive_notes > 2:
            twentyfive_notes -= 3
            continue
        else:
            flag += 1
            break

if flag == 1:
    print("NO")
else:
    print("YES")
