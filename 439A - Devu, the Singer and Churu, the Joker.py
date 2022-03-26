x = input().split()
n = int(x[0])
d = int(x[1])
x = input().split()
list1 = []
for i in x:
    list1.append(int(i))
if (n-1) * 10 >= d or (sum(list1) + (n-1) * 10) > d:
    print(-1)
else:
    rest = (n-1)*10
    remain = d - sum(list1)
    jokes = rest // 5 + (remain-rest) // 5
    print(jokes)
