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
    h = ref_list[0]
    w = ref_list[1]
    
    start = ""
    other = "0"*w
    last = ""
    for i in range(w):
        if i%2 == 0:
            start+="1"
        else:
            start+="0"
    for i in range(w):
        if i == 0 or i == w-1:
            last+="1"
        else:
            last+="0"
    if h % 2 == 0:
        for i in range(h):
            if i == h-2:
                print(other)
                continue
            if i==0:
                print(start)
            elif i == h-1:
                print(start)
            else:
                if i%2 == 0:
                    print(last)
                else:
                    print(other)
    else:
        for i in range(h):
            if i == h-2:
                print(other)
                continue
            if i==0:
                print(start)
            elif i == h-1:
                print(start)
            else:
                if i%2 == 0:
                    print(last)
                else:
                    print(other)
        
    k1+=1
    if k1==len(list1):
        break
    else:
        print("")
