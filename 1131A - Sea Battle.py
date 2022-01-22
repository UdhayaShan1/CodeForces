x = input().split()
w1 = int(x[0])
h1 = int(x[1])
w2 = int(x[2])
h2 = int(x[-1])

count = w1+2 + 2*h1

if w2>=w1:
    count += 2*h2 + w2 +2
else:
    count += (w1-w2) + 2 * h2
    count += w2+2

print(count)
