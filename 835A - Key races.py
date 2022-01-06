n1 = input().split()
list1 = []
for i in n1:
    list1.append(int(i))
    
s = list1[0]
v1 = list1[1]
v2 = list1[2]
t1 = list1[3]
t2 = list1[4]
if v1*s + 2* t1> v2*s + 2* t2:
    print("Second")
elif v1*s + 2* t1< v2*s + 2* t2:
    print("First")
else:
    print("Friendship")
