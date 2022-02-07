x = input()
flag = 0
for i in range(len(x)-6):
    if x[i:i+7] == "0"*7 or x[i:i+7] == "1"*7:
        flag+=1
        break
if flag > 0:
    print("YES")
else:
    print("NO")
