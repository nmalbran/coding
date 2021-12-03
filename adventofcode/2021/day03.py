import sys


def to_bin(num: str) -> int:
  out = 0
  for i in range(len(num)):
    out += int(num[len(num)-i-1])*(2**i)
  return out

def get_gamma_epsil(lines):
  ones = [0] * len(lines[0].strip())

  for line in lines:
    for i, num in enumerate(line.strip()):
      ones[i] += int(num)

  # print(ones)

  total = len(lines)

  gamma = []
  epsil = []

  for num in ones:
    if num >= total/2:
      gamma.append('1')
      epsil.append('0')
    else:
      gamma.append('0')
      epsil.append('1')

  return (''.join(gamma), ''.join(epsil))

def filter_bins(lines, criteria_num):
  filtered = [line.strip() for line in lines]

  for i in range(len(filtered[0])):
    criteria = get_gamma_epsil(filtered)[criteria_num]

    filtered = [line for line in filtered if line[i]==criteria[i]]
    # print (filtered)
    if len(filtered) == 1:
      return filtered[0]


with open(sys.argv[1]) as file:
  bins = file.readlines()

gamma, epsil = get_gamma_epsil(bins)


print(f'gamma: {to_bin(gamma)}')
print(f'epsil: {to_bin(epsil)}')
print(f'part1: {to_bin(gamma)*to_bin(epsil)}')

oxy = filter_bins(bins, 0)
co2 = filter_bins(bins, 1)
print(f'oxy: {oxy}')
print(f'CO2: {co2}')
print(f'life: {to_bin(oxy)*to_bin(co2)}')