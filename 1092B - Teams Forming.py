n1 = int(input())
x = input().split()
n2 = []
for j in x:
    n2.append(int(j))
    
teams = int(n1/2)
ppl_per_team = 2
b1 = False
count = 0
k1 = 0
n2.sort()
while b1==False:
    count += n2[k1+1] - n2[k1]
    k1+=2
    if k1==len(n2):
        print(count)
        break
