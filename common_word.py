li1 = [ int(i) for i in input('Enter a list: ').split()]
li2 = [ int(i) for i in input('Enter another list: ').split()]

li3 = []

for num in li1:
    if num in li2:
        li3.append(num)

print(li3)


