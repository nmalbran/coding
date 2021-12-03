from typing import List
import sys


def _read_numbers(filename: str) -> List[int]:
	with open(filename) as file:
		measurements = [int(line.strip()) for line in file.readlines()]
	return measurements

def count_measurements_larger_than_previous(filename: str) -> int:
	measurements = _read_numbers(filename)

	increases = 0
	for i in range(1, len(measurements)):
		if measurements[i] > measurements[i-1]:
			increases += 1

	return increases


def count_measurements_larger_in_window(filename: str, window: int) -> int:
	measurements = _read_numbers(filename)

	measurements_sum = []
	for i in range(0, len(measurements) - window+1):
		measurements_sum.append(sum(measurements[i:i+window]))

	increases = 0
	for i in range(1, len(measurements_sum)):
		if measurements_sum[i] > measurements_sum[i-1]:
			increases += 1

	return increases


if __name__ == '__main__':
	filename = sys.argv[1]
	print(count_measurements_larger_than_previous(filename))
	print(count_measurements_larger_in_window(filename, 1))
	print(count_measurements_larger_in_window(filename, 3))
