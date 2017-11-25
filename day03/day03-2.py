f = open('day03.txt', 'r')
s = f.read()
f.close()

dirs = {'^': (0,1), 'v': (0,-1), '<': (-1,0), '>': (1,0)}

pos = [(0,0), (0,0)]
visited = set()
visited.add((0,0))
for i in range(len(s)):
    dx,dy = dirs[s[i]]
    pos[i%2] = (pos[i%2][0] + dx, pos[i%2][1] + dy)
    visited.add(pos[i%2])

print(len(visited))
