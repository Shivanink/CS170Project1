import heapq as min_heap_esque_queue
import heapq
from queue import Queue
import time


goalState = [[1,2,3],
            [4,5,6],
            [7,8,0]]

trivial = [[1,2,3],
           [4,5,6],
           [7,8,0]]

veryEasy = [[1,2,3],
            [4,5,6],
            [7,0,8]]
            
easy     =  [[1,2,0],
            [4,5,3],
            [7,8,6]]

doable = [[0,1,2],
        [4,5,3],
        [7,8,6]]
ohboy =  [[8,7,1],
        [6,0,2],
        [5,4,3]]



class Node:
    def __init__(self, puzzle, root = None, depth = 0, parent = None,  heur = 0):
        self.puzzle = puzzle #current puzzle
        if(parent == None):
            self.root = self #set root to current node
        else:
            self.root = parent.root #else use parent's root
        self.depth = depth #depth/level of the tree
        self.parent = parent #parent/previous state of puzzle
        self.heur = heur #heurisitc value for the node
        self.child1 = None #up
        self.child2 = None #down
        self.child3 = None #left
        self.child4 = None #right
    def __lt__(self, other): #function that compares nodes, also min queue works with smallest values first
        return (self.depth + self.heur) < (other.depth + other.heur)

def findblank(puzzle) : #finds 0
    for i in range(len(puzzle)):
        for j in range(len(puzzle[i])):
            if(puzzle[i][j] == 0):
                return i, j
    
def copyPuzzle(puzzle): #to make a copy of the puzzle
    copy =[]
    for i in puzzle:
        row = []
        for j in i:
            row.append(j)
        copy.append(row)
    return copy



def generateChild(node, searchName):
    puzzle = node.puzzle
    #find posiiton of blank (0)
    ipos, jpos = findblank(puzzle)
    #see if it can move up, down, left, or right - ensure each is valid

    child1Node = None
    child2Node = None
    child3Node = None
    child4Node = None

    #up
    copy1 = copyPuzzle(puzzle)
    #if moving blank up is valid
    if(ipos - 1 >= 0): #if there is space above the blank
        temp = copy1[ipos-1][jpos]
        copy1[ipos-1][jpos] = 0
        copy1[ipos][jpos] = temp #move blank up
        child1Node = Node(puzzle = copy1, depth = node.depth +1, parent = node, heur =heuristics(copy1,searchName)) #create node
        node.child1 = child1Node #set created node to child of original node

    
    #down
    copy2 = copyPuzzle(puzzle)
    #if moving blank down is valid
    if(ipos + 1 < len(puzzle)): #if there is space below the blank
        temp = copy2[ipos+1][jpos]
        copy2[ipos+1][jpos] = 0
        copy2[ipos][jpos] = temp #move blank down
        child2Node = Node(puzzle = copy2, depth = node.depth +1, parent = node, heur =heuristics(copy2,searchName)) #create node
        node.child2 = child2Node #set created node to child of original node

    #left 
    copy3 = copyPuzzle(puzzle)
    #if moving blank left is valid
    if(jpos - 1 >= 0): #if there is space left of the blank
        temp = copy3[ipos][jpos-1]
        copy3[ipos][jpos-1] = 0
        copy3[ipos][jpos] = temp #move blank left
        child3Node = Node(puzzle = copy3, depth = node.depth +1, parent = node, heur =heuristics(copy3,searchName)) #create node
        node.child3 = child3Node #set created node to child of original node

    
    #right
    copy4 = copyPuzzle(puzzle)
    #if moving blank right is valid
    if(jpos + 1 < len(puzzle[0])): #if there is space right of the blank
        temp = copy4[ipos][jpos+1]
        copy4[ipos][jpos+1] = 0
        copy4[ipos][jpos] = temp #move blank right
        child4Node = Node(puzzle = copy4, depth = node.depth +1, parent = node, heur =heuristics(copy4,searchName)) #create node
        node.child4 = child4Node #set created node to child of original node


    children = [] #list of children

    #ensure all the children are valid
    if child1Node:
        children.append(child1Node)
    if child2Node:
        children.append(child2Node)
    if child3Node:
        children.append(child3Node)
    if child4Node:
        children.append(child4Node)
    return children
    
    
    
    #pop the one with the least cost in the q
    #will insert all 4 children in the priority q
    #check while q is not empty when you search priority q
    # i am deisgning the priority q that sorts the weight paraemter using heur

        



def select_and_init_algorithm(puzzle):
    algorithm = input("Select algorithm. (1) for Uniform Cost Search, (2) for the Misplaced Tile Heuristic, ""or (3) the Manhattan Distance Heuristic." + '\n')
    if algorithm == "1":
        generalSearch(puzzle, "uniform") #for uniform, the default heuristic is 0
    elif algorithm == "2":
        generalSearch(puzzle, "misplaced tile")
    elif(algorithm == "3"):
        generalSearch(puzzle, "manhattan distance")
    else:
        print("Invalid input")


def main():
    puzzle_mode = input("Welcome to an 8-Puzzle Solver. Type '1' to use a default puzzle, or '2' to create your own."+ '\n')
    if puzzle_mode == "1":
        select_and_init_algorithm(init_default_puzzle_mode()) #algorithm
    if puzzle_mode == "2":
        print("Enter your puzzle, using a zero to represent the blank. " + "Please only enter valid 8-puzzles. Enter the puzzle demilimiting " +"the numbers with a space. RET only when finished." + '\n')
        puzzle_row_one = input("Enter the first row: ")
        puzzle_row_two = input("Enter the second row: ")
        puzzle_row_three = input("Enter the third row: ")
        puzzle_row_one = puzzle_row_one.split()
        puzzle_row_two = puzzle_row_two.split()
        puzzle_row_three = puzzle_row_three.split()
        for i in range(0, 3):
            puzzle_row_one[i] = int(puzzle_row_one[i])
            puzzle_row_two[i] = int(puzzle_row_two[i])
            puzzle_row_three[i] = int(puzzle_row_three[i])
        user_puzzle = [puzzle_row_one, puzzle_row_two, puzzle_row_three]
        select_and_init_algorithm(user_puzzle)
    return 

def init_default_puzzle_mode():
    selected_difficulty = input("You wish to use a default puzzle. Please enter a desired difficulty on a scale from 0 to 4." + '\n')
    if selected_difficulty == "0":
        print("Difficulty of 'Trivial' selected.")
        return trivial
    if selected_difficulty == "1":
        print("Difficulty of 'Very Easy' selected.")
        return veryEasy
    if selected_difficulty == "2":
        print("Difficulty of 'Easy' selected.")
        return easy
    if selected_difficulty == "3":
        print("Difficulty of 'Doable' selected.")
        return doable
    if selected_difficulty == "4":
        print("Difficulty of 'Easy' selected.")
        return ohboy

    

def print_puzzle(puzzle):
    for i in range(0,3): 
        print(puzzle[i])
    print('\n')


def mapping(goalState): #general function to create dictionary so you can map the values and find out where all the numbers are
    chart = {} #create empty dict - chart that will store location of all tiles currently
    for i in range(len(goalState)):
        for j in range(len(goalState[i])): #calculates key for dict
            chart[goalState[i][j]] = (i,j) #adds tuple (value) to the chart (dictionary)
    return chart


def heuristics(puzzle, heurName): #returns heuristic
    
    if heurName == "misplaced tile":
        count = 0
        for i in range(len(goalState)): #num of rows
            for j in range(len(goalState[i])): #num of columns
                if(puzzle[i][j]!= goalState[i][j] and puzzle[i][j] != 0): #check if goalstate placement is equal to puzzle; ignore 0 because its a blank
                    count += 1
        return count
    elif heurName == "manhattan distance": #need to find shortest distance to goal position for each tile, and add all the ones that arent in the goal position
        positions = mapping(goalState)
        distance = 0
        for i in range(len(puzzle)):
            for j in range(len(puzzle[i])):
                chosen = puzzle[i][j]
                if (chosen != 0 and puzzle[i][j] != goalState[i][j]): #if its not a blank tile and if its already not in the goal position, then get its distance
                    actual_i = positions[chosen][0]
                    actual_j = positions[chosen][1]
                    distance += abs(j - actual_j) + abs(i - actual_j)
        return distance
    
    elif heurName == "uniform":
        return 0 #for uniform
    else:
        raise ValueError("Invalid Heurisitic Name")


#general search
#empty q-> intialize first node
#while q is not empty, pop front of the q which will return a node (after popping see if the popped node is a goal state or not)
#generate child nodes -> insert in q after getting heuristics


#make a general search function, have the function take in the heurisitc and puzzle

#use heapq since it maintains smallest element/lowest priority at top
def generalSearch(initialState, heurName):
    nodes = [] #make empty Queue

    starting = time.perf_counter()

    root = (Node(puzzle = initialState, depth = 0, parent = None, heur=heuristics(initialState, heurName)))
    heapq.heappush(nodes, (root.depth + root.heur, root)) #tuple we are using: (cost/priority, node)
    #root.depth + root.heur -> determines which node gets expanded first with using heuristics function
    #Notes: g(n) + h(n) = f(n), smallest f(n) is expanded


    #DOUBLE CHECK U ARE USING MIN HEAP
    Ongoing = True

    #path so far so you can trace
    visited = set()
   # count1 = 0
    maxQlen = 0 #find len of the max queue
    expandedCount = 0


    while Ongoing: #check heap size instead
       # print("ongoing")
        if not nodes: #if nodes is empty
            print("Queue empty")
            Ongoing = False
            return Ongoing
        maxQlen = max(len(nodes), maxQlen)
        fnval, node = heapq.heappop(nodes) #remove cheapest node and store the node and its cost
        #count1 += 1
        #print(f"count: {count1}")
    

        nodeTuple = []
        for i in node.puzzle:
            nodeTuple.append(tuple(i))
        nodeTuple = tuple(nodeTuple)

        goalTuple = []
        for i in goalState:
            goalTuple.append(tuple(i))
        goalTuple = tuple(goalTuple)
        #print(nodeTuple, goalTuple)
        if(nodeTuple == goalTuple): #if puzzle is at goal state, we are finished
            depth = node.depth #depth of final node
            correctPath = []
            while node:
                correctPath.append(node.puzzle)
                node = node.parent
            correctPath.reverse()
            for i in correctPath:
                print_puzzle(i)
            ending = time.perf_counter()

            totalTime = (ending - starting) #caclulate duration
            totalTime = round(totalTime, 4) #round to 5th place
            print(f"Time to Run: {totalTime} seconds")
            print(f"Depth: {depth}")
            print(f"Number of expanded nodes: {expandedCount}")
            print(f"Max Queue Length: {maxQlen}")
            print("Goal Reached!")
            return node

        '''
        puzzleCheck = [] #turn list of lists into tuple of tuples so its immutable and we can hash
        for i in node.puzzle:
            puzzleCheck.append(tuple(i)) #turn each row to a tuple
        puzzleCheck = tuple(puzzleCheck) #list of tuples to tuple of tuples

        if puzzleCheck in visited: #check if a puzzle has been visited or not and make sure it only gets visited once
            continue
        '''

        if nodeTuple in visited:
            #print("nodeTuple is in visited")
            continue
        
        
        visited.add(nodeTuple) #updated visited set, was puzzle check before
        #print("generating child for count", count1)
        expandedCount += 1
        children =  generateChild(node, heurName) #get children notes by expanding/generating childs
        #print('got here for pusihing children in the queue')
       # print(len(children))
        #add the child nodes to the queue
        for i in children:
            if i is not None:
                state = []
                for j in i.puzzle:
                    state.append(tuple(j))
                state = tuple(state)
                #print(f"state:{state} visited: {visited}")
                if state not in visited:
                    # visited.add(state)
                    heapq.heappush(nodes, (i.depth + i.heur, i))
                
        
    return None


    #keep track of depth
    # #keep track of time it takes to run for the graphs       
        
        







if __name__ =="__main__":
    main()