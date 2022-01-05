n1 = int(input())
list1 = []
for i in range(n1):
    x = input().split()
    temp = []
    for j in x:
        temp.append(int(j))
    list1.append(temp)
    
k1 = 0
b1 = False
while b1==False:
    ref_list = list1[k1]
    max_teams = sum(ref_list) // 4
    max_per = min(ref_list)
    print(min(max_per,max_teams))
    k1+=1
    if k1==len(list1):
        break
