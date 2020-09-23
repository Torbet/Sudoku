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

def possible(y, x, n):

    if n in grid[y]:
        return(False)

    for i in range(9):
        if grid[i][x] == n:
            return(False)
    return(True)


def solve():
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for n in range(1, 10):
                    if possible(y, x, n) == True:
                        grid[y][x] = n
                        solve()
    refresh()

solve()
    

