
from typing import List


def read_csv_nums(filename: str) -> List[int]:
	with open(filename) as f:
		return [int(n) for n in f.read().strip().split(',')]