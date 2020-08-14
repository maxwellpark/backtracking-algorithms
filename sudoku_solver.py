# Sudoku solver with backtracking 

grid = [
	[0,0,0,0,0,3,0,8,0],
	[0,0,4,0,0,0,1,0,9],
	[0,0,0,0,1,7,0,4,2],
	[0,5,0,0,0,0,0,0,8],
	[0,7,3,8,0,6,4,2,0],
	[8,0,0,0,0,0,0,9,0],
	[9,1,0,7,4,0,0,0,0],
	[3,0,2,0,0,0,8,0,0],
	[0,8,0,1,0,0,0,0,0]
] 

def render_grid():
    for i in range(len(grid)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(grid)):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(grid[i][j])
            else:
                print(f"{grid[i][j]} ",end="")

def next_empty_cell():
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] == 0:
                return (i, j)
    return None


def is_valid(digit, coords):
    # Row 
    for i in range(len(grid)):
        if grid[coords[0]][i] == digit and coords[1] != i:
            return False

    # Column 
    for i in range(len(grid)):
        if grid[i][coords[1]] == digit and coords[0] != i:
            return False

    # Subgrid  
    subgrid_x = coords[1] // 3
    subgrid_y = coords[0] // 3

    for i in range(subgrid_y*3, subgrid_y*3 + 3):
        for j in range(subgrid_x * 3, subgrid_x*3 + 3):
            if grid[i][j] == digit and (i,j) != coords:
                return False
    return True

def solve_grid():
    next_empty = next_empty_cell() 
	
    if not next_empty:
        return True
    else:
        row, col = next_empty

    for i in range(1,10):
        if is_valid(i, (row, col)):
            grid[row][col] = i

            if solve_grid():
                return True

            grid[row][col] = 0
            
    return False

# Entry point
print("Unsolved grid: \n") 
render_grid()
solve_grid()
print("-" * 25)
print("Solved grid: \n")
render_grid() 
