grid = [[6,5,0,8,7,3,0,9,0],
        [0,0,3,2,5,0,0,0,8],
        [9,8,0,1,0,4,3,5,7],
        [1,0,5,0,0,0,0,0,0],
        [4,0,0,0,0,0,0,0,2],
        [0,0,0,0,0,0,5,0,3],
        [5,7,8,3,0,1,0,2,6],
        [2,0,0,0,4,8,9,0,0],
        [0,9,0,6,2,5,0,8,1]]

def refresh():
    print('\n')
    for row in grid:
        for i in row:
            print(i, end="   ")
        print('\n')

def possible(x, y, n):
	for i in range (0, 9):
		if grid[i][y] == n:
			return False
	for j in range (9):
		if grid[x][j] == n:
			return False

	x0 = (x // 3) * 3
	y0 = (y // 3) * 3

	for i in range(3):
		for j in range(3):
			if grid[x0 + i][y0 + i] == n:
				return False
	return True

def solved():
	print('solved: \n')

def solve():
	for y in range(9):
		for x in range(9):
			if grid[y][x] == 0:
				for n in range(1, 10):
					if possible(y, x, n):
						grid[y][x] = n
						solve()
						grid[y][x] = 0
				return
	refresh()

refresh()
solve()


