n1 = int(input())
n2 = input()
z_count = len([i for i, x in enumerate(n2) if x == "z"])
n_count = len([i for i, x in enumerate(n2) if x == "n"])
list2 = [1]*n_count + [0]*z_count
print(*list2)
