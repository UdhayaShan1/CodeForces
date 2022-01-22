n1 = input()
n2 = input()
n3 = input()
list1 = []
for i in range(len(n3)):
    if n3[i].isupper() == True:
        temp = n3[i].lower()
        index_up = [j for j, x in enumerate(n1) if x == temp][0]
        list1.append(n2[index_up].upper())
    elif n3[i].islower() == True:
        temp = n3[i]
        index_up = [j for j, x in enumerate(n1) if x == temp][0]
        list1.append(n2[index_up])
    else:
        list1.append(n3[i])

print(''.join(list1))
