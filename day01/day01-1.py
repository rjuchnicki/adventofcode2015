f = open('day01.txt', 'r')
s = f.read()
f.close()

floor = 0
for c in s:
    floor = floor + 1 if c == '(' else floor - 1

print(floor)
