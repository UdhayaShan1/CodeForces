x = input().split()
n = int(x[0])
m = int(x[1])
treasure_even = 0
treasure_odd= 0
keys_even = 0
keys_odd = 0

for i in input().split():
    if int(i) % 2 == 0:
        treasure_even+=1
    else:
        treasure_odd+=1

for i in input().split():
    if int(i) % 2 == 0:
        keys_even+=1
    else:
        keys_odd+=1

print(min(treasure_even,keys_odd) + min(treasure_odd,keys_even))
