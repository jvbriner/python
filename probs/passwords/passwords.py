#!/usr/bin/python3
#
# solution: https://www.hackerrank.com/challenges/password-cracker
#
import sys

def search(word, words, indent=''):
    global memo
    if word in memo:
        return memo[word]
    
    # each search must decrease the size of word
    # print(indent, "-----> ", word)
    if word == "":
        # print(indent, "FOUND ")
        memo[word] = []
        return memo[word]
    
    for i in words:
        l = len(i)
        # print(indent, "   testing ", i)
        if i == word[0:l]:
            result = search(word[l:], words, indent+"   ")
            if result != None:
                result.insert(0,i)
                # print(indent, "   found ", result)
                memo[word] = result[:]
                return memo[word]

    memo[word] = None
    return memo[word]

sys.setrecursionlimit(4000)

t = int(input())
for i in range(t):
    n = int(input())
    words = input().split()
    p = input().strip()
    memo = {}
    results = search(p,words)
    if results != None:
        print(*results)
    else:
        print("WRONG PASSWORD")
