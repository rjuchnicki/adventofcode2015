import functools

f = open('day07.txt', 'r')
instructions = [x.strip('\n') for x in f.readlines()]
f.close()

circuit = {}

for i in instructions:
    cmd,reg = i.split(" -> ")
    circuit[reg] = cmd

@functools.lru_cache()
def evaluate(reg):
	try:
		return int(reg)
	except ValueError:
		pass

	cmd = circuit[reg].split(' ')
	if 'NOT' in cmd:
		return ~evaluate(cmd[1])
	elif 'AND' in cmd:
		return evaluate(cmd[0]) & evaluate(cmd[2])
	elif 'OR' in cmd:
		return evaluate(cmd[0]) | evaluate(cmd[2])
	elif 'LSHIFT' in cmd:
		return evaluate(cmd[0]) << evaluate(cmd[2])
	elif 'RSHIFT' in cmd:
		return evaluate(cmd[0]) >> evaluate(cmd[2])
	else:
		return evaluate(cmd[0])

print('Part 1')
a = str(evaluate('a'))
print(a)

print('\nPart 2')
evaluate.cache_clear()
circuit['b'] = str(a)
print(evaluate('a'))
