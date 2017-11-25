import re

f = open('day08.txt', 'r')
literals = [x.strip('\n') for x in f.readlines()]
f.close()

literal_rep = 0
escape_mem = 0
unescaped = 0
for l in literals:
    literal_rep += len(l)
    unescaped += len(l) + 2 + l.count('\\') + l.count('"')

    l = l[1:-1]
    escaped_char = len(re.findall(r'\\"|\\\\', l))
    escaped_hex = len(re.findall(r"\\x[0-9a-f]{2}", l))
    escape_mem += len(l) - escaped_char - 3*escaped_hex

print(literal_rep - escape_mem)
print(unescaped - literal_rep)
