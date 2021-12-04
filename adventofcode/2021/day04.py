from typing import List, Tuple

BOARD_SIZE = 5


class Board:
  def __init__(self, table: List[List]) -> None:
    self.numbers = {}
    self.rows = [0] * BOARD_SIZE
    self.columns = [0] * BOARD_SIZE
    self.numbers_left = set()
    self._has_won = False

    for r in range(BOARD_SIZE):
      for c in range(BOARD_SIZE):
        self.numbers[table[r][c]] = (r,c)
        self.numbers_left.add(table[r][c])

  def mark(self, num: int) -> None:
    if num in self.numbers:
      row, col = self.numbers[num]
      self.numbers_left.discard(num)
      self.rows[row] += 1
      self.columns[col] += 1
      self._has_won = (self.rows[row] == BOARD_SIZE or 
                       self.columns[col] == BOARD_SIZE)

  def has_won(self) -> bool:
    return self._has_won

  def score(self, last_num: int) -> int:
    return sum(self.numbers_left) * last_num

  @staticmethod
  def parse_board(lines: List[str]) -> 'Board':
    table = []
    for line in lines:
      table.append([int(n) for n in line.strip().split()])
    return Board(table)


def parse_game(filename: str) -> Tuple[List[Board], List[int]]:
  with open(filename) as f:
    lines = f.readlines()

  numbers = [int(n) for n in lines[0].strip().split(',')]

  boards = []
  for i in range(2, len(lines), 6):
    boards.append(Board.parse_board(lines[i:i+5]))

  return (boards, numbers)


def first_to_win(filename: str) -> int:
  boards, numbers = parse_game(filename)

  for num in numbers:
    for board in boards:
      board.mark(num)
      if board.has_won():
        return board.score(num)
  raise ValueError('No Board won')


def last_to_win(filename: str) -> int:
  boards, numbers = parse_game(filename)

  for num in numbers:
    for board in boards:
      board.mark(num)

    if len(boards) == 1 and boards[0].has_won():
      return boards[0].score(num)

    boards = [board for board in boards if not board.has_won()]

  raise ValueError('No Board won')


if __name__ == '__main__':
  import sys
  print(first_to_win(sys.argv[1]))
  print(last_to_win(sys.argv[1]))
