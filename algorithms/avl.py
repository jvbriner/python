#
# used for solution to https://www.hackerrank.com/challenges/minimum-loss
#
# Lauren has a chart of distinct projected prices for a house over the next  years, where the price of the house in the  year is . She wants to purchase and resell the house at a minimal loss according to the following rules:
# 
# The house cannot be sold at a price greater than or equal to the price it was purchased at (i.e., it must be resold at a loss).
# The house cannot be resold within the same year it was purchased.
# Find and print the minimum amount of money Lauren must lose if she buys the house and resells it within the next  years.
# 
# Note: It's guaranteed that a valid answer exists.
# 
# Input Format
# 
# The first line contains an integer, , denoting the number of years of house data. 
# The second line contains  space-separated long integers describing the respective values of .
# 
# Constraints
# 
# All the prices are distinct.
# It's guaranteed that a valid answer exists.
# Subtasks
# 
#  for  of the maximum score.
# Output Format
# 
# Print a single integer denoting the minimum amount of money Lauren must lose if she buys and resells the house within the next  years.
# 
# Sample Input 0
# 
# 3
# 5 10 3
# Sample Output 0
# 
# 2
# Explanation 0
# 
# Lauren buys the house in year  at price  and sells it in year  at  for a minimal loss of .
# 
# Sample Input 1
# 
# 5
# 20 7 8 2 5
# Sample Output 1
# 
# 2
# Explanation 1
# 
# Lauren buys the house in year  at price  and sells it in year  at  for a minimal loss of 1
#
#
##  Implementation of AVL tree
#
#   Author: Tim Rijavec
#           tim@coder.si
#           http://coder.si

class avlnode(object):
    """
    A node in an avl tree.
    """

    def __init__(self, key):
        "Construct."

        # The node's key
        self.key = key
        # The node's left child
        self.left = None
        # The node's right child
        self.right = None

    def __str__(self):
        "String representation."
        return str(self.key)

    def __repr__(self):
        "String representation."
        return str(self.key)
    
class avltree(object):    
    """
    An avl tree.
    """
    
    def __init__(self):
        "Construct."

        # Root node of the tree.
        self.node = None
        # Height of the tree.
        self.height = -1
        # Balance factor of the tree.
        self.balance = 0
        
    def insert(self, key):
        """
        Insert new key into node
        """
        # Initial tree
        if not self.node:
            self.node = avlnode(key)
            self.node.left = avltree()
            self.node.right = avltree()
            value = None
        # Insert key to the left subtree
        elif key < self.node.key:
            value = self.node.left.insert(key)
        # Insert key to the right subtree
        elif key > self.node.key:
            value = self.node.right.insert(key)
            
        selfkey = self.node.key
        
        # Rebalance tree if needed
        self.rebalance()
        
        if selfkey > key:
            if value == None:
                return selfkey
            if value > key:
                return value if value < selfkey else selkey
        else:
            if value != None and value > key:
                return value   
        return None


    def nextLargest(self, key):
        """
        find nextLargest to key in tree
        """
        
        # Initial tree
        if not self.node:
            return None
        
        # look to the left subtree
        if key < self.node.key:
            value = self.node.left.nextLargest(key)
        # look to the right subtree
        elif key > self.node.key:
            value = self.node.right.nextLargest(key)
        else:
            raise Exception('should not find self')
        
        if self.node.key > key:
            if value == None:
                return self.node.key
            if value > key:
                return value if value < self.node.key else self.node.key
        else:
            if value != None and value > key:
                return value
            
        return None
        
    def rebalance(self):
        """
        Rebalance tree. After inserting or deleting a node, 
        it is necessary to check each of the node's ancestors for consistency with the rules of AVL
        """

        # Check if we need to rebalance the tree
        #   update height
        #   balance tree
        self.update_heights(recursive=False)
        self.update_balances(False)

        # For each node checked, 
        #   if the balance factor remains −1, 0, or +1 then no rotations are necessary.
        while self.balance < -1 or self.balance > 1: 
            # Left subtree is larger than right subtree
            if self.balance > 1:

                # Left Right Case -> rotate y,z to the left
                if self.node.left.balance < 0:
                    #     x               x
                    #    / \             / \
                    #   y   D           z   D
                    #  / \        ->   / \
                    # A   z           y   C
                    #    / \         / \
                    #   B   C       A   B
                    self.node.left.rotate_left()
                    self.update_heights()
                    self.update_balances()

                # Left Left Case -> rotate z,x to the right
                #       x                 z
                #      / \              /   \
                #     z   D            y     x
                #    / \         ->   / \   / \
                #   y   C            A   B C   D 
                #  / \ 
                # A   B
                self.rotate_right()
                self.update_heights()
                self.update_balances()
            
            # Right subtree is larger than left subtree
            if self.balance < -1:
                
                # Right Left Case -> rotate x,z to the right
                if self.node.right.balance > 0:
                    #     y               y
                    #    / \             / \
                    #   A   x           A   z
                    #      / \    ->       / \
                    #     z   D           B   x
                    #    / \                 / \
                    #   B   C               C   D
                    self.node.right.rotate_right() # we're in case III
                    self.update_heights()
                    self.update_balances()

                # Right Right Case -> rotate y,x to the left
                #       y                 z
                #      / \              /   \
                #     A   z            y     x
                #        / \     ->   / \   / \
                #       B   x        A   B C   D 
                #          / \ 
                #         C   D
                self.rotate_left()
                self.update_heights()
                self.update_balances()

    def update_heights(self, recursive=True):
        """
        Update tree height

        Tree height is max height of either left or right subtrees +1 for root of the tree
        """
        if self.node: 
            if recursive: 
                if self.node.left: 
                    self.node.left.update_heights()
                if self.node.right:
                    self.node.right.update_heights()
            
            self.height = 1 + max(self.node.left.height, self.node.right.height)
        else: 
            self.height = -1

    def update_balances(self, recursive=True):
        """
        Calculate tree balance factor

        The balance factor is calculated as follows: 
            balance = height(left subtree) - height(right subtree). 
        """
        if self.node:
            if recursive:
                if self.node.left:
                    self.node.left.update_balances()
                if self.node.right:
                    self.node.right.update_balances()

            self.balance = self.node.left.height - self.node.right.height
        else:
            self.balance = 0 

            
    def rotate_right(self):
        """
        Right rotation
            set self as the right subtree of left subree
        """
        new_root = self.node.left.node
        new_left_sub = new_root.right.node
        old_root = self.node

        self.node = new_root
        old_root.left.node = new_left_sub
        new_root.right.node = old_root

    def rotate_left(self):
        """
        Left rotation
            set self as the left subtree of right subree
        """
        new_root = self.node.right.node
        new_left_sub = new_root.left.node
        old_root = self.node

        self.node = new_root
        old_root.right.node = new_left_sub
        new_root.left.node = old_root

    def delete(self, key):
        """
        Delete key from the tree

        Let node X be the node with the value we need to delete, 
        and let node Y be a node in the tree we need to find to take node X's place, 
        and let node Z be the actual node we take out of the tree.

        Steps to consider when deleting a node in an AVL tree are the following:

            * If node X is a leaf or has only one child, skip to step 5. (node Z will be node X)
                * Otherwise, determine node Y by finding the largest node in node X's left sub tree 
                    (in-order predecessor) or the smallest in its right sub tree (in-order successor).
                * Replace node X with node Y (remember, tree structure doesn't change here, only the values). 
                    In this step, node X is essentially deleted when its internal values were overwritten with node Y's.
                * Choose node Z to be the old node Y.
            * Attach node Z's subtree to its parent (if it has a subtree). If node Z's parent is null, 
                update root. (node Z is currently root)
            * Delete node Z.
            * Retrace the path back up the tree (starting with node Z's parent) to the root, 
                adjusting the balance factors as needed.
        """
        if self.node != None:
            if self.node.key == key:
                # Key found in leaf node, just erase it
                if not self.node.left.node and not self.node.right.node:
                    self.node = None
                # Node has only one subtree (right), replace root with that one
                elif not self.node.left.node:                
                    self.node = self.node.right.node
                # Node has only one subtree (left), replace root with that one
                elif not self.node.right.node:
                    self.node = self.node.left.node
                else:
                    # Find  successor as smallest node in right subtree or
                    #       predecessor as largest node in left subtree
                    successor = self.node.right.node  
                    while successor and successor.left.node:
                        successor = successor.left.node

                    if successor:
                        self.node.key = successor.key

                        # Delete successor from the replaced node right subree
                        self.node.right.delete(successor.key)

            elif key < self.node.key:
                self.node.left.delete(key)

            elif key > self.node.key:
                self.node.right.delete(key)

            # Rebalance tree
            self.rebalance()

    def inorder_traverse(self):
        """
        Inorder traversal of the tree
            Left subree + root + Right subtree
        """
        result = []

        if not self.node:
            return result
        
        result.extend(self.node.left.inorder_traverse())
        result.append(self.node.key)
        result.extend(self.node.right.inorder_traverse())

        return result

    def display(self, node=None, indent=""):
        if not node:
            node = self.node

        if node.right.node:
            self.display(node.right.node, indent + "   R")

        print(indent + '-', node)

        if node.left.node:
             self.display(node.left.node, indent + "   L")

tree = avltree()
n = int(input())
pricing = list(map(int,input().split()))
minCost = None

for i in range(n):
    pr = pricing[i]
    nextLarge = tree.insert(pr)
    # print(pricing[0:i+1], nextLarge, minCost)
    if nextLarge != None:
        diff = nextLarge - pr
        if minCost == None or diff < minCost:
            # print("new minCost", minCost)
            minCost = diff
    # tree.display()
print(minCost)

