from dataclasses import dataclass
from collections import Counter
from typing import List


@dataclass(frozen=True)
class Point:
  x: int
  y: int
 
  @staticmethod
  def parse(line: str) -> 'Point':
    x, y = [int(n.strip()) for n in line.split(',')]
    return Point(x,y)


@dataclass
class Vent:
  p1: Point
  p2: Point
 
  def is_horizontal(self) -> bool:
    return self.p1.y == self.p2.y
 
  def is_vertical(self) -> bool:
    return self.p1.x == self.p2.x
 
  def calc(self, func, val:str) -> int:
    return func(getattr(self.p1, val), getattr(self.p2, val))
 
  @property
  def points(self) -> List[Point]:
    min_x = self.calc(min, 'x')
    min_y = self.calc(min, 'y')
    max_x = self.calc(max, 'x')
    max_y = self.calc(max, 'y')
    if self.is_horizontal():
      return [Point(x, self.p1.y) for x in range(min_x, max_x+1)]
    elif self.is_vertical():
      return [Point(self.p1.x, y) for y in range(min_y, max_y+1)]
    else:
      # return []  # No diagonals
      length = range(max_x - min_x + 1)
      if ((self.p1.x < self.p2.x and self.p1.y < self.p2.y) or
          (self.p2.x < self.p1.x and self.p2.y < self.p1.y)):
        return [Point(min_x+i, min_y+i) for i in length]
      elif self.p1.x > self.p2.x and self.p1.y < self.p2.y:
        return [Point(self.p1.x-i,self.p1.y+i) for i in length]
      else:
        return [Point(self.p2.x-i,self.p2.y+i) for i in length]
 
  @staticmethod
  def parse(line: str) -> 'Vent':
    p1, p2 = [Point.parse(p) for p in line.strip().split('->')]
    return Vent(p1, p2)


class Map:
  def __init__(self):
    self.counters = Counter()
    self.dangerous_points = set()
 
  def mark_vent(self, vent: Vent) -> None:
    for p in vent.points:
      self.counters[p] += 1
      if self.counters[p] >= 2:
        self.dangerous_points.add(p)


def process_vent(filename: str) -> int:
  map = Map()
  with open(filename) as f:
    for line in f:
      map.mark_vent(Vent.parse(line))
 
  return len(map.dangerous_points)


if __name__ == '__main__':
  print(process_vent('day05-example.txt'))
  print(process_vent('day05-input.txt'))