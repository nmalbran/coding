from collections import deque

DAYS = 256

def count_school(filename: str) -> int:
  school = deque([0] * 9)
 
  with open(filename) as f:
    for n in f.read().strip().split(','):
      school[int(n)] += 1
 
  for i in range(DAYS):
    created = school.popleft()
    school[6] += created
    school.append(created)
    # print(school)
  return sum(school)


if __name__ == '__main__':
  print(count_fishes('day06-example.txt'))
  print(count_fishes('day06-input.txt'))
