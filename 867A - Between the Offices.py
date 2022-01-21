n1 = int(input())
str1 = input()

count_sf = 0
count_other = 0
for i in range(len(str1)-1):
    if str1[i] + str1[i+1] == "SF":
        count_sf+=1
    elif str1[i]+str1[i+1] == "FS":
        count_other+=1
        
if count_sf>count_other:
    print("Yes")
else:
    print("No")
