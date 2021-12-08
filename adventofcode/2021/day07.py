
from common import read_csv_nums
from collections import Counter
from typing import Dict


def arithmetic_sum(n: int) -> int:
  return (n * (1 + n))//2


def compute_fuel_for_pos(crabs: Dict[int,int], pos:int) -> int:
  # Part 1
  # return sum([abs(c - pos)*crabs[c] for c in crabs])
  
  # Part 2
  return sum([arithmetic_sum(abs(c - pos))*crabs[c] for c in crabs])


def compute_fuel(filename: str) -> float:
  nums = read_csv_nums(filename)

  crabs: Dict[int, int] = Counter()
  min_n = float('inf')
  max_n = float('-inf')
  for n in nums:
    crabs[n] += 1
    if n < min_n:
      min_n = n
    if n > max_n:
      max_n = n

  min_fuel = float('inf')
  for pos in range(min_n, max_n+1):
    fuel = compute_fuel_for_pos(crabs, pos)
    if fuel < min_fuel:
      min_fuel = fuel

  return min_fuel


if __name__ == '__main__':
  print(compute_fuel('day07-example.txt'))
  print(compute_fuel('day07-input.txt'))
