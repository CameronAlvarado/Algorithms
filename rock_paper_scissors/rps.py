#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  rps = ['rock', 'paper', 'scissors']
  combinations = [] 
    # from lecture, ensure the arguments coming in are expected types
  def helper_function(n: int, result: list): # not needed, just defines types
    if n == 0:
      return combinations.append(result)
    for y in rps:
      helper_function(n - 1, result + [y])
  helper_function(n, [])
  return combinations

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')