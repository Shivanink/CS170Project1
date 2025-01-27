import heapq as min_heap_esque_queue


trivial = [[1,2,3],
           [4,5,6],
           [7,8,0]]

veryEasy = [[1,2,0],
            [4,5,6],
            [7,0,8]]


#class Node:
    #def __init__(self, root, state, cost)

def select_and_init_algorithm(puzzle):
    algorithm = input("Select algorithm. (1) for Uniform Cost Search, (2) for the Misplaced Tile Heuristic, ""or (3) the Manhattan Distance Heuristic." + '\n')
    if algorithm == "1":
        heuristicVal = 0
        uniform_cost_search(puzzle) #for uniform, the default heuristic is 0
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
    for i in range(0,3): #DONT HARD CODE THIS
        print(puzzle[i])
    print('\n')

def heuristics(puzzle, heurName):
    goalState = [[1,2,3],
                 [4,5,6],
                 [7,8,0]]
    
    if heurName == "misplaced tile":
        count = 0
        for i in range(len(goalState)): #num of rows
            for j in range(len(goalState[i])): #num of columns
                if(puzzle[i][j]!= goalState[i][j] and puzzle[i][j] != 0): #check if goalstate placement is equal to puzzle; ignore 0 because its a blank
                    count += 1




def uniform_cost_search(puzzle): 
    return 
def misplaced_tile(puzzle, heuristic):
    return
def manhattan_distance(puzzle, heuristic):
    return