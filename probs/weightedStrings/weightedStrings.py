#!/usr/bin/python3
#
# Solution to: https://www.hackerrank.com/challenges/weighted-uniform-string
#

import sys

s = input().strip()
n = int(input().strip())

# your code goes here
nums = map(lambda n: ord(n)-ord('a')+1, list(s))
existSet = set()
lastVal = -1
lastSum = -1
for i in nums:
    if (lastVal != i):
        lastVal = i
        lastSum = i
    else:
        lastSum += i 
    existSet.add(lastSum)
    
for a0 in range(n):
    x = int(input().strip())
    if x in existSet:
        print("Yes")
    else:
        print("No")
