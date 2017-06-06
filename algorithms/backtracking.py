# Solution to https://www.hackerrank.com/challenges/count-luck/
# Backtracking problem

# Ron and Hermione are deep in the Forbidden Forest collecting potion 
# ingredients, and they've managed to lose their way. The path out of the 
# forest is blocked, so they must make their way to a portkey that will 
# transport them back to Hogwarts.

# Consider the forest as an  grid. Each cell is either empty (represented by .) 
# or blocked by a tree (represented by ). Ron and Hermione can move (together 
# inside a single cell) LEFT, RIGHT, UP, and DOWN through empty cells, but 
# they cannot travel through a tree cell. Their starting cell is marked with 
# the character , and the cell with the portkey is marked with a . 
# The upper-left corner is indexed as .

# .X.X......X
# .X*.X.XXX.X
# .XX.X.XM...
# ......XXXX.
# In example above, Ron and Hermione are located at index  and the portkey 
# is at . Each cell is indexed according to Matrix Conventions

# Hermione decides it's time to find the portkey and leave. Each time they 
# are able to move in more than one direction, she waves her wand and it 
# points to the correct direction. Ron is betting that she will have to wave 
# her wand exactly  times. Can you determine if Ron's guesses are correct?

# Note: It is guaranteed that there is only one path from the starting 
# location to the portkey.

# Input Format

# The first line contains an integer, , the number of test cases.

# Each test case is described as follows: 
# The first line contains  space-separated integers,  and , respectively, 
# denoting the forest matrix. 
# The  subsequent lines each contain a string of length  describing a row of 
# the forest matrix. 
# The last line contains an integer, , denoting Ron's guess as to how many 
# times Hermione will wave her wand.

# Constraints

# There will be exactly one  and one  in the forest.
# Exactly one path exists between  and .
# Output Format

# On a new line for each test case, print  if Ron impresses Hermione by 
# guessing correctly; otherwise, print .

# Sample Input

# 3
# 2 3
# *.M
# .X.
# 1
# 4 11
# .X.X......X
# .X*.X.XXX.X
# .XX.X.XM...
# ......XXXX.
# 3
# 4 11
# .X.X......X
# .X*.X.XXX.X
# .XX.X.XM...
# ......XXXX.
# 4
# Sample Output

# Impressed
# Impressed
# Oops!
# Explanation

# For each test case ,  denotes the number of times Hermione waves her wand.

# Case 0: Hermione waves her wand at , giving us . Because , we print  on a 
# new line. 
# Case 1: Hermione waves her wand at , , and , giving us . Because , we print  
# on a new line. 
# Case 2: Hermione waves her wand at , , and , giving us . Because and ,  and 
# we print  on a new line.
#     

class MagicForest:
    def __init__(self):
        # read forest map from stdin
        [self.numRows, self.numCols] = list(map(int, input().split()))
        
        # initialize the forest map
        self.forest = []
        for i in range(self.numRows):
            self.forest.append(list(input()))
            
        self.inf = 1000000  # infinity
        self.print('The initial forest')
            
    def findStart(self):
        for row in range(self.numRows):
            for col in range(self.numCols):
                if (self.forest[row][col] == 'M'):
                    return [row, col]
        return [-1, -1]

    def print(self, message='forest'):
        return  # skip printing
        print('-----------', message)
        for i in range(self.numRows):
            print(*self.forest[i],sep='')
        print('-----------', flush=True)
        
    # generate options at row, col
    def options(self, row, col):
        opts = []
        if row-1 >= 0 and (self.forest[row-1][col] == '.' or self.forest[row-1][col] == '*'):
            opts.append([row-1, col])
        if row+1 < self.numRows and (self.forest[row+1][col] == '.' or self.forest[row+1][col] == '*'):
            opts.append([row+1, col])
        if col-1 >= 0 and (self.forest[row][col-1] == '.' or self.forest[row][col-1] == '*'):
            opts.append([row, col-1])
        if col+1 < self.numCols and (self.forest[row][col+1] == '.' or self.forest[row][col+1] == '*'):
            opts.append([row, col+1])
        # print("options: ", opts)
        return opts
    
    # find the port key from position row, col
    # return inf if no path, otherwise number of wand uses needed
    def findPK(self, row, col):
        self.print(str(row)+','+str(col) + ' ' + self.forest[row][col])
        
        if self.forest[row][col] == '*':
            self.print('soln found: '+str(row)+ ' '+str(col))
            return 0
        
        opts = self.options(row, col)
        if len(opts) == 0:
            self.forest[row][col] = 'D'
            self.print('deadend: '+str(row)+ ' '+str(col))
            return self.inf

        if len(opts) == 1:
            self.forest[row][col] = 'S'
            self.print('same dir: '+str(row)+ ' '+str(col))
            return self.findPK(opts[0][0], opts[0][1])

        self.print('wand needed: '+str(row)+ ' '+str(col))
        self.forest[row][col] = 'W'
       
        # mark all options so that we can the minimum option
        for opt in opts:
            if self.forest[opt[0]][opt[1]] == '*':
                self.print('Special last wand')
                return 1
            self.forest[opt[0]][opt[1]] = 'O'
            
        self.print('Options with wand')
            
        minOption = self.inf
        # investigate the options
        for opt in opts:
            cost = self.findPK(opt[0], opt[1])
            if cost < minOption:
                minOption = cost
                
        return minOption + 1
                    
t = int(input())
for trial in range(t):
    mf = MagicForest()
    [row, col] = mf.findStart()
    numWand = mf.findPK(row, col)
    
    guess = int(input())
    
    if numWand == guess:
        print("Impressed")
    else:
        print("Oops!")

