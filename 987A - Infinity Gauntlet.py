n1 = int(input())
list_have = []
dict_all = {"purple":"Power","green":"Time","blue":"Space","orange":"Soul","red":"Reality","yellow":"Mind"}
for i in range(n1):
    list_have.append(dict_all[input()])

list_all = ["Power","Time","Space","Soul","Reality","Mind"]

print(6-len(list_have))

for i in list_all:
    if i not in list_have:
        print(i)
