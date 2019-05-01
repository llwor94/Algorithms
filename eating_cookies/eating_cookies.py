#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution


def eating_cookies(n, cache=[1, 1, 2]):
  if not n in range(0, len(cache)):
    value = eating_cookies(
      n - 1) + eating_cookies(n - 2) + eating_cookies(n - 3)
    cache.append(value)
  return cache[n]

if __name__ == "__main__":
  
    num_cookies = 10
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  