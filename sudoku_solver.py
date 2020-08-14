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
