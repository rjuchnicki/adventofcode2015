import re

f = open('day05.txt', 'r')
inputs = [x.strip('\n') for x in f.readlines()]
f.close()

nice = 0
for s in inputs:
	repeated_pair = bool(re.search(r"(\w\w).*\1", s))
	sandwich_letter = bool(re.search(r"(\w)\w\1", s))
	if repeated_pair and sandwich_letter:
		nice += 1

print(nice)
