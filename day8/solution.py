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
        print(f"Row {row} col {column} height {height} highest {highest}")
        if height > highest:
            highest = height
            print("marking visible")
            visible[row][column] = 1

# look down each column from the bottom
for column in range(len(grid[0])):
    highest = -1
    for row in reversed(range(len(grid))):
        height = grid[row][column]
        if height > highest:
            highest = height
            visible[row][column] = 1

for row in visible:
    print("".join(str(h) for h in row))
print(sum(sum(row) for row in visible))
