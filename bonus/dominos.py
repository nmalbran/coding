

def dominos(input: str) -> str:
  length = len(input)
  right = [None] * (length + 1)
  left = right[:]

  for r in range(length):
    # Process to the right
    if input[r] == 'R':
      right[r+1] = 0
    elif input[r] == 'O' and right[r] is not None:
      right[r+1] = right[r] + 1

    # Process to the left
    l = length - r - 1
    if input[l] == 'L':
      left[l] = 0
    elif input[l] == 'O' and left[l+1] is not None:
      left[l] = left[l+1] + 1


  out = []
  for i in range(length):
    letter = input[i]
    if (letter in ['R', 'L'] or  # R & L don't change
        right[i+1] == left[i]):  # O that was not pushed or pushed equally
      out.append(letter)

    elif right[i+1] is None:     # No right pushing
      out.append('L')
    elif (left[i] is None or     # No left pushing
          right[i+1] < left[i]): # Both pushing, right is closer
      out.append('R')
    else:                        # Both pushing, left is closer
      out.append('L')

  return ''.join(out)



TESTS = [
  ('OROOOLOO', 'ORROLLOO'),
  ('OOLOOO', 'LLLOOO'),
  ('OROOLOO', 'ORRLLOO'),
  ('OROO', 'ORRR'),
  ('ROOO', 'RRRR'),
  ('OLORO', 'LLORR'),
  ('OROOROOOLOROOLO', 'ORRRRROLLORRLLO'),
]

for case, expected in TESTS:
  out = dominos(case)
  if out != expected:
    print(f'''
Failed:   {case}
Expected: {expected}
Was:      {out}''')