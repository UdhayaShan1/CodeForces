n1 = int(input())
list1 = []
for i in range(n1):
    list1.append(input().split())
    
k1 = 0
b1 = False
flag = 0
while b1==False:
    if k1==len(list1):
        break
    score1 = int(list1[k1][1])
    score2 = int(list1[k1][2])
    if score1 >= 2400 and score2 > score1:
        print("YES")
        flag+=1
        break
    k1+=1
if flag == 0:
    print("NO")
    
