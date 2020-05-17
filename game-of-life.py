SENTINEL = '0'
POPULATED = '1'
EMPTY = '0'


def add_sentinels(grid):
    size = len(grid[0])
    sentinel_grid = [(size + 2) * SENTINEL]
    sentinel_grid += [SENTINEL + row + SENTINEL for row in grid]
    sentinel_grid.append((size + 2) * SENTINEL)
    return sentinel_grid


def get_neighbours(grid, row, col):
    neighbours = [grid[i][j] for i in range(row-1, row+2) for j in range(col-1, col+2)]
    neighbours.remove(grid[row][col])
    return neighbours


def play(grid):
    next_gen_grid = ''
    for row, line in enumerate(grid[1:-1], 1):
        for col, cell in enumerate(line[1:-1], 1):
            alive = get_neighbours(grid, row, col).count(POPULATED)
            if cell == EMPTY:
                next_gen_grid += POPULATED if alive == 3 else EMPTY
            else:
                next_gen_grid += {0: EMPTY, 1: EMPTY, 2: POPULATED, 3: POPULATED, 4: EMPTY, 5: EMPTY, 6:EMPTY, 7: EMPTY, 8: EMPTY}[alive]
        next_gen_grid += '\n'
    return next_gen_grid.strip()


def should_expand_grid(grid):
    next_gen_grid = preprocess_grid(play(add_sentinels(preprocess_grid(grid))))
    if POPULATED in next_gen_grid[0] or POPULATED in next_gen_grid[-1]:
        return True
    for row in next_gen_grid[1:-1]:
        if POPULATED in (row[0], row[-1]):
            return True
    return False


def preprocess_grid(grid):
    return grid.split('\n')


def get_grid(FILE):
    return [line.strip() for line in open(FILE)]


if should_expand_grid('\n'.join(i for i in get_grid('game_of_life.txt'))):
    grid = add_sentinels(add_sentinels(get_grid('game_of_life.txt')))
else:
    grid = add_sentinels(get_grid('game_of_life.txt'))

n = int(input())
for i in range(n):
    print(play(grid).replace(EMPTY, ' '), '\n')
    if should_expand_grid(play(grid)):
        grid = add_sentinels(add_sentinels(preprocess_grid(play(grid))))
    else:
        grid = add_sentinels(preprocess_grid(play(grid)))
