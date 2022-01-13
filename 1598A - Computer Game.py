n1 = int(input())
list1 = []
part1 = []
part2 = []
for i in range(n1):
    list1.append(int(input()))
    part1.append(input())
    part2.append(input())

k1 = 0
b1 = False
while b1==False:
    if k1==len(part1):
        break
    ref_part1 = part1[k1]
    ref_part2 = part2[k1]
    n = list1[k1]
    k2 = 0
    c1 = False
    flag = 0
    while c1==False:
        if ref_part1[k2] == ref_part2[k2] and ref_part2[k2] == "1":
            print("NO")
            flag += 1
            k1+=1
            break
        k2+=1
        if k2==len(ref_part1):
            print("YES")
            k1+=1
            break
    continue
