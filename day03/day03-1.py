f = open('day03.txt', 'r')
s = f.read()
f.close()

dirs = {'^': (0,1), 'v': (0,-1), '<': (-1,0), '>': (1,0)}

pos = (0,0)
visited = set()
visited.add((0,0))
for c in s:
    dx,dy = dirs[c]
    pos = (pos[0] + dx, pos[1] + dy)
    visited.add(pos)

print(len(visited))
