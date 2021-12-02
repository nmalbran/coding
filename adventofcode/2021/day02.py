import sys


def part1():
	with open(sys.argv[1]) as file:
		instructions = file.readlines()


	pos = 0
	depth = 0

	for step in instructions:
		words = step.split(' ')
		verb = words[0]
		num = int(words[1])

		if verb == "forward":
			pos += num
		elif verb == "down":
			depth += num
		elif verb == "up":
			depth -= num
		else:
			raise ValueError("wrong verb")

		print(f'pos: {pos}, depth: {depth}')
	print(f'total: {pos*depth}')


with open(sys.argv[1]) as file:
	instructions = file.readlines()


pos = 0
depth = 0
aim = 0

for step in instructions:
	words = step.split(' ')
	verb = words[0]
	num = int(words[1])

	if verb == "forward":
		pos += num
		depth += (aim * num)
	elif verb == "down":
		aim += num
	elif verb == "up":
		aim -= num
	else:
		raise ValueError("wrong verb")

	print(f'pos: {pos}, depth: {depth}, aim: {aim}')
print(f'total: {pos*depth}')
