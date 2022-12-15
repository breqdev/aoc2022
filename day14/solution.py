with open("input.txt") as f:
    lines = f.readlines()

paths = []
farthest_left = float("inf")
farthest_right = float("-inf")
deepest = 0

for line in lines:
    points = []
    parts = line.split(" -> ")
    for part in parts:
        x, y = (int(c) for c in part.split(","))
        points.append((x, y))

        if x < farthest_left:
            farthest_left = x
        if x > farthest_right:
            farthest_right = x
        if y > deepest:
            deepest = y
    paths.append(points)

print(paths)

x_start = farthest_left
width = farthest_right - farthest_left + 1
height = deepest + 1

grid = [["." for _ in range(width)] for _ in range(height)]

for path in paths:
    for first, second in zip(path[:-1], path[1:]):
        xmin, xmax = sorted((first[0], second[0]))
        ymin, ymax = sorted((first[1], second[1]))
        for x in range(xmin, xmax + 1):
            for y in range(ymin, ymax + 1):
                grid[y][x - x_start] = "#"

print("\n".join("".join(row) for row in grid))

# sand
drop_count = 0

while True:
    sand_pos = (500, 0)

    while sand_pos[1] < deepest:
        # Try to drop directly below
        if grid[sand_pos[1] + 1][sand_pos[0] - x_start] == ".":
            sand_pos = (sand_pos[0], sand_pos[1] + 1)

        # Try to drop diagonally to the left
        elif grid[sand_pos[1] + 1][sand_pos[0] - 1 - x_start] == ".":
            sand_pos = (sand_pos[0] - 1, sand_pos[1] + 1)

        # Try to drop diagonally to the right
        elif grid[sand_pos[1] + 1][sand_pos[0] + 1 - x_start] == ".":
            sand_pos = (sand_pos[0] + 1, sand_pos[1] + 1)

        # we found a resting place
        else:
            grid[sand_pos[1]][sand_pos[0] - x_start] = "o"
            drop_count += 1
            break
    else:
        # dropped into the abyss
        break

print(drop_count)
