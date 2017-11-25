f = open('day02.txt', 'r')
dim_strings = [x.strip('\n') for x in f.readlines()]
f.close()

total = 0
for d in dim_strings:
    dims = [int(i) for i in d.split('x')]
    dims.sort()
    total += 2*dims[0] + 2*dims[1] + dims[0]*dims[1]*dims[2]

print(total)
