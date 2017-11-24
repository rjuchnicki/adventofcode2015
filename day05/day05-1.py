import re

f = open('day05.txt', 'r')
inputs = [x.strip('\n') for x in f.readlines()]
f.close()

vowels = "aeiou"

nice = 0
for s in inputs:
	three_vowels = sum([s.count(c) for c in vowels]) >= 3
	double_letter = bool(re.search(r"(\w)\1", s))
	naughty_pair = bool(re.search(r"(ab|cd|pq|xy)", s))
	if three_vowels and double_letter and not naughty_pair:
		nice += 1

print(nice)
