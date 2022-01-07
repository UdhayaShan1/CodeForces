n1 = int(input())
x = input().split()
list1 = []
for i in x:
    list1.append(int(i))

k1 = 0 
b1 = False
while b1==False:
    starti = k1+1
    first_likes_this = list1[k1]
    second_likes_this = list1[first_likes_this-1]
    third_likes_this = list1[second_likes_this-1]
    if third_likes_this == starti:
        print("YES")
        break
    else:
        k1+=1
    if k1==len(list1):
        print("NO")
        break
