import heapq as min_heap_esque_queue
import heapq
from queue import Queue


goalState = [[1,2,3],
            [4,5,6],
            [7,8,0]]

trivial = [[1,2,3],
           [4,5,6],
           [7,8,0]]

veryEasy = [[1,2,0],
            [4,5,6],
            [7,0,8]]


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


    #up
    copy1 = copyPuzzle(puzzle)
    #if moving blank up is valid
    if(ipos - 1 >= 0): #if there is space above the blank
        temp = copy1[ipos-1][jpos]
        copy1[ipos-1][jpos] = 0
        copy1[ipos][jpos] = temp #move blank up
        child1Node = Node(puzzle = copy1, depth = node.depth +1, parent = node, heur =heuristics(copy1,searchName,goalState)) #create node
        node.child1 = child1Node #set created node to child of original node

    
    #down
    copy2 = copyPuzzle(puzzle)
    #if moving blank down is valid
    if(ipos + 1 < len(puzzle)): #if there is space below the blank
        temp = copy2[ipos+1][jpos]
        copy2[ipos+1][jpos] = 0
        copy2[ipos][jpos] = temp #move blank down
        child2Node = Node(puzzle = copy2, depth = node.depth +1, parent = node, heur =heuristics(copy2,searchName,goalState)) #create node
        node.child2 = child2Node #set created node to child of original node

    #left 
    copy3 = copyPuzzle(puzzle)
    #if moving blank left is valid
    if(jpos - 1 >= 0): #if there is space left of the blank
        temp = copy3[ipos][jpos-1]
        copy3[ipos][jpos-1] = 0
        copy3[ipos][jpos] = temp #move blank left
        child3Node = Node(puzzle = copy3, depth = node.depth +1, parent = node, heur =heuristics(copy3,searchName,goalState)) #create node
        node.child3 = child3Node #set created node to child of original node

    
    #right
    copy4 = copyPuzzle(puzzle)
    #if moving blank right is valid
    if(jpos + 1 < len(puzzle[0])): #if there is space right of the blank
        temp = copy4[ipos][jpos+1]
        copy4[ipos][jpos+1] = 0
        copy4[ipos][jpos] = temp #move blank right
        child4Node = Node(puzzle = copy4, depth = node.depth +1, parent = node, heur =heuristics(copy4,searchName,goalState)) #create node
        node.child4 = child4Node #set created node to child of original node


    return child1Node, child2Node, child3Node, child4Node
    
    
    
    #pop the one with the least cost in the q
    #will insert all 4 children in the priority q
    #check while q is not empty when you search priority q
    # i am deisgning the priority q that sorts the weight paraemter using heur

        



def select_and_init_algorithm(puzzle):
    algorithm = input("Select algorithm. (1) for Uniform Cost Search, (2) for the Misplaced Tile Heuristic, ""or (3) the Manhattan Distance Heuristic." + '\n')
    if algorithm == "1":
        generalSearch(puzzle, heuristics(puzzle, "uniform")) #for uniform, the default heuristic is 0
    elif algorithm == "2":
        heuristicVal = heuristics(puzzle, "misplaced tile")
        misplaced_tile(puzzle) #maybe take in heuristic here
    elif(algorithm == "3"):
        heuristicVal = heuristics(puzzle, "manhattan distance")
        manhattan_distance(puzzle)
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
    selected_difficulty = input("You wish to use a default puzzle. Please enter a desired difficulty on a scale from 0 to 5." + '\n')
    if selected_difficulty == "0":
        print("Difficulty of 'Trivial' selected.")
        return trivial
    if selected_difficulty == "1":
        print("Difficulty of 'Very Easy' selected.")
        return veryEasy
    

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


def heuristics(puzzle, heurName):
    
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
        print("Invalid HeurName")


#general search
#empty q-> intialize first node
#while q is not empty, pop front of the q which will return a node (after popping see if the popped node is a goal state or not)
#generate child nodes -> insert in q after getting heuristics


#make a general search function, have the function take in the heurisitc and puzzle

#use heapq since it maintains smallest element/lowest priority at top
def generalSearch(initialState, heurName):
    nodes = [] #make empty Queue
    root = (Node(puzzle = initialState, depth = 0, parent = None, heur=heuristics(initialState, heurName, goalState)))
    heapq.heappush(nodes, (root.depth + root.heur, root)) #tuple we are using: (cost/priority, node)
    #root.depth + root.heur -> determines which node gets expanded first with using heuristics function
    #Notes: g(n) + h(n) = f(n), smallest f(n) is expanded
    Ongoing = True

    #path so far so you can trace
    visited = set()

    print("got here")
    print(root.puzzle)

    while Ongoing:
        if not nodes: #if nodes is empty
            Ongoing = False
            return Ongoing
        fnval, node = heapq.heappop(nodes) #remove cheapest node and store the node and its cost

        puzzleCheck = repr(node.puzzle) #turns it into string
        if not( puzzleCheck in visited): #check if a puzzle has been visited or not and make sure it only gets visited once
            visited.add(puzzleCheck)

        if(node.puzzle == goalState): #if puzzle is at goal state, we are finished
            return node
        c1, c2, c3, c4 =  generateChild(node, heurName) #get children notes by expanding/generating childs
        #add the child nodes to the queue
        if c1: 
            heapq.heappush(nodes, (c1.depth + c1.heur, c1))
        if c2: 
            heapq.heappush(nodes, (c2.depth + c2.heur, c2))
        if c3: 
            heapq.heappush(nodes, (c3.depth + c3.heur, c3))
        if c4:
            heapq.heappush(nodes, (c4.depth + c4.heur, c4))
    return None


    
        
        
        







 

def uniform_cost_search(puzzle): 
    return 
def misplaced_tile(puzzle, heuristic):
    return
def manhattan_distance(puzzle, heuristic):
    return

if __name__ =="__main__":
    main()