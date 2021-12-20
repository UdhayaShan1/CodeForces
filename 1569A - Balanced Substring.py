n1 = int(input())
listn = []
list1 = []
for i in range(n1):
    listn.append(int(input()))
    list1.append(input())
    
k1 = 0
b1 = False
while b1==False:
    if k1==len(list1):
        break
    ref_n = listn[k1]
    ref_str = list1[k1]
    if len(ref_str) == 1:
        print(-1,-1)
        k1+=1
        continue
    count_yes = 0
    for i in range(len(ref_str)-1):
        if ref_str[i] + ref_str[i+1] == "ab" or ref_str[i] + ref_str[i+1] == "ba":
            print(i+1,i+2)
            count_yes+=1
            break
    if count_yes == 0:
        print(-1,-1)
    k1+=1
    
