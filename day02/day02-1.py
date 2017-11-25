f = open('day02.txt', 'r')
dim_strings = [x.strip('\n') for x in f.readlines()]
f.close()

total = 0
for d in dim_strings:
    dims = [int(i) for i in d.split('x')]
    a1 = dims[0] * dims[1]
    a2 = dims[0] * dims[2]
    a3 = dims[1] * dims[2]
    total += 2*a1 + 2*a2 + 2*a3 + min(a1, a2, a3)

print(total)
