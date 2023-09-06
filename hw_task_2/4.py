a = [5, 2, 'aewf', 4, 'weeewqe', 4]
b = [4, 'asadsafv', 'weeewqe', 3]

c = []

for i in a:
    if i in b and i not in c:
        c.append(i)

print(c)