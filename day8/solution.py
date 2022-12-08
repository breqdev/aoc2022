with open("input.txt") as f:
    grid = [[int(c) for c in line.strip()] for line in f.readlines()]

visible = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]

# look down each row from the left
for row, cells in enumerate(grid):
    highest = -1
    for col, height in enumerate(cells):
        if height > highest:
            highest = height
            visible[row][col] = 1

# look down each row from the right
for row, cells in enumerate(grid):
    highest = -1
    for col, height in reversed(list(enumerate(cells))):
        if height > highest:
            highest = height
            visible[row][col] = 1

# look down each column from the top
for column in range(len(grid[0])):
    highest = -1
    for row in range(len(grid)):
        height = grid[row][column]
        if height > highest:
            highest = height
            visible[row][column] = 1

# look down each column from the bottom
for column in range(len(grid[0])):
    highest = -1
    for row in reversed(range(len(grid))):
        height = grid[row][column]
        if height > highest:
            highest = height
            visible[row][column] = 1

# for row in visible:
#     print("".join(str(h) for h in row))
print(sum(sum(row) for row in visible))

scenic_scores = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]

for y, row in enumerate(grid):
    for x, height in enumerate(row):
        right_scenic_score = 0
        for i in range(x + 1, len(row)):
            right_scenic_score += 1
            if row[i] >= height:
                break

        left_scenic_score = 0
        for i in range(x - 1, -1, -1):
            left_scenic_score += 1
            if row[i] >= height:
                break

        down_scenic_score = 0
        for i in range(y + 1, len(grid)):
            down_scenic_score += 1
            if grid[i][x] >= height:
                break

        up_scenic_score = 0
        for i in range(y - 1, -1, -1):
            up_scenic_score += 1
            if grid[i][x] >= height:
                break

        scenic_scores[y][x] = right_scenic_score * left_scenic_score * down_scenic_score * up_scenic_score

# for row in scenic_scores:
#     print("\t".join(str(h) for h in row))
print(max(max(row) for row in scenic_scores))
