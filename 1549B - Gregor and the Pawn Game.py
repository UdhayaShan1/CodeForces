n1 = int(input())
listn = []
list1 = []
list2 = []
for i in range(n1):
    listn.append(int(input()))
    list1.append(input())
    list2.append(input())
    
k1 = 0
b1 = False
while b1==False:
    ref_n = listn[k1]
    ref_enemy = list(list1[k1])
    ref_you = list(list2[k1])
    count = 0
    indices_pawns_yours = [i for i, x in enumerate(ref_you) if x=="1"]
    indices_pawns_enemy= [i for i, x in enumerate(ref_enemy) if x=="1"]
    for i in range(len(ref_you)):

        if ref_you[i] == "1" and ref_enemy[i] == "0":
            count+=1
            ref_enemy[i] = "2"
            continue
        if (ref_you[i] == "1"):
            if ref_enemy[i] == "1" or ref_enemy[i] == "2":
                if i == 0:
                    if ref_enemy[i+1] == "1":
                        count+=1
                        ref_enemy[i+1] = "2"
                elif i == len(ref_enemy)-1:
                    if ref_enemy[i-1] == "1":
                        count+=1
                        ref_enemy[i-1] = "2"
                else:
                    if ref_enemy[i-1] == "1":
                        count+=1
                        ref_enemy[i-1] = "2"
                    elif ref_enemy[i+1] == "1":
                        count+=1
                        ref_enemy[i+1] = "2"
    print(count)
    k1+=1
    if k1==len(list1):
        break
            
