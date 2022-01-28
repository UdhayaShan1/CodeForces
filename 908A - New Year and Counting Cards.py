x = input()
list1 = ["a","e","i","o","u"]
count = 0
for i in x:
    if i in list1:
        count+=1
        continue
    if i.isdigit() == True:
        if int(i) % 2 != 0:
            count+=1
        
print(count)
