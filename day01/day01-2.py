f = open('day01.txt', 'r')
s = f.read()
f.close()

floor = 0
i = 0
for c in s:
    i+=1
    floor = floor + 1 if c == '(' else floor - 1
    if floor == -1:
        break

print(i)
