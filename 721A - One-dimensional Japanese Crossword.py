n1 = int(input())
n2 = input()
count = 0
index_b = [i for i, x in enumerate(n2) if x == "B"]
list2 = []
streak = 0
for i in range(len(index_b)):
    
    if i != len(index_b)-1:
        if index_b[i+1] - index_b[i] != 1:
            count+=1
            list2.append(streak+1)
            streak = 0
        else:
            streak+=1
    else:
        list2.append(streak+1)
        count+=1
        streak = 0
        
print(count)
print(*list2)
