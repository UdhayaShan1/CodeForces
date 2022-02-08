x = list(input())

for i in range(len(x)):
    if ''.join(x[i:i+3]) == "WUB":
        x[i] = "@"
        x.pop(i+1)
        x.pop(i+1)

for i in range(len(x)):
    if x[i] == "@":
        x[i] = " "

y = (''.join(x).strip())
print(' '.join(y.split()))
