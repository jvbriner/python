#!/usr/bin/python3
n = int(input())
a = list(map(int, input().split()))

def qsort(a, indent = ""):
    
    if len(a) <= 1:
        return a

    key = a[0]
    left = []
    right = []
    middle = []

    for i in range(len(a)):
        if a[i] > key:
            right.append(a[i])
        elif a[i] < key:
            left.append(a[i])
        else:
            middle.append(a[i])
            
    left = qsort(left, indent + "  L ")
    right = qsort(right, indent + "  R ")
    
    left.extend(middle)
    left.extend(right)
    return left

a = qsort(a)
print(*a)
