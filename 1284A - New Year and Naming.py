x = input().split()
list1 = []
for j in x:
    list1.append(int(j))
n = input().split()
m = input().split()
q = int(input())
list2 = []
for i in range(q):
    list2.append(int(input()))
    

b1 = False
k1 = 0
n_length = list1[0]
m_length = list1[1]
while b1==False:
    year = list2[k1]
    position_n = year % n_length-1
    position_m = year % m_length-1
    print(n[position_n]+m[position_m])
    k1+=1
    if k1==len(list2):
        break
