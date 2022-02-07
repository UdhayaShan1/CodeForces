x = list(input())
y = []
list1 = ["h","e","l","o"]
for i in x:
    if i in list1:
        y.append(i)
h = [i for i, x in enumerate(y) if x == "h"]
e = [i for i, x in enumerate(y) if x == "e"]
l = [i for i, x in enumerate(y) if x == "l"]
o = [i for i, x in enumerate(y) if x == "o"]
if len(h) == 0 or len(e) == 0 or len(l) == 0 or len(o) == 0:
    print("NO")
else:
    if o[-1] < h[0]:
        print("NO")
    else:
        temp = [h[0]]
        for i in e:
            if i > h[0] and i < o[-1]:
                temp.append(i)
                temp.append(o[-1])
                break
        if len(temp)!=3:
            print("NO")
        else:
            count = 0
            for i in l:
                if i>temp[1] and i<temp[-1]:
                    count+=1
            if count >= 2:
                print("YES")
            else:
                print("NO")
