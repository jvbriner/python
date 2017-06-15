#!/usr/bin/python3
class Node:
    def __init__(self, pos, value):
        self.pos = pos
        self.value = value
        self.connected = []
        self.visited = False
        self.total = 0   # calculated cost of subtree

maxTotal = 1001*100000 + 1 # problem statement: 10^5 * 1001 is maximum cost

# get the total cost for each subtree
def getTotalCost(node):
    :
    if node.total != 0:
        return 0  # been here before, don't double count
    
    node.total = node.value
    for i in node.connected:
        node.total += getTotalCost(i)
        
    return node.total
    
# determine which child should be removed from the
# tree so that the two trees formed will have the minimum difference in cost
def findMinCut(node, totalCost, indent = 'mincut: '):
    global maxTotal
    if node.visited:
        return maxTotal
    
    node.visited = True
    oldTreeCost = totalCost - node.total
    diff = abs(oldTreeCost - node.total)
    # print(indent, node.pos, node.value, node.total, diff)
    
    # visit children to see if the cut is them or below ...
    minChild = maxTotal
    for i in node.connected:
        childMinCut = findMinCut(i, totalCost, indent + '    ')
        if childMinCut < minChild:
            minChild = childMinCut
          
    node.visited = False
    return minChild if minChild < diff else diff

def printTree(node, indent = ''):
    return # no output
    if node.visited:
        return
    
    node.visited = True
    print(indent, node.pos, node.value, node.total)
    
    for i in node.connected:
        printTree(i, indent + '    ')

    node.visited = False
    return
        
##################################### MAIN
nNodes = int(input())
values = list(map(int,input().split()))

nodes = []
nodes.append(Node(-1, -1))  # filler for zero based array
for i in range(1, nNodes+1):
    nodes.append(Node(i, values[i-1]))
    
# read in connectivity
for edge in range(nNodes-1):
    [u,v] = list(map(int,input().split()))
    nodes[u].connected.append(nodes[v])
    nodes[v].connected.append(nodes[u])
    
root = nodes[1]
printTree(root)

getTotalCost(root)
totalCost = root.total

minCut = findMinCut(root, totalCost)
print(minCut)
