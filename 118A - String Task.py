n1 = list(input())
vowel = ["a", "e", "i", "o", "u", "y"]
list1 = []
for i in range(len(n1)):
    if n1[i].lower() in vowel:
        continue
    list1.append(n1[i].lower())
k=0
for i in range(len(list1)):
    list1.insert(i+k,".")
    k+=1
    
print(''.join(list1))
