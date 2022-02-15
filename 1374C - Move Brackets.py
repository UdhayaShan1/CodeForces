n1 = int(input())
listn = []
list1 = []
for i in range(n1):
    listn.append(int(input()))
    list1.append(list(input()))

k1 = 0
b1 = False
while b1==False:
    ref = list1[k1]
    c1 = False
    while c1==False:
        flag = 0
        for i in range(len(ref)-1):
            if ref[i] + ref[i+1] == "()":
                ref[i] = "o"
                flag+=1
                ref.pop(i)
                ref.pop(i)
                break
        if flag == 0:
            break
    ref1 = 0
    for i in ref:
        if i == "(":
            ref1+=1
    print(ref1)
    k1+=1
    if k1==len(list1):
        break
